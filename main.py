import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
import yahoo_fin.stock_info as si
from scipy import stats 
#import requests
import base64

### Title ###
st.title('Stock Tracker')

st.markdown("""
This project aims to present any ***given stock*** currently existing on the NYSE with information regarding opening and closing price, its price to expense ratio, and a graph charting its performance.
* **Python libraries:** pandas, streamlit, numpy, matplotlib, yfinance    
""")

### SIDEBAR USER INPUT AREA
st.sidebar.header("User Input")
stock_symbol = st.sidebar.text_input("Please Insert Valid Stock Symbol Below")

## OPTIONS ## 
Selected_Metrics = st.sidebar.multiselect('Metrics', "Open", "High", "Low")

if stock_symbol:
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
    df = pd.DataFrame(data[['Open','High','Low']])
    st.dataframe(df)

if st.button("Show Extended Information"):   
    quote_table = si.get_quote_table(stock_symbol, dict_result = False)
    st.dataframe(quote_table)

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

st.button('Update')