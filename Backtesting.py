import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

def backtest(eth_data, signals):
    # Create a new DataFrame to store the results of the backtesting
    results = pd.DataFrame(index=eth_data.index, columns=['Position', 'Returns'])
    results['Position'] = np.nan
    results['Returns'] = np.nan

    # Initialize the current position and balance
    position = 0
    balance = 1000
    
    # Loop through each signal
    for i in range(len(signals)):
        # If there is a buy signal
        if signals[i] == 'Buy':
            # Buy one ETH for the current balance
            shares = balance / eth_data['close'][i]
            balance = 0
            position = shares
            results['Position'][i] = position
        # If there is a sell signal
        elif signals[i] == 'Sell':
            # Sell the current position of ETH
            balance = position * eth_data['close'][i]
            position = 0
            results['Position'][i] = position
        # Calculate the daily returns
        results['Returns'][i] = (eth_data['close'][i] - eth_data['close'][i-1]) / eth_data['close'][i-1]
    
    # Calculate the total returns
    results['Cumulative'] = (results['Returns'] + 1).cumprod()
    results['Cumulative'] = results['Cumulative'] * balance + position * eth_data['close'][-1]
    
    return results

