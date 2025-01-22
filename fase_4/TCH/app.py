import streamlit as st
import warnings
from pandas.errors import SettingWithCopyWarning
from home import HomePage
from model import ModelPage
from history import HistoryPage
from forecast_class import Forecast
from info import InfoPage
from prediciton import PredPage
from production_consumption import ProdConsPage
import time

class RenderPages():
    def __init__(self):
        
        self.tab_value = "Info"

        st.set_page_config(
            page_title="TCH 4",
            layout="wide"
        )
        warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
        warnings.simplefilter(action="ignore", category=FutureWarning)
        warnings.simplefilter(action="ignore", category=UserWarning)
        warnings.simplefilter(action="ignore")


        @st.cache_data()
        def create_model():
            brent = Forecast('BZ=F')
            brent.split_train_test()
            brent.train_xgb()

            return brent

        self.brent = create_model()


        self.sidebar_left = st.sidebar

        self.lang = self.sidebar_left.radio("Language:", ["EN", "PT"])

    def loading_page(self):
        # Display a loading spinner with a message
        text = 'Please wait... Loading the content' if self.lang == 'EN' else 'Espere... carregando conteúdo'
        with st.spinner('Please wait... Loading the content'):
            time.sleep(1)  # Simulate a long loading process


    def get_page(self):

        if self.lang == "EN":
            self.pages_names = ["Info", "Home", "Model", "History", 'Production & Consumption', "Prediction"]
            
            if self.tab_value not in self.pages_names:
                dict_tabs = {"Informação": 'Info',
                        "Home": "Home",
                        "Modelo": "Model",
                        "História": "History",
                        "Predição": "Prediction",
                        "Produção e Consumo": "Production & Consumption"}
            
                self.tab_value = dict_tabs[self.tab_value]

            self.page_title = '# Brent Price Analysis'
            self.side_page = 'Pages:'
            
        else:
            self.pages_names = ["Informação", "Home", "Modelo", "História", "Produção e Consumo", "Predição"]
            
            if self.tab_value not in self.pages_names:
                dict_tabs = {'Info': "Informação",
                        "Home": "Home",
                        "Model": "Modelo",
                        "History": "História",
                        "Prediction": "Predição",
                        "Production & Consumption": "Produção e Consumo"}
            
                self.tab_value = dict_tabs[self.tab_value]

            self.page_title = '# Análise do Preço do Petróleo (BRENT)'
            self.side_page = 'Páginas:'

        
    def select_page(self):
        self.radio_tabs = self.sidebar_left.radio(self.side_page, self.pages_names, index=self.pages_names.index(self.tab_value))

        self.tab_value = self.radio_tabs

        self.loading_page()

    def go_to_page(self):
        st.write(self.page_title)

        if self.tab_value == 'Info' or self.tab_value == 'Informação':
            info_page = InfoPage(self.lang)

        if self.tab_value == 'Home':
            home_page = HomePage(self.brent.df, self.lang)

        if self.tab_value == 'Model' or self.tab_value == 'Modelo':
            ModelPage(self.brent.metrics_xgb, self.brent.xbg_train_df, self.brent.xgb_test_df, self.lang)

        if self.tab_value == 'History' or self.tab_value == 'História':
            HistoryPage(self.brent.df, self.lang)

        if self.tab_value == 'Prediction' or self.tab_value == 'Predição':
            PredPage(self.brent, self.lang)


        if self.tab_value == 'Production & Consumption' or self.tab_value == 'Produção e Consumo':
            ProdConsPage(self.brent.df, self.lang)


if __name__ == '__main__':
    render = RenderPages()
    render.get_page()
    render.select_page()
    render.go_to_page()