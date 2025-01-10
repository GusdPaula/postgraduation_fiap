import streamlit as st
import pandas as pd
import joblib
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MinMaxScaler
import os
import __main__
from imblearn.over_sampling import SMOTE

# Idade
st.write("""### Idade""")
input_idade = float(st.slider('Selecione a sua idade', 18, 100))

# Gênero
st.write('### Gênero')
input_genero= st.selectbox('Qual o Gênero ?', ['Homem', 'Mulher'])

input_genero_dict = {'Homem': 1, 'Mulher':2}
input_genero = input_genero_dict.get(input_genero)

# Altura
st.write("""### Altura""")
input_altura = float(st.slider('Selecione a sua altura', 100, 250))

# Peso
st.write("""### Peso""")
input_peso = float(st.slider('Selecione seu peso', 40, 250))

# PressaoArterialSistolica
st.write("""### Pressâo Arterial Sistólica""")
input_PressaoArterialSistolica = float(st.slider('Selecione Pressâo Arterial Sistólica', -20000, 20000))

# PressaoArterialDiastolica
st.write("""### Pressâo Arterial Diastólica""")
input_PressaoArterialDiastolica = float(st.slider('Selecione Pressâo Arterial Diastólica', -20000, 20000))

# colesterol
st.write("""### Colesterol""")
input_colesterol = float(st.slider('Selecione seu colesterol', 1, 3))

# glicose
st.write("""### Glicose""")
input_glicose = float(st.slider('Selecione sua glicose', 1, 3))

# Fumante
st.write('### Fumante?')
input_fumante = st.radio('Você fuma?',['Sim','Não'], index=0)
input_sim_nao_dict = {'Sim': 1, 'Não':0}
input_fumante = input_sim_nao_dict.get(input_fumante)

# Alcool
st.write('### Alcool?')
input_alcool = st.radio('Você bebe?',['Sim','Não'], index=0)
input_alcool = input_sim_nao_dict.get(input_alcool)

#  AtivoFisicamente
st.write('### Ativo Fisicamente?')
input_AtivoFisicamente = st.radio('Se exercita?',['Sim','Não'], index=0)
input_AtivoFisicamente = input_sim_nao_dict.get(input_AtivoFisicamente)




class MinMax(BaseEstimator,TransformerMixin):
    def __init__(self,min_max_scaler = ['Idade', 'Altura', 'Peso', 'PressaoArterialSistolica', 'PressaoArterialDiastolica']):
        self.min_max_scaler = min_max_scaler
    def fit(self,df):
        return self
    def transform(self,df):
        if (set(self.min_max_scaler).issubset(df.columns)):
            min_max_enc = MinMaxScaler()
            df[self.min_max_scaler] = min_max_enc.fit_transform(df[self.min_max_scaler])
            return df
        else:
            print('Uma ou mais features não estão no DataFrame')
            return df

class Oversample(BaseEstimator,TransformerMixin):
    def __init__(self):
        pass
    def fit(self,df):
        return self
    def transform(self,df):
        
        return df


main_path = __main__.__file__

#Predições 
if st.button('Enviar'):
    # Lista de todas as variáveis: 
    novo_cliente = [
                        input_idade,
                        input_genero,
                        input_altura,
                        input_peso,
                        input_PressaoArterialSistolica,
                        input_PressaoArterialDiastolica,
                        input_colesterol,	
                        input_glicose,
                        input_fumante,
                        input_alcool,
                        input_AtivoFisicamente,
                        0
                        ]


    cols_novo_cliente = ['Idade',
                        'Genero',
                        'Altura',
                        'Peso',
                        'PressaoArterialSistolica',
                        'PressaoArterialDiastolica',
                        'Colesterol',
                        'Glicose',
                        'Fumante',
                        'UsaAlcool',
                        'AtivoFisicamente',
                        'DoencaVascular'
                        ]

    

    #Criando novo cliente
    cliente_predict_df = pd.DataFrame([novo_cliente], columns=cols_novo_cliente)

    pipeline_path = main_path.replace('desafio.py', 'pipeline.joblib')
    pipeline = joblib.load(pipeline_path)

    test_df_path = main_path.replace('desafio.py', 'test.csv')
    test_df = pd.read_csv(test_df_path, sep=';')
    df_pipeline = pd.concat([test_df, cliente_predict_df])

    df_pipeline = pipeline.fit_transform(df_pipeline)

    del df_pipeline['DoencaVascular']

    model_path = main_path.replace('desafio.py', 'xgb.joblib')
    model = joblib.load(model_path)

    final_pred = model.predict(df_pipeline)

    if final_pred[-1] == 0:
        st.success('### Baixa probabilidade de ter doença!')
        st.balloons()
    else:
        st.error('### Alta probabilidade de ter doença!')