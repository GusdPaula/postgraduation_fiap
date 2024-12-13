# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd
import plotly.express as px

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

table_saude = "pnad_covid19_202011_saude_BR_GR_UF"
table_trabalho = "pnad_covid19_202011_trabalho_BR_GR_UF"
table_escola_item = "pnad_covid19_202011_escola_emprestimos_itens_de_limpeza_BR_GR_UF"

table_saude_uf = "saude_uf"
table_trabalho_uf = "trabalho_uf"
table_escola_item_uf = "escola_item_uf"

columns = ['Indicador', 'Novembro', 'Outubro', 'Setembro']

@st.cache_data(ttl=600)
def get_df(filter_string, group_col, table, columns):
    query = f"SELECT * FROM `tech-chlg.pnad_covid.{table}`"
    query_job = client.query(query)
    rows_raw = query_job.result()
    rows = [dict(row) for row in rows_raw]
    df = pd.DataFrame(rows)
    df = df[columns]

    # TODO: existe uma linha de total
    if filter_string == "ALL":
        df = df.groupby(group_col).sum()
    else:
        df = df[df[group_col].str.contains(filter_string)]
        df = df.groupby(group_col).sum()

    return df


def filter_df(df, filter_string, column_name, not_contain=False):

    if not_contain:
        df = df[~df[column_name].str.contains(filter_string)]

    else:
        df = df[df[column_name].str.contains(filter_string)]

    return df


#df = get_df('mil pessoas', 'Indicador', table_saude, columns)

st.title("Análise COVID-19")

st.write("A presente apresentação foi construída com o propósito de analisar os principais dados referentes ao covid 19 nos meses de Novembro, Outubro e Setembro de 2020.")

st.write("A análise foi dividida em partes. Entre elas: a alocação dos dados em nuvem, a extração dos dados, a criação do dashboard/relatório e, por fim, a realização das análises dos dados.")

st.image(r'C:\Users\Gustavo_SantosdePaul\OneDrive - Dell Technologies\Documents\pos\fase_3\flow.png')

st.write("### 1 - Download dos dados")

st.write('Primeiramente, os dados foram extraídos em formato .xlsx do site do PNAD (https://covid19.ibge.gov.br/pnad-covid/).')
st.write('Os últimos arquivos referentes a saúde, trabalho e excola/items de limpeza foram baixados do ano 2020.')

st.write("### 2 - Alocação dos dados")

st.write("Os dados foram carregados no Google Colab onde, utilizando do Python e da sua biblioteca Pandas, manipulções foram feitas para que se enquadrasse no BiggQuery.")
st.write("Uma vez feita a manipulação, os dados foram carregados no BigQuery utilizando a biblioteca pandas_gbq e do Google could.")
# TODO: adicionar link do rep
st.write('O código pode ser checado no link: adiconar link')

st.write("### 3 - Extração dos dados")

st.write("Uma vez na nuvem, os dados foram extraídos utilizando a biblioteca do Google Cloud no python e então manipulados com pyspark.")
# TODO: adicionar outras formas dos demais.
st.write("### 4 - Criação do Dashboard/relatório")

st.write('O presentente relatório também foi contruído por meio do Python, mais especificamente de sua biblioteca streamlit.')
# TODO: adicionar outras formas dos demais.
st.write("### 5 - Análise")

st.write("#### Características clínicas dos sintomas:")
st.write("Os principais sintomas apresentados são perda de cheiro ou sabor ou tosse, febre e dificuldade para respirar ou febre, tosse e dor no peito")


df_sintomas = get_df('Pessoas que apresentaram', 'Indicador', table_saude, columns)
df_sintomas.reset_index(inplace=True)
df_sintomas = filter_df(df_sintomas, 'mil pessoas', 'Indicador')
df_sintomas = filter_df(df_sintomas, 'conjugados', 'Indicador', not_contain=True)
df_sintomas = filter_df(df_sintomas, 'algum', 'Indicador', not_contain=True)
df_sintomas.index = df_sintomas['Indicador']
del df_sintomas['Indicador']

