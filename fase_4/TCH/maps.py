import pandas as pd
import streamlit as st
import plotly.express as px
import pycountry

class MapsPage():
    def __init__(self, lang):

        if lang == "EN":
            st.write('## Production and consumption through the years in the map')
            st.write('We can notice that the countries that most product oil are not the ones that most consume, except the US.')
            st.write('This forces the price control in the hands and politics on the producer countries.')
        
        else:
            st.write('## Produção e consumo pelos anos no mapa')
            st.write('Podemos perceber que os países que mais produzem petróleo não são os que mais consomem, exceto os EUA.')
            st.write('Isso força o controle do preço nas mãos e nas políticas dos países produtores.')


        df = pd.read_csv('https://raw.githubusercontent.com/GusdPaula/postgraduation_fiap/refs/heads/main/fase_4/TCH/World%20Energy%20Consumption.csv', sep=",", na_values="", nrows=10)

        df['extra 1'] = ''
        df['extra 2'] = ''

        columns = df.columns

        df = pd.read_csv('https://raw.githubusercontent.com/GusdPaula/postgraduation_fiap/refs/heads/main/fase_4/TCH/World%20Energy%20Consumption.csv', sep=",", na_values="", header=None, names=columns, skiprows=1)

        raw_df = df.copy()
        
        df = df[['oil_consumption', 'oil_production', 'country', 'year']]
        df = df[(pd.isna(df.oil_consumption) == False) | (pd.isna(df.oil_production) == False)]
        #df = df[(pd.isna(df.oil_consumption) > 0) | (pd.isna(df.oil_production) > 0)]
        df.index = pd.to_datetime(df.year, format='%Y')

        @st.cache_data()
        def get_date():
            # Convert 'Date' to datetime and extract the min and max years
            df['year'] = pd.to_datetime(df['year'], errors='coerce')  # Ensure it's datetime format
            min_year = df['year'].dt.year.min()  # Extract year and get the min
            max_year = df['year'].dt.year.max()  # Extract year and get the max

            return min_year, max_year

        # Get the min and max years for the slider
        min_year, max_year = get_date()

        # Slider to select the year range (ensure years are integers)
        selected_year_range = st.slider(
            "Select a date range" if lang == "EN" else 'Selecione um espaço de tempo',
            min_value=min_year,  # Ensure it's an integer (year)
            max_value=max_year,  # Ensure it's an integer (year)
            value=(min_year, max_year),  # Default value set to the full range
            step=1,  # Step size of 1 year
        )

        df.year = df.year.astype(int)
        df = df[(df.year >= selected_year_range[0]) & (df.year <= selected_year_range[1])]
        df.reset_index(inplace=True, drop=True)
        df.fillna(0, inplace=True)
        
        df.sort_values('year', inplace=True)



        # Function to get ISO alpha-3 code for a given country name
        def get_iso_alpha_3(country_name):
            try:
                return pycountry.countries.get(name=country_name).alpha_3
            except AttributeError:
                return None  # Return None if country is not found

        # Apply the function to the 'Country' column to get ISO alpha-3 codes
        df['ISO_Alpha_3'] = df['country'].apply(get_iso_alpha_3)
        df = df.groupby(['country', 'ISO_Alpha_3'])[['oil_consumption', 'oil_production']].sum()
        df = df.reset_index()
        
        prod_col, cons_col = st.columns(2)

        with prod_col:
            df_prod = df.rename(columns={"oil_production": 'Scale (in terawatt-hours)' if lang == 'EN' else 'Escala (em terawatt-hora)'})
            fig_map_oil_prod = px.scatter_geo(df_prod, locations="ISO_Alpha_3", color="Scale (in terawatt-hours)" if lang == 'EN' else 'Escala (em terawatt-hora)',
                        hover_name="country", size="Scale (in terawatt-hours)" if lang == 'EN' else 'Escala (em terawatt-hora)', color_continuous_scale="Viridis", title='Oil Production' if lang == 'EN' else 'Produção de Óleo')
            
            # Update layout to make the background blank and change line color to white
            fig_map_oil_prod.update_layout(
                geo=dict(
                    landcolor='lightgray',  # Color the land to light gray
                    showland=True,  # Show land
                    lakecolor='white',  # Set the color of lakes to white
                    showcoastlines=True,  # Show coastlines
                    coastlinecolor='white',  # Set the coastline color to white
                    showframe=False,  # Hide the frame around the map
                    showocean=True,  # Show ocean areas
                    oceancolor='lightblue'  # Set the ocean color to light blue (not white)
                )
            )

            # Update traces to make the lines white (for borders around the countries)
            fig_map_oil_prod.update_traces(marker=dict(line=dict(width=1, color='white')))
            st.plotly_chart(fig_map_oil_prod)

        with cons_col:
            df_cons = df.rename(columns={"oil_consumption": 'Scale (in terawatt-hours)' if lang == 'EN' else 'Escala (em terawatt-hora)'})
            fig_map_oil_cons = px.scatter_geo(df_cons, locations="ISO_Alpha_3", color="Scale (in terawatt-hours)" if lang == 'EN' else 'Escala (em terawatt-hora)',
                        hover_name="country", size="Scale (in terawatt-hours)" if lang == 'EN' else 'Escala (em terawatt-hora)', color_continuous_scale="Jet", title='Oil Consumption' if lang == 'EN' else 'Consumo de Óleo')
            

            fig_map_oil_cons.update_layout(
                legend_title="Country Sizes",
                geo=dict(
                    landcolor='lightgray',  # Color the land to light gray
                    showland=True,  # Show land
                    lakecolor='white',  # Set the color of lakes to white
                    showcoastlines=True,  # Show coastlines
                    coastlinecolor='white',  # Set the coastline color to white
                    showframe=False,  # Hide the frame around the map
                    showocean=True,  # Show ocean areas
                    oceancolor='lightblue'  # Set the ocean color to light blue (not white)
                ),
            )

            # Update traces to make the lines white (for borders around the countries)
            fig_map_oil_cons.update_traces(marker=dict(line=dict(width=1, color='white')))
            
            st.plotly_chart(fig_map_oil_cons)


