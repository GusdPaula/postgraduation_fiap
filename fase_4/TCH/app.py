import streamlit as st
import warnings
from pandas.errors import SettingWithCopyWarning
from home import HomePage
from model import ModelPage
from history import HistoryPage
from forecast_class import Forecast
from info import InfoPage
from prediciton import PredPage

st.set_page_config(
    page_title="Brent Price Analysis",
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

brent = create_model()


if 'tab_value' not in st.session_state:
    st.session_state.tab_value = "Home"


sidebar_left = st.sidebar

lang = sidebar_left.radio("Language:", ["EN", "PT"])

if lang == "EN":
    info_page, home_page, model_page, history_page, prediction_page = ["Info", "Home", "Model", "History", "Prediction"]

    if st.session_state.tab_value not in ["Info", "Home", "Model", "History", "Prediction"]:
        dict_tabs = {"Informação": 'Info',
                 "Home": "Home",
                 "Modelo": "Model",
                 "História": "History",
                 "Predição": "Prediction"}
    
        st.session_state.tab_value = dict_tabs[st.session_state.tab_value]

    page_title = '# Brent Price Analysis'
    side_page = 'Pages:'
    radio_tabs = sidebar_left.radio(side_page, [info_page, home_page, model_page, history_page, prediction_page], index=["Info", "Home", "Model", "History", "Prediction"].index(st.session_state.tab_value))

else:
    info_page, home_page, model_page, history_page, prediction_page = ["Informação", "Home", "Modelo", "História", "Predição"]

    if st.session_state.tab_value not in ["Informação", "Home", "Modelo", "História", "Predição"]:
        dict_tabs = {'Info': "Informação",
                 "Home": "Home",
                 "Model": "Modelo",
                 "History": "História",
                 "Prediction": "Predição"}
    
        st.session_state.tab_value = dict_tabs[st.session_state.tab_value]

    page_title = '# Análise do Preço do Petróleo (BRENT)'
    side_page = 'Páginas:'
    radio_tabs = sidebar_left.radio(side_page, [info_page, home_page, model_page, history_page, prediction_page], index=["Informação", "Home", "Modelo", "História", "Predição"].index(st.session_state.tab_value))

st.session_state.tab_value = radio_tabs

st.write(page_title)

if st.session_state.tab_value == 'Info' or st.session_state.tab_value == 'Informação':
    home_page = InfoPage(lang)

if st.session_state.tab_value == 'Home':
    home_page = HomePage(brent.df, lang)

if st.session_state.tab_value == 'Model' or st.session_state.tab_value == 'Modelo':
    ModelPage(brent.metrics_xgb, brent.xbg_train_df, brent.xgb_test_df, lang)

if st.session_state.tab_value == 'History' or st.session_state.tab_value == 'História':
    HistoryPage(brent.df, lang)

if st.session_state.tab_value == 'Prediction' or st.session_state.tab_value == 'Predição':
    PredPage(brent, lang)

