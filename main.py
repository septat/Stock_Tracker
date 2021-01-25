import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
from scipy import stats 
#import requests
import base64

st.title('Stock Tracker')

st.markdown("""
This project aims to present any ***given stock*** currently existing on the NYSE with information regarding opening and closing price, its price to expense ratio, and a graph charting its performance.
* **Python libraries:** pandas, streamlit, numpy, matplotlib, yfinance    
""")


stock_symbol = st.text_input("Please Insert Valid Stock Symbol Below")

# OPTIONS # INSERT CHECKBOXES WITH AN UPDATE BUTTON So that things can be updated realtively easily for the user 
# time = st.text_input("Please enter a time frame")
# inter
#  


if (stock_symbol):
    data = yf.download(
        tickers=stock_symbol,
        period="ytd",
        interval="1d",
        group_by='ticker',
        auto_adjust=True,
        prepost=True,
        threads=True,
        proxy=None
        )
    print(data)
    df = pd.DataFrame(data[['Open','High','Low']])
    st.dataframe(df)
    
# def price_plot(symbol):
#   df = pd.DataFrame(data[symbol].Close)
#   df['Date'] = df.index
#   plt.title(stock_symbol, fontweight='bold')
#   plt.xlabel('Date', fontweight='bold')
#   plt.ylabel('Closing Price', fontweight='bold')
#   return st.pyplot()

# if st.button('Show Plots'):
#     st.header('Stock Closing Price')
#     price_plot(stock_symbol)


### THE SIDEBAR CANT BE IMPLEMENTED FOR LACK OF CONCRETE IDEA OF IMPLEMENTATION
#st.sidebar.header('User Input Features')



# CSV FILE DOWNLOAD # 
# def filedownload(df):
#     csv = df.to_csv(index=False)
#     # strings <-> bytes conversions
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
#     return href
