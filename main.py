import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
from scipy import stats 
import requests

st.title('Stock Tracker')

st.markdown("""
This project aims to present any ***given stock*** currently existing on the NYSE with information regarding opening and closing price, its price to expense ratio, and a graph charting its performance.
* **Python libraries:** pandas, streamlit, numpy, matplotlib, yfinance    
""")

st.sidebar.header('User Input Features')

@st.cache