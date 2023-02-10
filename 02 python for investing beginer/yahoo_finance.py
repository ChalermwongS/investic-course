# -*- coding: utf-8 -*-
"""Yahoo Finance

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HvaXt_IYpgY3nKgOpyte2HPpGZw8Kxdu
"""

!pip install yfinance

import pandas as pd
import yfinance as yf

start = '2021-01-01'
end = '2022-01-01'

"""#ตอนนี้เราไม่จำเป็นต้องใช้ yf.pdr แล้วนะครับสามารถดึงด้วย yf.download ได้เลย"""

data = yf.download('TSLA', start=start, end=end)

data

