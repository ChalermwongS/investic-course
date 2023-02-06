# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:45:40 2023

@author: Chalermwong
"""

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

##################################################################

plt.plot([1,2,3,4], [1,4,9,16])
plt.xlabel('Square Number')
plt.ylabel('Normal Number')
plt.show()

##################################################################

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.show()

##################################################################

x = np.array([130,147,138,185,174,166,153,162,168])
y = np.array([96,73,88,92,81,70,69,85,84])

plt.xlim(120,200)
plt.ylim(60,100)
plt.scatter(x,y)
plt.title('Scatter Plot')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()

##################################################################

bar = ['bar-1','bar-2','bar-3','bar-4']
bars = [70,65,30,58]

plt.bar(bar, bars, color='red')
plt.title('Bar Graph')
plt.xlabel('Type')
plt.ylabel('Range')
plt.show()

##################################################################

x = np.random.randn(1000)

plt.title('Histogram')
plt.xlabel('Random Data')
plt.ylabel('Freq')
plt.hist(x, 10)
plt.show()

##################################################################

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IO')
plt.text(60, .025, r'$\mu=100,\ \ sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

##################################################################

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

fig = plt.figure(figsize =(10, 10))
  
sub1 = plt.subplot(2, 2, 1)
sub2 = plt.subplot(2, 2, 2)
sub3 = plt.subplot(2, 2, 3)
sub4 = plt.subplot(2, 2, 4)
  
sub1.plot(a, 'sb')
sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st')
  
sub2.plot(b, 'or')
sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd')
  
sub3.plot(list(range(0, 22, 3)), 'vg')
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title('3rd')
  
sub4.plot(c, 'Dm')
sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th')
  
plt.show()

##################################################################














