# -*- coding: utf-8 -*-
"""Copy of Matplotlib Pandas Visualize

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ILJx1HqiEfEmkNOUNbbV8tjPvk825zj-
"""

# !pip install yfinance

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
yf.pdr_override()

start = '2000-01-01'
end = '2021-08-31'

spy = pdr.get_data_yahoo('SPY', start=start, end=end)
qqq = pdr.get_data_yahoo('QQQ', start=start, end=end)

spy

spy['Close'].plot()

spy['Daily Return'] = spy.Close.pct_change()

spy['Daily Return'].plot()

spy.iloc[-20:].plot.bar(y='Daily Return', color='k')

qqq['Daily Return'] = qqq.Close.pct_change()

qqq.iloc[-20:].plot.bar(y='Daily Return', color='b')

df = spy.join(qqq, rsuffix='_r')

df

df.iloc[-20:].plot(y=['Daily Return','Daily Return_r'])

df.iloc[-20:].plot.bar(y=['Daily Return', 'Daily Return_r'])

df.iloc[-20:].plot.bar(y=['Daily Return', 'Daily Return_r'], stacked=True)

df.iloc[-1000:].plot.hist(y=['Daily Return', 'Daily Return_r'], bins=50, alpha=0.5)

df.iloc[-1000:].plot.hist(y=['Daily Return', 'Daily Return_r'], bins=50, alpha=0.5, cumulative=True)

df.iloc[-1000:].plot.scatter(x='Daily Return', y='Daily Return_r', color='orange')

df.plot(y=['Close','Close_r'])

df.iloc[-100:].plot(y=['Close'], style='k--')

spy.plot(subplots=True, figsize=(10,10))

