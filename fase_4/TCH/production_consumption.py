import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pycountry

class ProdConsPage():
    def __init__(self, brent_df: pd.DataFrame, lang):
        df = pd.read_csv('https://raw.githubusercontent.com/GusdPaula/postgraduation_fiap/refs/heads/main/fase_4/TCH/World%20Energy%20Consumption.csv', sep=",", na_values="", nrows=10)

        df['extra 1'] = ''
        df['extra 2'] = ''

        columns = df.columns

        df = pd.read_csv('https://raw.githubusercontent.com/GusdPaula/postgraduation_fiap/refs/heads/main/fase_4/TCH/World%20Energy%20Consumption.csv', sep=",", na_values="", header=None, names=columns, skiprows=1)

        raw_df = df.copy()
        
        df = df[['oil_consumption', 'oil_production', 'oil_energy_per_capita', 'country', 'year']]
        df = df[(pd.isna(df.oil_consumption) == False) | (pd.isna(df.oil_production) == False)| (pd.isna(df.oil_energy_per_capita) == False)]
        df = df[df.country == "World"]
        del df['country']
        df.index = pd.to_datetime(df.year, format='%Y')
        del df['year']

        def custom_legend_name(fig, new_names):
            for i, new_name in enumerate(new_names):
                fig.data[i].name = new_name

        if lang == 'EN':
            st.write('## Oil Production and Consumption')

            st.write('Looking at the charts it is possible to notice that production and consumption were side by side through the years.')
            st.write('Also, we can notice that neither the comsumption or the production seems to affect directly the brent price. Except in extreme situations, like in 2019 and 2020 with Covid-19, where all the world production decreased and people were in quarantine.')
        
        else:
            st.write('## Produção e Consumo de Petróleo')

            st.write('Observando os gráficos, é possível perceber que a produção e o consumo estiveram lado a lado ao longo dos anos.')
            st.write('Além disso, podemos perceber que nem o consumo nem a produção parecem afetar diretamente o preço do brent. Exceto em situações extremas, como em 2019 e 2020 com o Covid-19, onde toda a produção glocal caiu e as pessaos estavam em quarentena.')


        col_cons_prod, col_sd = st.columns(2)

        cons_prod_fig = go.Figure(data=[go.Bar(x=df.index, y=df['oil_production']),
                                  go.Line(x=df.index, y=df['oil_consumption'], line=dict(color='orange', width=3))])
        
        cons_prod_fig.update_layout(title='Oil Production and Consumption in terawatt-hours through the years' if lang == "EN" else 'Produção e Consumo de Óleo em terawatt-hours ao passar dos anos',
                                    legend=dict(
                                            orientation='h',  # Set the legend to be horizontal
                                            x=0.5,  # Position the legend in the center horizontally
                                            xanchor='center',  # Anchor the legend to the center horizontally
                                            y=1.,  # Position the legend slightly above the plot
                                            yanchor='bottom'  # Anchor the legend to the bottom (of the position set by y)
                                        ))
        custom_legend_name(cons_prod_fig, ['Oil Production' if lang == "EN" else 'Produção de Óleo', 'Oil Consumption' if lang == "EN" else 'Consumo de Óleo'])

        with col_cons_prod:
            st.plotly_chart(cons_prod_fig)

        brent_df = brent_df.groupby('year').agg({
                'Open': 'first',    # First open price of the year
                'Close': 'last',    # Last close price of the year
                'High': 'max',      # Maximum high price of the year
                'Low': 'min',       # Minimum low price of the year
                'Volume': 'sum'     # Total volume traded in the year
            }).reset_index()

        brent_df['Date'] = pd.to_datetime(brent_df['year'], format='%Y')

        brent_df.index = brent_df.Date
        brent_df = brent_df.Close
        df = pd.merge(df, brent_df, how='left',left_index=True, right_index=True)
        normalized_df=(df-df.mean())/df.std()
        normalized_df.rename(columns={'Close': 'Price'}, inplace=True)
        filtered_df = normalized_df.query('year >= 2007')

        labels={'oil_consumption': "Oil Consumption",
                'oil_production': "oil Prodcution",
                'oil_energy_per_capita': 'Oil Consumption Per Capita',
                'Price': 'Price'}
        
        fig_price_cons_prod = go.Figure(data=[go.Line(x=filtered_df.index, y=filtered_df['oil_production'], line=dict(color='blue', width=3)),
                                  go.Line(x=filtered_df.index, y=filtered_df['oil_consumption'], line=dict(color='lightblue', width=3)),
                                  go.Line(x=filtered_df.index, y=filtered_df['oil_energy_per_capita'], line=dict(color='orange', width=3)),
                                  go.Line(x=filtered_df.index, y=filtered_df['Price'], line=dict(color='brown', width=3))])

        fig_price_cons_prod.update_layout(title='Oil Production, Consumption and Price Standard Deviation' if lang == "EN" else 'Desvio Padrão da Produção, Consumo e Preço do Oléo',
                                          legend=dict(
                                            orientation='h',  # Set the legend to be horizontal
                                            x=0.5,  # Position the legend in the center horizontally
                                            xanchor='center',  # Anchor the legend to the center horizontally
                                            y=1.,  # Position the legend slightly above the plot
                                            yanchor='bottom'  # Anchor the legend to the bottom (of the position set by y)
                                        ))
        
        custom_legend_name(fig_price_cons_prod,
                           ['Oil Production' if lang == "EN" else 'Produção de Óleo',
                            'Oil Consumption' if lang == "EN" else 'Consumo de Óleo',
                            'Oil Consumption Per Capita' if lang == "EN" else 'Consumo de Óleo Per Capita',
                            'Brent Price' if lang == "EN" else 'Preço do Óleo'])
        
        fig_price_cons_prod.add_vrect(x0='2019', x1='2020', line_width=0, fillcolor="red", opacity=0.2)

        with col_sd:
            st.plotly_chart(fig_price_cons_prod)
