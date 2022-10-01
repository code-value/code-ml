import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import yfinance as yf


data = yf.Ticker('BTC-USD')

# Actual price of Bitcoin in past 1 yr
bitcoin = data.history('1y')['Close']

# Number of Bitcoin purchased using $1000 1 yr ago
num_bitcoin = 1000/bitcoin.values[0]

# Value of Investment each day for 1 yr
value = np.array(bitcoin)*num_bitcoin


# percentage change in Bitcoin's price
x = bitcoin.pct_change()

#cumulative change for $1 of investment in Bitcoin
ret = (x + 1).cumprod()

plt.plot(ret)

plt.savefig('cumulative')

# Risk Analysis

annual_std = np.std(ret) * np.sqrt(252)
print("Volatility", annual_std)

sharpe = (np.mean(ret) / np.std(ret))*np.sqrt(252)

print("Sharpe", sharpe)

