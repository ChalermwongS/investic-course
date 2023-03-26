# -*- coding: utf-8 -*-
"""Workshop - SMA Cross Over

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17G2IrQSaGhVgbpnMqgzmoEcF-LTbfI9c
"""

!pip install yfinance

!pip install mplfinance

import pandas as pd
import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

"""## ดึงข้อมูลราคา Bitcoin"""

data = yf.download('BTC-USD', start='2021-01-01', end='2022-01-01')

df = data.copy()

"""#สร้างเส้นค่าเฉลี่ยเส้นสั้น 12 กับเส้นยาว 26 โดยใช้ Function Rolling"""

df['sma_short'] = df.Close.rolling(12).mean()
df['sma_long'] = df.Close.rolling(26).mean()

"""##เวลาเราต้องการจะ Plot ลงในรูปเดียวกันกับราคาบน mplfinance จำเป็นต้องสร้าง addplot โดยจะต้องใส่สองเส้นเข้าไปนั้นคือ SMA12 และ SMA26 โดยให้เส้นสั้นเป็นสีส้มและเส้นยาวเป็นสีเหลือง"""

sma_short = mpf.make_addplot(df['sma_short'], color='orange')
sma_long = mpf.make_addplot(df['sma_long'], color='y')

"""##สร้างเป็น List เอาไว้ก่อนเข้าไปใส่ใน Function plot ของ mplfinance"""

sma_list = [sma_short, sma_long]

"""##แล้วเราก็ Plot ก็จะเห็นว่าทั้งสองเส้นนั้นเข้าไปอยู่บนกราฟแท่งเทียนก่อนหน้านี้เรียบร้อย"""

mpf.plot(df,style='yahoo', type='candle', addplot = sma_list, figsize=(14,6))

df

"""## ต่อมาคือการสร้าง condition เพื่อให้ส่งคำสั่งโดย เมื่อเส้นสั้นมีค่ามากกว่าเส้นยาวให้ทำการซื้อ โดยเราจะสร้างตัวแปรที่เรียกว่า trend ขึ้นมาก่อน แล้วเช็คว่า sma เส้นสั้นมีค่ามากกว่า sma เส้นยาวหรือไม่"""

df['trend'] = df['sma_short'] > df['sma_long']

df

"""#ต่อมาเราทำการ shift ไป 1 ค่าเพื่อเช็คว่าแท่งของวันต่อไปตรงกันหรือไม่หากไม่ตรงก็ให้ Action ในวันนั้น"""

df['trend_shift'] = df.trend.shift(1)

df

"""##หาก trend มีค่าเป็น true และ  shift trend มีค่าเป็น fasle ให้ action buy กลับกัน หาก trend มีค่าเป็น false และ  shift trend มีค่าเป็น true ให้ action sell"""

df.loc[(df.trend == True) & (df.trend_shift == False),'action'] = 'buy'
df.loc[(df.trend == False) & (df.trend_shift == True),'action'] = 'sell'

df

df[df.action=='buy']

"""##ส่วนนี้จะเป็นการ Mark Ticker ของลูกศรที่บอกสัญญาณซื้อขาย หาก buy ให้ Mark ต่ำกว่าที่ 0.95 หาก Sell ให้ Mark ที่สูงกว่า 1.05"""

df.loc[df['action'] == 'buy', 'marker_position'] = df['Low'] *0.95
df.loc[df['action'] == 'sell', 'marker_position'] = df['High'] *1.05

df[df.marker_position.notnull()]

"""## เลือกว่าเราต้องการ buy หรือ sell"""

#buy action dataframe
a = df.loc[df.action == 'buy']

#sell action dataframe
b = df.loc[df.action == 'sell']

b

plt.figure(figsize=(16,9))
plt.plot(df.Close, label='Close Price')
plt.plot(df.sma_short, label='SMA 12')
plt.plot(df.sma_long, label='SMA 26')
plt.plot(a.marker_position, 'g^', markersize=10)
plt.plot(b.marker_position, 'rv', markersize=10)
plt.legend()

