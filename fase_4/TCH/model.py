import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

class ModelPage():
    def __init__(self, metrics: pd.DataFrame, train_df: pd.DataFrame, test_df: pd.DataFrame, lang):
        self.metrics = metrics
        self.train_df = train_df
        self.test_df = test_df

       

        st.write("#### Model Metrics" if lang == 'EN' else "#### Métricas do Modelo")
        st.dataframe(self.metrics, hide_index=True)

        def custom_legend_name(fig, new_names):
            for i, new_name in enumerate(new_names):
                fig.data[i].name = new_name

        
        @st.cache_data()        
        def get_date():
            start_date = pd.to_datetime(train_df.Date).min().timestamp()
            end_date = pd.to_datetime(train_df.Date).max().timestamp()

            start_date = datetime.fromtimestamp(start_date)
            end_date = datetime.fromtimestamp(end_date)

            return start_date, end_date

        start_date, end_date = get_date()

       
        selected_date_range = st.slider(
            "Select a date range" if lang == "EN" else 'Selecione um espaço de tempo',
            min_value=start_date,
            max_value=end_date,
            value=(end_date - + timedelta(weeks=20), end_date),
            step=timedelta(days=1),
        )
        start = datetime.date(selected_date_range[0])
        end = datetime.date(selected_date_range[1])

        train_df = train_df.loc[start:end]

        train_df = train_df[['Date', 'Close']]
        test_df = test_df[['Date', 'Predictions']]
        test_df.rename(columns={'Predictions': 'Close'}, inplace=True)

        train_df = pd.concat([train_df, test_df])

        fig_model = go.Figure(data=[go.Scatter(x=train_df.Date, y=train_df['Close'], line=dict(color='purple', width=3)),
                                    go.Scatter(x=test_df.Date, y=test_df['Close'], line=dict(color='orange', width=3))])
        fig_model.update_layout(title='Brent Price Over Time in USD' if lang == 'EN' else 'Preço do Petróleo no tempo em Dólar')
        custom_legend_name(fig_model, ['Train' if lang == 'EN' else 'Treino', 'Test' if lang == 'EN' else 'Teste'])

        st.plotly_chart(fig_model)