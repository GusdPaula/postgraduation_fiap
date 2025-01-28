import streamlit as st
import plotly.graph_objects as go
import pandas as pd

class HistoryPage():
    '''
        Page to show the main events behind brent price
    
    '''
    def __init__(self, df: pd.DataFrame, lang):
        
        # creating price plot
        fig_price = go.Figure(data=[go.Bar(x=df['Date'], y=df['Close'])])
        fig_price.update_layout(title='Brent Price Over Time in USD' if lang == 'EN' else 'Preço do Petróleo no tempo em Dólar')

        fig_price.update_layout(
            xaxis_title=None,
            yaxis_title=None,
            xaxis_rangeslider_visible=True
        )

        # Adding buttons grid
        col_button_cri_2008, col_button_cri_2014, col_button_cri_2020, col_button_high_2022 = st.columns(4)

        # Buttons and their respective events
        # Events will have their individual text and the one square added in the price plot
        text = 'Click on the buttons to see what happened with Brent Price... ' if lang == 'EN' else 'Clique nos botões para ver o que houve com o preço...'
        with col_button_cri_2008:
            if st.button('2008 Crisis' if lang == 'EN' else 'Crise de 2008'):
                fig_price.add_vrect(x0='2008-1-1', x1='2008-12-31', line_width=0, fillcolor="red", opacity=0.2)

                if lang == 'EN':
                    text = 'In the past, supply disruptions triggered by political events have caused oil prices to shift drastically; the Iranian revolution, Iran-Iraq war, Arab oil embargo, and Persian Gulf wars have been especially notable. The Asian financial crisis and the global economic crisis of 2007-2008 also caused fluctuation... the price run-up of 2007–08 was caused by strong demand confronting stagnating world production.'
                else:
                    text = 'No passado, as interrupções de fornecimento causadas por eventos políticos fizeram com que os preços do petróleo mudassem drasticamente; a revolução iraniana, a guerra Irã-Iraque, o embargo árabe ao petróleo e as guerras do Golfo Pérsico foram especialmente notáveis. A crise financeira asiática e a crise econômica global de 2007-2008 também causaram flutuações... o aumento de preços de 2007-08 foi causado pela forte demanda frente à estagnação da produção mundial.'

        with col_button_cri_2014:
            if st.button('2014-2016 Crisis' if lang == 'EN' else 'Crise de 2014-2016'):
                fig_price.add_vrect(x0='2014-1-1', x1='2016-12-31', line_width=0, fillcolor="red", opacity=0.2)
                    
                if lang == 'EN':
                    text = "Between 2014 and 2016, global oil prices collapsed from over $100 per barrel to below $30 due to oversupply, especially from U.S. shale production, and OPEC's decision not to cut production. A slowdown in global demand, particularly from China, worsened the situation. This caused financial stress for oil-producing countries and companies, with many facing bankruptcies. In late 2016, OPEC and non-OPEC countries (OPEC+) agreed to cut production, leading to a gradual price recovery. By the end of 2016, prices started to stabilize above $50 per barrel."
                else:
                    text = "Entre 2014 e 2016, os preços globais do petróleo colapsaram de mais de $100 por barril para abaixo de $30 devido ao excesso de oferta, especialmente da produção de xisto dos EUA, e à decisão da OPEC de não reduzir a produção. Uma desaceleração da demanda global, particularmente da China, piorou a situação. Isso causou estresse financeiro para os países e empresas produtoras de petróleo, com muitas enfrentando falências. No final de 2016, a OPEC e os países não membros da OPEC (OPEC+) concordaram em cortar a produção, levando a uma recuperação gradual dos preços. Até o final de 2016, os preços começaram a se estabilizar acima de $50 por barril."

        with col_button_cri_2020:
            if st.button('2020 Crisis' if lang == 'EN' else 'Crise de 2020'):
                fig_price.add_vrect(x0='2020-1-1', x1='2020-12-31', line_width=0, fillcolor="red", opacity=0.2)

                if lang == 'EN':
                    text = "The Brent Crude oil crisis of 2020 was driven by the COVID-19 pandemic, which drastically reduced global oil demand. In March, a price war between Saudi Arabia and Russia caused oil prices to plummet. By April, oil prices briefly dropped below $20 per barrel, and the WTI benchmark even went negative. In response, OPEC+ agreed to historic production cuts. Oil prices slowly recovered through the second half of 2020, but the market remained volatile."
                else:
                    text = "A crise do petróleo Brent de 2020 foi impulsionada pela pandemia de COVID-19, que reduziu drasticamente a demanda global de petróleo. Em março, uma guerra de preços entre a Arábia Saudita e a Rússia fez os preços do petróleo despencarem. Em abril, os preços do petróleo caíram brevemente para abaixo de $20 por barril, e o benchmark WTI chegou até a entrar em território negativo. Em resposta, a OPEC+ concordou com cortes históricos na produção. Os preços do petróleo se recuperaram lentamente ao longo do segundo semestre de 2020, mas o mercado continuou volátil."

        with col_button_high_2022:
            if st.button('2022 Rally' if lang == 'EN' else 'Aumento em 2022'):
                fig_price.add_vrect(x0='2021-6-1', x1='2022-12-31', line_width=0, fillcolor="green", opacity=0.2)

                if lang == 'EN':
                    text = "In 2022, oil prices surged due to the Russia-Ukraine war, which disrupted global oil supplies and led to sanctions on Russian oil exports. Ongoing production cuts by OPEC+ and post-pandemic demand recovery also strained supply, pushing prices higher. Inflation and market speculation further contributed to the rally. By mid-year, Brent Crude prices hit around $120 per barrel. The combination of geopolitical tensions and supply-demand imbalances fueled the price increase."
                else:
                    text = "Em 2022, os preços do petróleo dispararam devido à guerra entre a Rússia e a Ucrânia, que interrompeu os fornecimentos globais de petróleo e levou a sanções contra as exportações de petróleo russo. Os cortes contínuos de produção da OPEC+ e a recuperação da demanda pós-pandemia também tensionaram a oferta, elevando os preços. A inflação e a especulação do mercado contribuíram ainda mais para o aumento. A meio do ano, os preços do Brent Crude chegaram a cerca de $120 por barril. A combinação das tensões geopolíticas e os desequilíbrios entre oferta e demanda impulsionaram o aumento do preço."

        # Showing the text and plot
        st.write(text)
        st.plotly_chart(fig_price)