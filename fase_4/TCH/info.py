import streamlit as st

class InfoPage():
    def __init__(self, lang):

        if lang == "EN":
            st.write('## Info')

            st.write("This dashboard was built due to FIAP's fourth Tech Challenge on Data Alytics specialization.")
            
            st.write('### Data, Model and Exploratoy Data Analysis')
            st.write('You can check the exploratory data analysis on the link: https://github.com/GusdPaula/postgraduation_fiap/blob/bef985e7ca1bab681fa1ff631d188fdcf646340f/fase_4/TCH/brent.ipynb')
            st.write('The data was pull from Yahoo Finance API.')
            st.write('Some models were tested, but XGBoost was the best one and the one that we are using on the dashboard.')

            st.write('### Pages')

            st.write('##### Home Page')
            st.write('In the Home page you can see the price and the volume over time and the options to change data ranges, data periods and to add Moving Averages (MA) or to see the Standard Deviation.')
            st.write("The moving averages are the price's average for a period (20 days or 50 days in this case) and the price tends to be close to these lines.")
            st.write("The standard deviation shows the movement in percentage for the price and volume")

            st.write('##### Model Page')
            st.write('On the Model page you can see the model metrics results and the chart with the train and test data.')
            st.write(' - Mean Squared Error (MSE): MSE is a cost function that calculates the average of the squares of the errors—i.e., the average squared difference between the estimated values and the actual value.')
            st.write(' - Mean Absolute Percentage Error (MAPE): MAPE expresses the error as a percentage of the actual values, providing an easy-to-understand metric.')
            st.write(' - Mean Absolute Error (MAE): MAE measures the average magnitude of the errors in a set of predictions, without considering their direction. It is the average absolute difference between the predicted and actual values. Unlike MSE, it doesn’t square the errors, which means it doesn’t punish larger errors as harshly.')

            st.write('##### History Page')
            st.write('On the History page you will be able to see the Brent Price key crises or the rallies. The crises will be highlighted in the price chart as red and rallies as green.')
            st.write('It is important to mention that the price usually increase or decrease because of politics and agreements that the Countries inside OPEP do.')

            st.write('##### Production & Consumption Page')
            st.write('On the Production & Consumption page you can find the production and consumption through the years for Oil/Brent and also the standard deviation with the price.')
            st.write('The data was pull from the link: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption')
            st.write('The exploratory analysis on this data can be found on the link: https://github.com/GusdPaula/postgraduation_fiap/blob/37856517ad72bcf1612756a317111cd8ea117cb6/fase_4/TCH/energy_consumption.ipynb')

            st.write('##### Prediction Page')
            st.write('On the Prediction page you will see the price prediction for the next 7 days.')
        
        else:
            st.write('## Informações')

            st.write("Este dashboard foi construído devido ao quarto Tech Challenge da FIAP na especialização de Análise de Dados.")

            st.write('### Dados, Modelo e Análise Exploratória de Dados')
            st.write('Você pode verificar a análise exploratória de dados no link: https://github.com/GusdPaula/postgraduation_fiap/blob/bef985e7ca1bab681fa1ff631d188fdcf646340f/fase_4/TCH/brent.ipynb')
            st.write('Os dados foram obtidos da API do Yahoo Finance.')
            st.write('Alguns modelos foram testados, mas o XGBoost foi o melhor e é o que estamos utilizando no dashboard.')

            st.write('### Páginas')

            st.write('##### Página Home')
            st.write('Na página Home, você pode ver o preço e o volume ao longo do tempo, além das opções para alterar os intervalos de dados, períodos de dados e para adicionar Médias Móveis (MA) ou ver o Desvio Padrão.')
            st.write("As médias móveis são a média do preço para um período (20 dias ou 50 dias, neste caso), e o preço tende a ficar próximo dessas linhas.")
            st.write("O desvio padrão mostra o movimento em percentual para o preço e volume.")

            st.write('##### Página de Modelo')
            st.write('Na página de Modelo, você pode ver os resultados das métricas do modelo e o gráfico com os dados de treinamento e teste.')
            st.write(' - Erro Quadrático Médio (MSE): O MSE é uma função de custo que calcula a média dos quadrados dos erros, ou seja, a diferença quadrada média entre os valores estimados e os valores reais.')
            st.write(' - Erro Percentual Absoluto Médio (MAPE): O MAPE expressa o erro como uma porcentagem dos valores reais, fornecendo uma métrica fácil de entender.')
            st.write(' - Erro Absoluto Médio (MAE): O MAE mede a magnitude média dos erros em um conjunto de previsões, sem considerar sua direção. É a média da diferença absoluta entre os valores previstos e os valores reais. Ao contrário do MSE, ele não eleva os erros ao quadrado, o que significa que não pune os erros maiores com tanta severidade.')
            
            st.write('##### Página de História')
            st.write('Na página de História, você poderá ver as principais crises ou rallys do preço do Brent. As crises serão destacadas no gráfico de preços em vermelho e os rallys em verde.')
            st.write('É importante mencionar que os preços geralmente sobe ou desce por conta de atividades políticas e acordos entre os países da OPEP.')

            st.write('##### Página de Produção & Consumo')
            st.write('Na página de Produção & Consumo, você pode encontrar a produção e o consumo ao longo dos anos para o Petróleo/Brent, além da desvio padrão com o preço.')
            st.write('Os dados foram obtidos no link: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption')
            st.write('A análise exploratória desses dados pode ser encontrada no link: https://github.com/GusdPaula/postgraduation_fiap/blob/37856517ad72bcf1612756a317111cd8ea117cb6/fase_4/TCH/energy_consumption.ipynb')


            st.write('##### Página de Predição')
            st.write('Na página de Predição, você verá a previsão de preço para os próximos 7 dias.')