df_sintomas = df_sintomas[['Setembro', 'Outubro', 'Novembro']]

df_sintomas_transposed = df_sintomas.transpose()
df_sintomas_transposed.rename(columns={'Pessoas que apresentaram o sintoma de perda de cheiro ou de sabor (mil pessoas)': 'Perda de cheiro ou de sabor',
                                       'Pessoas que apresentaram os sintomas de tosse, febre e dificuldade para respirar (mil pessoas) ': 'Tosse, febre e dificuldade para respirar',
                                       'Pessoas que apresentaram os sintomas de tosse, febre e dor no peito (mil pessoas)': 'Tosse, febre e dor no peito'},
                                       inplace=True)


chart_df_sintomas = px.line(df_sintomas_transposed, labels={
                     "value": "Número",
                     "index": "Mês",
                     "Indicador": "Sintomas"
                 },
                title="Sintomas apresentados (mil pessoas)")

st.plotly_chart(chart_df_sintomas)
st.write('Os principais sintomos foram perda de cheiro ou de sabor. E não houve grande variação nos últimos três meses.')

st.write("#### Situação dos testes:")
df_testes = get_df('mil pessoas', 'Indicador', table_saude, columns)
df_testes.reset_index(inplace=True)
df_testes = filter_df(df_testes, 'Pessoas que fizeram algum teste para saber se estavam infectadas pelo Coronavírus', 'Indicador')
df_testes.index = df_testes['Indicador']
del df_testes['Indicador']

df_testes = df_testes[['Setembro', 'Outubro', 'Novembro']]

df_testes = df_testes.transpose()

df_testes.rename(columns={'Pessoas que fizeram algum teste para saber se estavam infectadas pelo Coronavírus (mil pessoas)': 'Testes realizados',
                                       'Pessoas que fizeram algum teste para saber se estavam infectadas pelo Coronavírus e testaram positivo (mil pessoas) ': 'Testes positivos'},
                                       inplace=True)

chart_df_testes = px.bar(df_testes, labels={
                     "value": "Número",
                     "index": "Mês",
                 },
                title="Testes realizados x testes positivos")

df_tipo_testes = get_df('Pessoas que fizeram o exame', 'Indicador', table_saude, columns)
df_tipo_testes.reset_index(inplace=True)
df_tipo_testes = filter_df(df_tipo_testes, '(mil pessoas)', 'Indicador')
df_tipo_testes.index = df_tipo_testes['Indicador']
del df_tipo_testes['Indicador']

df_swab = get_df('SWAB', 'Indicador', table_saude, columns)
df_swab.reset_index(inplace=True)
df_swab = filter_df(df_swab, '(mil pessoas)', 'Indicador')
df_swab.index = df_swab['Indicador']
del df_swab['Indicador']

df_tipo_testes = pd.concat([df_tipo_testes, df_swab])

df_tipo_testes = df_tipo_testes[['Setembro', 'Outubro', 'Novembro']]

df_tipo_testes = df_tipo_testes.transpose()

df_tipo_testes.rename(columns={'Pessoas que fizeram o exame de sangue através da veia do braço (mil pessoas) ': 'Veia do braço',
                                       'Pessoas que fizeram o exame de sangue com furo no dedo (mil pessoas)': 'Furo no dedo',
                                       'Pessoas que fizeram o teste SWAB (mil pessoas)': 'SWAB'},
                                       inplace=True)

chart_df_tipo_testes = px.bar(df_tipo_testes, labels={
                     "value": "Número",
                     "index": "Mês",
                 },
                title="Tipo de testes realizados",
                barmode="group")

