# -*- coding: utf-8 -*-
"""Investic-mplfinance

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BQZgO9zbiyuLUUhb0mekHIPKR6tlpInG
"""

!pip install mplfinance

!pip install python-binance

!pip install yfinance

"""# Prepare Data"""

import pandas as pd
import mplfinance as mpf
from binance.client import Client
import yfinance as yf

start = '2020-01-01'
end = '2021-01-01'

data = yf.download("ETH-USD",period='1d',start=start,end=end)

data

from binance.client import Client
client = Client()

data = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_1DAY, start, end)

data

ETH = pd.DataFrame(data, columns =['otime','open','high','low','close','volume','ctime',
                                'quote_vol','no_trade','taker_base_vol','taker_quote_vol','ignore'])

ETH

ETH = ETH[['otime','open','high','low','close','volume']]
ETH['otime'] = pd.to_datetime(ETH['otime'],unit= 'ms')

ETH

ETH.set_index('otime')

ETH

ETH = ETH.set_index('otime')

ETH = ETH.astype(float)

ETH

ETH.loc['2020-01':'2020-03']

mpf.plot(ETH.loc['2020-01':'2020-03'])







mpf.plot(ETH[:'2020-03'], type='candle')

mpf.plot(ETH['2020-07':], type='candle')

mpf.plot(ETH['2020-07':], type='line')



mpf.plot(ETH['2020-06':'2020-12'], type='candle', volume=True)

mpf.plot(ETH['2020-06':'2020-12'], type='candle', volume=True,figsize=(16,10))

"""# ตกแต่ง"""

mpf.plot(ETH['2020-06':'2020-12'], hlines=dict(hlines=[500,330], colors=['r','g'], linestyle='--'), type='candle')

"""![image.png](data:image/png;base64,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)"""

mpf.plot(ETH['2020-06':'2020-12'], hlines=dict(hlines=[500, 300], colors=['r','g'], linestyle='-'), type='candle')

mpf.plot(ETH['2020-06':'2020-12'], hlines=dict(hlines=[500, 300], colors=['r','g'], linestyle='solid'), type='candle')

"""### worth reading
### vline
### tline
https://github.com/matplotlib/mplfinance/blob/master/examples/using_lines.ipynb
"""

mpf.plot(ETH, type='candle', mav=(12,26,100))

mpf.plot(ETH[:'2020-4'], type='candle', volume=True, mav=(12,26),figsize=(20,10))

"""# ตกแต่งกันหน่อย !!
### tight_layout
### title

"""

mpf.plot(ETH, type='candle', volume=True, mav=(12,26,9), title='ETH Price na ja',tight_layout=True, figratio=(8, 4))



"""# make_addplot"""

ret = ETH['close'].pct_change(2)

ret

ETH.close

134.35/130.77-1

ret_add = mpf.make_addplot(ret, color='yellow', ylabel='return')

mpf.plot(ETH, addplot=ret_add)

ret_add = mpf.make_addplot(ret, color='g', panel=1,  ylabel='return')

mpf.plot(ETH, addplot=ret_add)

mpf.plot(ETH, addplot=ret_add,volume=True)

ret_add = mpf.make_addplot(ret, color='green', panel=2,  ylabel='return')
mpf.plot(ETH, addplot=ret_add,volume=True,mav=(12,26))

ETH.close

ETH.close.rolling(5).mean()

#Don't !!
ETH.close.ewm(3).mean()

ETH['EMA_5'] = ETH['close'].ewm(5,adjust=False,min_periods=5).mean()

ema_plot = mpf.make_addplot(ETH['EMA_5'], ylabel='ema_5')

mpf.plot(ETH,addplot=ema_plot,style='charles')

mpf.plot(ETH[:'2020-03'],type='candle',style='yahoo',mav=(5,12,21),volume=True)
