import streamlit as st
from forecast_class import Forecast
from datetime import datetime, timedelta
import plotly.graph_objects as go
import pandas as pd

class PredPage():
    def __init__(self, model: Forecast, lang):
        '''
            Page that will show the price prediction for the next 7 days
        
        '''

        # Adjusting text based on the language
        st.write('## Price Prediciton' if lang == "EN" else '## Predição do Preço')

        # Predicting the price
        model.predict_future_days()

        # Getting the predictions
        preds = model.seven_days_pred

        # Get historical data
        real_data = model.df_real

        def custom_legend_name(fig, new_names):
            '''
                This function will help adjusting the chart legend

            '''
            for i, new_name in enumerate(new_names):
                fig.data[i].name = new_name

        
        @st.cache_data()        
        def get_date():
            '''
                Getting start and end date from the DF.
            
            '''
            start_date = pd.to_datetime(real_data.Date).min().timestamp()
            end_date = pd.to_datetime(preds.index).max().timestamp()

            start_date = datetime.fromtimestamp(start_date)
            end_date = datetime.fromtimestamp(end_date)

            return start_date, end_date

        start_date, end_date = get_date()

        # Adjusting date slider
        selected_date_range = st.slider(
            "Select a date range" if lang == "EN" else 'Selecione um espaço de tempo',
            min_value=start_date,
            max_value=end_date,
            value=(end_date - + timedelta(weeks=20), end_date),
            step=timedelta(days=1),
        )
        start = datetime.date(selected_date_range[0])

        # Filtering data based on the date slider
        real_data = real_data.loc[start:]

        # Getting relevant colmns
        real_data = real_data[['Date', 'Close']]
        preds['Date'] = preds.index
        preds = preds[['Date', 'Close']]

        # Concating the DFs for better chart visualization
        real_data = pd.concat([real_data, preds])

        # Creating the price prediction chart
        fig_model = go.Figure(data=[go.Scatter(x=real_data.Date, y=real_data['Close'], line=dict(color='purple', width=3)),
                                    go.Scatter(x=preds.index, y=preds['Close'], line=dict(color='orange', width=3))])
        fig_model.update_layout(title='Brent Price Prediciton in USD' if lang == "EN" else 'Predição do preço do Petróleo em dólar')
        custom_legend_name(fig_model, ['Real Price' if lang == "EN" else 'Preço Real', 'Prediction' if lang == "EN" else 'Predição'])

        # Creating DF with prediciton
        preds.index = preds.index.strftime('%Y-%m-%d')
        preds = preds.T

        # Showing the DF with preds
        st.dataframe(preds.filter(items=['Close'], axis=0), hide_index=True)

        # Showing the chart
        st.plotly_chart(fig_model)