st.plotly_chart(chart_df_tipo_testes)
st.write('Os exames de furo do dedo e na veia são exames de sangue que verificam a resposta imunológica do indivíduo em relação ao vírus, a indicação é para a fase descendente da infecção. Os exames são feitos por meio de amostra de sangue venoso e têm melhor resposta se aplicados de 7 a 10 dias após o surgimento dos sintomas. Eles foram os menos utilizados nos últimos três meses.')
st.write('O teste SWAB (do cotonete), dito o mais eficaz segundo especialistas é capaz de detectar a presença do vírus a partir de 1 dias após a contaminação e até 12 dias. É realizado utilizando material da naso-orofaringe (nariz ou boca), coletado com um swab, instrumento similar com haste flexível de algodão. Foi o mais realizados no último mês.')

st.plotly_chart(chart_df_testes)

st.write('A proporção de testes positivos e realizados se demonstrou bem baixa, porém com crescimento nos últimos três meses.')


st.write("#### Situação dos hospitais:")
df_internadas = get_df('internadas', 'Indicador', table_saude, columns)
df_internadas.reset_index(inplace=True)
df_internadas = filter_df(df_internadas, '(mil pessoas)', 'Indicador')
df_internadas.index = df_internadas['Indicador']
del df_internadas['Indicador']
st.dataframe(df_internadas)

# TODO: como conseguir o número dos leitos?

# df_sintomas_uf = get_df('mil pessoas', 'Indicador', table_saude_uf, columns)
# st.dataframe(df_sintomas_uf)

# st.write("#### Características da população")
# df_escola_item = get_df('mil pessoas', 'Indicador', table_escola_item, columns)
# st.dataframe(df_escola_item)

# df_escola_item_uf = get_df('mil pessoas', 'Indicador', table_escola_item_uf, columns)
# st.dataframe(df_escola_item_uf)

# st.write("#### Características econômicas da sociedade")
# df_trabalho = get_df('mil pessoas', 'Indicador', table_trabalho, columns)
# st.dataframe(df_trabalho)

# df_trabalho_uf = get_df('mil pessoas', 'Indicador', table_trabalho_uf, columns)
# st.dataframe(df_trabalho_uf)


###########################################

st.write("#### Características econômicas da sociedade:")

df_trabalho = get_df('mil pessoas', 'Indicador', table_trabalho, columns)
df_trabalho_ocupadas = df_trabalho.copy()
df_trabalho_ocupadas = df_trabalho_ocupadas.reset_index()
df_trabalho_ocupadas = df_trabalho_ocupadas[df_trabalho_ocupadas['Indicador'] == 'Pessoas ocupadas (mil pessoas)']
df_trabalho_ocupadas.index = df_trabalho_ocupadas['Indicador']
del df_trabalho_ocupadas['Indicador']

df_trabalho_desocupadas = df_trabalho.copy()
df_trabalho_desocupadas = df_trabalho_desocupadas.reset_index()
df_trabalho_desocupadas = df_trabalho_desocupadas[df_trabalho_desocupadas['Indicador'] =='Pessoas desocupadas (mil pessoas)']
df_trabalho_desocupadas.index = df_trabalho_desocupadas['Indicador']
del df_trabalho_desocupadas['Indicador']

df_ocp_desocup = pd.concat([df_trabalho_ocupadas, df_trabalho_desocupadas])
df_ocp_desocup = df_ocp_desocup[['Setembro', 'Outubro', 'Novembro']]

df_ocp_desocup = df_ocp_desocup.transpose()

chart_df_sintomas = px.line(df_ocp_desocup, labels={
                     "value": "Número",
                     "index": "Mês",
                     "Indicador": "Situação"
                 },
                title="Pessoas ocupadas x Pessoas desocupadas")

st.plotly_chart(chart_df_sintomas)

st.dataframe(df_ocp_desocup)

# TODO: Gráfico diminuição de renda

st.write("#### Situação Macroeconômica:")

# TODO: Dólar, Bolsa e dívida pública



st.write("### 6 - Conclusão")
st.write("#### Quais ações tomar em caso de nova crise?")
