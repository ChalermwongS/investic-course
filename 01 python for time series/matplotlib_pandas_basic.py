# -*- coding: utf-8 -*-
"""Copy of Matplotlib Pandas Basic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ihQxt0_jHwTM2GBCL-NtZK7fa0ZN8CL1
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

np.random.normal(0.05/250,0.1/250,100)

a = pd.Series(np.random.normal(0.05/250,0.1/250,100))

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

b = (a+1).cumprod()-1
b.plot()

df = pd.DataFrame(np.random.randn(1000,4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
plt.figure()
df.plot()

df = pd.DataFrame(np.random.randn(1000, 2), columns=['B','C']).cumsum()
df['A'] = pd.Series(list(range(len(df))))
df.plot(x='A', y='B')

plt.figure()
df.iloc[5].plot(kind='bar')

df2 = pd.DataFrame(np.random.rand(10,4), columns=['a','b','c','d'])
df2.plot.bar()

df2.plot.bar(stacked=True)

df2.plot.barh(stacked=True)

#Histogram
df = pd.DataFrame(
    {
        'a':np.random.randn(1000) + 1,
        'b':np.random.randn(1000),
        'c':np.random.randn(1000) - 1
    },
    columns=['a','b','c']
)

plt.figure()

df.plot.hist(alpha=0.5)

plt.figure()

df.plot.hist(stacked=True, bins=20)

data = pd.Series(np.random.randn(1000))

data.hist(by=np.random.randint(0, 4, 1000), figsize=(6,4))

df = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])
ax = df.plot.scatter(x="a", y="b", color="Red", label="Group 1")

df.plot.scatter(x="c", y="d", color="Green", label="Group 2", ax=ax)

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df.plot(subplots=True, figsize=(6, 6))

