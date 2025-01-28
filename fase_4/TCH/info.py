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
            st.write(' - Mean Squared Error (MSE): MSE is a cost function that calculates the average of the squares of the errors—i.e., the average squared difference between the estimated values and the actual value.')
            st.write(' - Mean Absolute Percentage Error (MAPE): MAPE expresses the error as a percentage of the actual values, providing an easy-to-understand metric.')
            st.write(' - Mean Absolute Error (MAE): MAE measures the average magnitude of the errors in a set of predictions, without considering their direction. It is the average absolute difference between the predicted and actual values. Unlike MSE, it doesn’t square the errors, which means it doesn’t punish larger errors as harshly.')

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
            st.write('The dashboard was deployed using **Streamlit Cloud**.')
            st.write('Streamlit allows easy deployment and hosting of interactive data applications. Here are the detailed steps and considerations for deploying this dashboard: ')
            st.write('1. **Prepare the Code and Dependencies: **')
            st.write('   - Make sure all code files are properly structured and pushed to a GitHub repository.')
            st.write('   - Ensure that all the required libraries and dependencies are listed in the **requirements.txt** file.')
            st.write('   - Ensure the entry point of the application is **app.py** or a similarly named file that contains the Streamlit logic to launch the dashboard.')
            st.write('2. **GitHub Repository: **')
            st.write('   - The code for this project should be stored in a public or private GitHub repository, depending on your preference.')
            st.write('   - Make sure the repository contains the latest code, including your **app.py**, **requirements.txt**, and any other files necessary for the dashboard’s functionality.')
            st.write('3. **Streamlit Cloud Setup: **')
            st.write('   - Streamlit Cloud is the easiest and fastest platform to deploy your dashboard. If you don’t have an account, you can sign up at: https://streamlit.io/cloud.')
            st.write('   - Link your GitHub account to Streamlit Cloud.')
            st.write('   - From Streamlit Cloud, create a new app and select your GitHub repository containing your dashboard code.')
            st.write('4. **Deployment Configuration: **')
            st.write('   - Once your repository is linked, the system will automatically check for a valid **app.py** file or the correct entry point and will install the dependencies from **requirements.txt**.')
            st.write('   - You can modify the app configuration to specify the port number or other environment variables if necessary.')
            st.write('5. **Testing and Debugging: **')
            st.write('   - After Streamlit deploys the app, you will receive a public URL for the dashboard. Visit this URL and check the functionality of your application.')
            st.write('   - If you encounter errors or issues, review the Streamlit logs for debugging and troubleshooting.')
            st.write('   - It’s recommended to also test the app in different browsers and devices to ensure cross-platform compatibility.')
            st.write('6. **Monitoring and Optimization: **')
            st.write('   - Streamlit Cloud provides built-in monitoring tools, which allow you to view real-time usage data and track any issues or performance problems.')
            st.write('   - If your app grows in traffic or complexity, you might want to consider adding more computational resources or optimize the code for better performance.')
            st.write('   - Regularly check the app performance to see if you need to make changes or improve any part of the dashboard.')
            st.write('7. **Future Enhancements and Scaling: **')
            st.write('   - As this project is a minimum viable product (MVP), the next steps might include adding additional features like multi-user authentication, more interactive graphs, or data refresh capabilities.')
            st.write('   - You can also consider hosting your app on other cloud providers like AWS, Google Cloud, or Heroku in case of high traffic or to ensure long-term scalability.')
            st.write('   - Consider adding more data sources or models to enhance the dashboard’s functionality and predictive capabilities.')

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
            st.write('O dashboard foi implantado usando **Streamlit Cloud**.')
            st.write('O Streamlit permite a implantação e hospedagem de aplicativos interativos de dados com facilidade. Aqui estão os passos detalhados e considerações para implantar este dashboard: ')
            st.write('1. **Preparar o Código e as Dependências: **')
            st.write('   - Certifique-se de que todos os arquivos de código estejam bem estruturados e enviados para um repositório no GitHub.')
            st.write('   - Verifique se todas as bibliotecas e dependências necessárias estão listadas no arquivo **requirements.txt**.')
            st.write('   - Certifique-se de que o ponto de entrada da aplicação seja o **app.py** ou um arquivo com a lógica do Streamlit para lançar o dashboard.')
            st.write('2. **Repositório no GitHub: **')
            st.write('   - O código para este projeto deve ser armazenado em um repositório público ou privado do GitHub, dependendo da sua preferência.')
            st.write('   - Verifique se o repositório contém o código mais recente, incluindo o **app.py**, **requirements.txt** e quaisquer outros arquivos necessários para a funcionalidade do dashboard.')
            st.write('3. **Configuração do Streamlit Cloud: **')
            st.write('   - O Streamlit Cloud é a plataforma mais fácil e rápida para implantar seu dashboard. Se você não tiver uma conta, pode se inscrever em: https://streamlit.io/cloud.')
            st.write('   - Vincule sua conta do GitHub ao Streamlit Cloud.')
            st.write('   - No Streamlit Cloud, crie um novo aplicativo e selecione seu repositório do GitHub que contém o código do dashboard.')
            st.write('4. **Configuração de Implantação: **')
            st.write('   - Depois que o repositório for vinculado, o sistema verificará automaticamente se existe um arquivo **app.py** válido ou o ponto de entrada correto e instalará as dependências do **requirements.txt**.')
            st.write('   - Você pode modificar a configuração do aplicativo para especificar o número da porta ou outras variáveis de ambiente, se necessário.')
            st.write('5. **Testando e Depurando: **')
            st.write('   - Após a implantação do aplicativo, você receberá uma URL pública para o dashboard. Acesse essa URL e verifique o funcionamento do aplicativo.')
            st.write('   - Se encontrar erros ou problemas, revise os logs do Streamlit para depurar e solucionar os problemas.')
            st.write('   - Também é recomendável testar o aplicativo em diferentes navegadores e dispositivos para garantir a compatibilidade entre plataformas.')
            st.write('6. **Monitoramento e Otimização: **')
            st.write('   - O Streamlit Cloud fornece ferramentas de monitoramento integradas, que permitem visualizar os dados de uso em tempo real e acompanhar quaisquer problemas ou problemas de desempenho.')
            st.write('   - Se o seu aplicativo crescer em tráfego ou complexidade, você pode considerar adicionar mais recursos computacionais ou otimizar o código para melhorar o desempenho.')
            st.write('   - Verifique regularmente o desempenho do aplicativo para ver se você precisa fazer alterações ou melhorar alguma parte do dashboard.')
            st.write('7. **Melhorias Futuras e Escalabilidade: **')
            st.write('   - Como este projeto é um produto mínimo viável (MVP), os próximos passos podem incluir adicionar recursos adicionais como autenticação de múltiplos usuários, gráficos mais interativos ou recursos de atualização de dados.')
            st.write('   - Você também pode considerar hospedar o aplicativo em outros provedores de nuvem, como AWS, Google Cloud ou Heroku, em caso de alto tráfego ou para garantir escalabilidade a longo prazo.')
            st.write('   - Considere adicionar mais fontes de dados ou modelos para melhorar a funcionalidade e as capacidades preditivas do dashboard.')

