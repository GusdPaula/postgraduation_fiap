import streamlit as st
from forecast_class import Forecast
from datetime import datetime, timedelta
import plotly.graph_objects as go
import pandas as pd

class PredPage():
    def __init__(self, model: Forecast):
        model.predict_future_days()

        preds = model.seven_days_pred
        real_data = model.df_real

        def custom_legend_name(fig, new_names):
            for i, new_name in enumerate(new_names):
                fig.data[i].name = new_name

        
        @st.cache_data()        
        def get_date():
            start_date = pd.to_datetime(real_data.Date).min().timestamp()
            end_date = pd.to_datetime(preds.index).max().timestamp()

            start_date = datetime.fromtimestamp(start_date)
            end_date = datetime.fromtimestamp(end_date)

            return start_date, end_date

        start_date, end_date = get_date()

       
        selected_date_range = st.slider(
            "Select a date range",
            min_value=start_date,
            max_value=end_date,
            value=(end_date - + timedelta(weeks=20), end_date),
            step=timedelta(days=1),
        )
        start = datetime.date(selected_date_range[0])

        real_data = real_data.loc[start:]

        real_data = real_data[['Date', 'Close']]
        preds['Date'] = preds.index
        preds = preds[['Date', 'Close']]

        real_data = pd.concat([real_data, preds])

        fig_model = go.Figure(data=[go.Scatter(x=real_data.Date, y=real_data['Close'], line=dict(color='purple', width=3)),
                                    go.Scatter(x=preds.index, y=preds['Close'], line=dict(color='orange', width=3))])
        fig_model.update_layout(title='Brent Price Prediciton in USD')
        custom_legend_name(fig_model, ['Real Price', 'Prediction'])

        preds.index = preds.index.strftime('%Y-%m-%d')
        preds = preds.T
        st.dataframe(preds.filter(items=['Close'], axis=0))
        st.plotly_chart(fig_model)