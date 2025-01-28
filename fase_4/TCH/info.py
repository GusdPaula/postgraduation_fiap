import streamlit as st

class InfoPage():
    '''
        Info page that will show the text main informations about the app and analysis
    '''
    def __init__(self, lang):

        if lang == "EN":
            st.write('## Info')

            st.write("This dashboard was built due to FIAP's fourth Tech Challenge on Data Analytics specialization.")
            
            st.write('### Data, Model and Exploratory Data Analysis')
            st.write('You can check the exploratory data analysis on the link: https://github.com/GusdPaula/postgraduation_fiap/blob/bef985e7ca1bab681fa1ff631d188fdcf646340f/fase_4/TCH/brent.ipynb')
            st.write('The data was pulled from the Yahoo Finance API.')
            st.write('Some models were tested, but XGBoost was the best one and the one that we are using on the dashboard.')

            st.write('### Pages')

            st.write('##### Home Page')
            st.write('In the Home page, you can see the price and the volume over time and the options to change data ranges, data periods and to add Moving Averages (MA) or to see the Standard Deviation.')
            st.write("The moving averages are the price's average for a period (20 days or 50 days in this case) and the price tends to be close to these lines.")
            st.write("The standard deviation shows the movement in percentage for the price and volume.")

            st.write('##### Model Page')
            st.write('On the Model page, you can see the model metrics results and the chart with the train and test data.')
            st.write(' - **Mean Squared Error (MSE):** MSE is a cost function that calculates the average of the squares of the errors—i.e., the average squared difference between the estimated values and the actual value.')
            st.write(' - **Mean Absolute Percentage Error (MAPE):** MAPE expresses the error as a percentage of the actual values, providing an easy-to-understand metric.')
            st.write(' - **Mean Absolute Error (MAE):** MAE measures the average magnitude of the errors in a set of predictions, without considering their direction. It is the average absolute difference between the predicted and actual values. Unlike MSE, it doesn’t square the errors, which means it doesn’t punish larger errors as harshly.')

            st.write('##### History Page')
            st.write('On the History page, you will be able to see the Brent Price key crises or the rallies. The crises will be highlighted in the price chart as red and rallies as green.')
            st.write('It is important to mention that the price usually increases or decreases because of politics and agreements between the countries inside OPEC.')

            st.write('##### Production & Consumption Page')
            st.write('On the Production & Consumption page, you can find the production and consumption through the years for Oil/Brent and also the standard deviation with the price.')
            st.write('The data was pulled from the link: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption')
            st.write('The exploratory analysis on this data can be found on the link: https://github.com/GusdPaula/postgraduation_fiap/blob/37856517ad72bcf1612756a317111cd8ea117cb6/fase_4/TCH/energy_consumption.ipynb')

            st.write('##### Maps Page')
            st.write('On the Maps page, you can find the oil production and consumption per country through the years.')
            st.write('The data was pulled from the link: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption')
            st.write('The exploratory analysis on this data can be found on the link: https://github.com/GusdPaula/postgraduation_fiap/blob/03939946a351c1632cab424a79ab9cf22b7c6d5f/fase_4/TCH/map_chart.ipynb')

            st.write('##### Prediction Page')
            st.write('On the Prediction page, you will see the price prediction for the next 7 days.')

            st.write('### Deployment Plan')
            st.write('The dashboard was deployed using Streamlit Cloud.')
            st.write('Streamlit allowed easy deployment and hosting of interactive data applications. Below are the detailed steps and considerations that were followed to deploy this dashboard: ')
            st.write('1. **Code and Dependencies Preparation:**')
            st.write('   - All code files were properly structured and pushed to a GitHub repository.')
            st.write('   - All required libraries and dependencies were listed in the **requirements.txt** file.')
            st.write('   - The entry point of the application was set to **app.py** or a similarly named file that contained the Streamlit logic to launch the dashboard.')
            st.write('2. **GitHub Repository:**')
            st.write('   - The code for this project was stored in a public or private GitHub repository, based on the user’s preference.')
            st.write('   - The repository contained the latest code, including **app.py**, **requirements.txt**, and any other files necessary for the dashboard’s functionality.')
            st.write('3. **Streamlit Cloud Setup:**')
            st.write('   - Streamlit Cloud was chosen as the fastest and easiest platform to deploy the dashboard. If the user didn’t have an account, they could sign up at: https://streamlit.io/cloud.')
            st.write('   - The user linked their GitHub account to Streamlit Cloud.')
            st.write('   - From Streamlit Cloud, a new app was created, and the GitHub repository containing the dashboard code was selected.')
            st.write('4. **Deployment Configuration:**')
            st.write('   - Once the repository was linked, the system automatically checked for a valid **app.py** file or the correct entry point and installed the dependencies from **requirements.txt**.')
            st.write('   - The app configuration was modified, if necessary, to specify the port number or other environment variables.')
            st.write('5. **Testing and Debugging:**')
            st.write('   - After Streamlit deployed the app, a public URL was received for the dashboard. The user visited this URL to check the functionality of the application.')
            st.write('   - If errors or issues occurred, the Streamlit logs were reviewed for debugging and troubleshooting.')
            st.write('   - It was recommended to test the app in different browsers and devices to ensure cross-platform compatibility.')
            st.write('6. **Monitoring and Optimization:**')
            st.write('   - Streamlit Cloud provided built-in monitoring tools, allowing real-time usage data to be viewed and any performance issues to be tracked.')
            st.write('   - If the app grew in traffic or complexity, additional computational resources or code optimizations were considered for better performance.')
            st.write('   - The app’s performance was regularly checked to determine if any improvements were needed.')
            st.write('7. **Future Enhancements and Scaling:**')
            st.write('   - As the project was a minimum viable product (MVP), the next steps included adding features like multi-user authentication, more interactive graphs, or data refresh capabilities.')
            st.write('   - The app could also be hosted on other cloud providers like AWS, Google Cloud, or Heroku if traffic increased or for long-term scalability.')
            st.write('   - Additional data sources or models were considered to enhance the dashboard’s functionality and predictive capabilities.')

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
            st.write(' - **Erro Quadrático Médio (MSE):** O MSE é uma função de custo que calcula a média dos quadrados dos erros, ou seja, a diferença quadrada média entre os valores estimados e os valores reais.')
            st.write(' - **Erro Percentual Absoluto Médio (MAPE):** O MAPE expressa o erro como uma porcentagem dos valores reais, fornecendo uma métrica fácil de entender.')
            st.write(' - **Erro Absoluto Médio (MAE):** O MAE mede a magnitude média dos erros em um conjunto de previsões, sem considerar sua direção. É a média da diferença absoluta entre os valores previstos e os valores reais. Ao contrário do MSE, ele não eleva os erros ao quadrado, o que significa que não pune os erros maiores com tanta severidade.')

            st.write('##### Página de História')
            st.write('Na página de História, você poderá ver as principais crises ou rallys do preço do Brent. As crises serão destacadas no gráfico de preços em vermelho e os rallys em verde.')
            st.write('É importante mencionar que os preços geralmente sobem ou descem por conta de atividades políticas e acordos entre os países da OPEP.')

            st.write('##### Página de Produção & Consumo')
            st.write('Na página de Produção & Consumo, você pode encontrar a produção e o consumo ao longo dos anos para o Petróleo/Brent, além da desvio padrão com o preço.')
            st.write('Os dados foram obtidos no link: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption')
            st.write('A análise exploratória desses dados pode ser encontrada no link: https://github.com/GusdPaula/postgraduation_fiap/blob/37856517ad72bcf1612756a317111cd8ea117cb6/fase_4/TCH/energy_consumption.ipynb')

            st.write('##### Página de Mapas')
            st.write('Na página de Mapas, você pode encontrar a produção e o consumo de petróleo por país ao longo dos anos.')
            st.write('Os dados foram obtidos no link: https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption')
            st.write('A análise exploratória desses dados pode ser encontrada no link: https://github.com/GusdPaula/postgraduation_fiap/blob/03939946a351c1632cab424a79ab9cf22b7c6d5f/fase_4/TCH/map_chart.ipynb')

            st.write('##### Página de Predição')
            st.write('Na página de Predição, você verá a previsão de preço para os próximos 7 dias.')

            st.write('### Plano de Implantação')
            st.write('O dashboard foi implantado usando o Streamlit Cloud.')
            st.write('O Streamlit permitiu a implantação e o hospedagem fácil de aplicativos de dados interativos. Abaixo estão as etapas detalhadas e considerações que foram seguidas para implantar esse dashboard:')
            st.write('1. **Preparação do Código e Dependências:**')
            st.write('   - Todos os arquivos de código foram devidamente estruturados e enviados para um repositório do GitHub.')
            st.write('   - Todas as bibliotecas e dependências necessárias foram listadas no arquivo **requirements.txt**.')
            st.write('   - O ponto de entrada do aplicativo foi definido como **app.py** ou um arquivo de nome semelhante que continha a lógica do Streamlit para iniciar o dashboard.')
            st.write('2. **Repositório do GitHub:**')
            st.write('   - O código deste projeto foi armazenado em um repositório público ou privado no GitHub, conforme a preferência do usuário.')
            st.write('   - O repositório continha o código mais recente, incluindo **app.py**, **requirements.txt** e outros arquivos necessários para a funcionalidade do dashboard.')
            st.write('3. **Configuração do Streamlit Cloud:**')
            st.write('   - O Streamlit Cloud foi escolhido como a plataforma mais rápida e fácil para implantar o dashboard. Caso o usuário não tivesse uma conta, ele poderia se inscrever em: https://streamlit.io/cloud.')
            st.write('   - O usuário conectou sua conta do GitHub ao Streamlit Cloud.')
            st.write('   - A partir do Streamlit Cloud, foi criado um novo aplicativo e o repositório do GitHub contendo o código do dashboard foi selecionado.')
            st.write('4. **Configuração da Implantação:**')
            st.write('   - Assim que o repositório foi vinculado, o sistema verificou automaticamente a presença de um arquivo **app.py** ou o ponto de entrada correto e instalou as dependências do **requirements.txt**.')
            st.write('   - A configuração do aplicativo foi modificada, se necessário, para especificar o número da porta ou outras variáveis de ambiente.')
            st.write('5. **Testes e Depuração:**')
            st.write('   - Após o Streamlit implantar o aplicativo, foi recebida uma URL pública para o dashboard. O usuário acessou essa URL para verificar a funcionalidade do aplicativo.')
            st.write('   - Caso ocorressem erros ou problemas, os logs do Streamlit foram revisados para depuração e resolução de problemas.')
            st.write('   - Foi recomendado testar o aplicativo em diferentes navegadores e dispositivos para garantir a compatibilidade entre plataformas.')
            st.write('6. **Monitoramento e Otimização:**')
            st.write('   - O Streamlit Cloud forneceu ferramentas de monitoramento integradas, permitindo visualizar os dados de uso em tempo real e acompanhar quaisquer problemas ou problemas de desempenho.')
            st.write('   - Se o aplicativo crescesse em tráfego ou complexidade, foram consideradas a adição de mais recursos computacionais ou a otimização do código para melhorar o desempenho.')
            st.write('   - O desempenho do aplicativo foi verificado regularmente para determinar se era necessário fazer melhorias.')
            st.write('7. **Melhorias Futuras e Escalabilidade:**')
            st.write('   - Como o projeto era um produto mínimo viável (MVP), os próximos passos incluíam a adição de recursos como autenticação de múltiplos usuários, gráficos mais interativos ou recursos de atualização de dados.')
            st.write('   - O aplicativo também poderia ser hospedado em outros provedores de nuvem, como AWS, Google Cloud ou Heroku, caso o tráfego aumentasse ou para garantir escalabilidade a longo prazo.')
            st.write('   - Fontes de dados ou modelos adicionais foram considerados para aprimorar a funcionalidade e as capacidades preditivas do dashboard.')
