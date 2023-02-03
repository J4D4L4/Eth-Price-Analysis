import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

def eth_price_analysis(eth_data):
    # Calculate Simple Moving Average (SMA)
    SMA = eth_data['close'].rolling(window=20).mean()
    # Calculate Bollinger Bands
    upper_band, middle_band, lower_band = talib.BBANDS(eth_data['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    # Calculate Relative Strength Index (RSI)
    RSI = talib.RSI(eth_data['close'], timeperiod=14)

    # Plot the price data, SMA, Bollinger Bands and RSI
    plt.figure(figsize=(20,10))
    plt.plot(eth_data['close'], label='Close')
    plt.plot(SMA, label='SMA')
    plt.plot(upper_band, label='Upper Band')
    plt.plot(middle_band, label='Middle Band')
    plt.plot(lower_band, label='Lower Band')
    plt.plot(RSI, label='RSI')
    plt.legend(loc='best')
    plt.show()

    # Check for buy or sell signals
    for i in range(len(eth_data)):
        if RSI[i] > 70:
            print("Sell signal at index {} with RSI {}".format(i, RSI[i]))
        elif RSI[i] < 30:
            print("Buy signal at index {} with RSI {}".format(i, RSI[i]))
        elif eth_data['close'][i] > upper_band[i]:
            print("Sell signal at index {} with price {}".format(i, eth_data['close'][i]))
        elif eth_data['close'][i] < lower_band[i]:
            print("Buy signal at index {} with price {}".format(i, eth_data['close'][i]))

# Load Ethereum price data into a pandas DataFrame
eth_data = pd.read_csv('eth_price_data.csv')
# Call the eth_price_analysis function
eth_price_analysis(eth_data)
