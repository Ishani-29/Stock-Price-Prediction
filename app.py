import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
import streamlit as st

# Define the ticker symbol and date range
# ticker_symbol = 'AAPL'
start_date = '2014-01-01'
end_date = '2024-01-01'

st.title('Stock Trend Prediction')
# Download historical data
user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = yf.download(user_input, start=start_date, end=end_date)

#Describing data
st.subheader('Data from 2014 - 2023')
st.write(df.describe())