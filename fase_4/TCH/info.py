import streamlit as st

class InfoPage():
    def __init__(self):
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
        
        st.write('##### Prediction Page')
        st.write('On the Prediction page you will see the price prediction for the next 7 days.')