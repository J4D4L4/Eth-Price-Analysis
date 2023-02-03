import pandas as pd
from pandas_datareader import data as pdr
import datetime
import yfinance as yfin

# Specify start and end date for the data
start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
yfin.pdr_override()
# Download Ethereum data using pandas_datareader library
eth_data = pdr.DataReader('ETH-USD', start, end)

# Filter data to include only close, open, high and low columns
eth_data = eth_data[['Date','Close', 'Open', 'High', 'Low']]

# Save the data to a CSV file
eth_data.to_csv('eth_data.csv', index=False)

# Print the first 5 rows of the data
print(eth_data.head())
