import numpy as np  
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


data = yf.download(["SPY", "GLD", "TLT"], start="2005-01-01", end="2025-01-01", interval="1mo")


#print(data.columns)   # What kind of data do you have?
#print(data.head())    # Peek at the first few rows
#print(data.shape)     # How big is it?

close = data['Close']

p_t_minus_1 = close.shift(1)
p_t_minus_12 = close.shift(12)
momentum = p_t_minus_1 / p_t_minus_12 - 1


#print(momentum.head(15))


# Step 1: signal mask
signal = (momentum > 0).astype(float)   # 1 if in position, 0 if not

# Step 2: forward return
forward_return = close.shift(-1) / close - 1

# Step 3: strategy return
strategy_return = signal * forward_return

cumulative = (1 + strategy_return).cumprod()


cumulative.plot(title="Momentum Strategy Equity Curve")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.grid(True)
plt.show()
plt.savefig("momentum_plot.png", dpi=300)

