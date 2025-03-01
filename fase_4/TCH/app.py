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
from maps import MapsPage

class RenderPages():
    '''
    
        App Page that brings all the other pages and run the model
    
    '''
    def __init__(self):
        
        # Setting initial tab
        self.tab_value = "Info"

        # Setting page configs
        st.set_page_config(
            page_title="TCH 4",
            layout="wide"
        )

        # Ignoring warings
        warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
        warnings.simplefilter(action="ignore", category=FutureWarning)
        warnings.simplefilter(action="ignore", category=UserWarning)
        warnings.simplefilter(action="ignore")

        # Running the model
        @st.cache_data()
        def create_model():
            brent = Forecast('BZ=F')
            brent.split_train_test()
            brent.train_xgb()

            return brent

        self.brent = create_model()

        # Adding widgets
        self.sidebar_left = st.sidebar
        self.lang = self.sidebar_left.radio("Language:", ["EN", "PT"])

    def loading_page(self):
        # Display a loading spinner with a message
        text = 'Please wait... Loading the content' if self.lang == 'EN' else 'Espere... carregando conteúdo'
        with st.spinner(text):
            time.sleep(1)  

    def get_page(self):
        '''
            This will get the page when user click on the language radio button
        
        '''

        # Pages in language is english
        if self.lang == "EN":
            self.pages_names = ["Info", "Home", "Model", "History", 'Production & Consumption', 'Maps', "Prediction"]
            
            if self.tab_value not in self.pages_names:
                dict_tabs = {"Informação": 'Info',
                        "Home": "Home",
                        "Modelo": "Model",
                        "História": "History",
                        "Predição": "Prediction",
                        "Produção e Consumo": "Production & Consumption",
                        "Mapas": " Maps"}
            
                self.tab_value = dict_tabs[self.tab_value]

            self.page_title = '# Brent Price Analysis'
            self.side_page = 'Pages:'
        
        # Page if language is PT
        else:
            self.pages_names = ["Informação", "Home", "Modelo", "História", "Produção e Consumo", "Mapas", "Predição"]
            
            if self.tab_value not in self.pages_names:
                dict_tabs = {'Info': "Informação",
                        "Home": "Home",
                        "Model": "Modelo",
                        "History": "História",
                        "Prediction": "Predição",
                        "Production & Consumption": "Produção e Consumo",
                        "Maps": "Mapdas"}
            
                self.tab_value = dict_tabs[self.tab_value]

            self.page_title = '# Análise do Preço do Petróleo (BRENT)'
            self.side_page = 'Páginas:'

        
    def select_page(self):
        '''
            This will select the page when user click on the page radio button


        '''

        self.radio_tabs = self.sidebar_left.radio(self.side_page, self.pages_names, index=self.pages_names.index(self.tab_value))

        self.tab_value = self.radio_tabs

        self.loading_page()

    def go_to_page(self):
        '''
            This will load the selected page
        
        '''
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
        
        if self.tab_value == 'Maps' or self.tab_value == 'Mapas':
            MapsPage(self.lang)


if __name__ == '__main__':
    render = RenderPages()
    render.get_page()
    render.select_page()
    render.go_to_page()