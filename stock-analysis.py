import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Stock ticker
ticker = 'AAPL'

# Download stock data
data = yf.download(ticker, start='2020-01-01', end='2024-01-01')

# Closing prices
data['Close'].plot(figsize=(10, 5), title='Apple Stock Price')

# Daily returns
data['Returns'] = data['Close'].pct_change()

# Moving averages
data['MA50'] = data['Close'].rolling(window=50).mean()
data['MA200'] = data['Close'].rolling(window=200).mean()

# Plot moving averages
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['MA50'], label='50-Day MA')
plt.plot(data['MA200'], label='200-Day MA')

plt.title('Stock Analysis')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Volatility
volatility = data['Returns'].std()

print("Stock Volatility:", volatility)

plt.show()
