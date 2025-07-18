# -*- coding: utf-8 -*-
"""Beginners Task .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Wy4QutFv6AaCRfXzRWBEfiZWxu7Ut6sr
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 15, 13, 18, 16])

plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

x = ['A', 'B', 'C', 'D']
y = [10, 15, 7, 12]

plt.bar(x, y, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()

data = np.random.normal(100, 20, 200)

plt.hist(data, bins=10, color='lightgreen', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='orange')
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

labels = ['A', 'B', 'C', 'D']
sizes = [20, 30, 25, 25]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

plt.pie(sizes, labels=labels, colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
plt.title('Pie Chart')
plt.show()

x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 8, 7]

plt.fill_between(x, y, color='skyblue', alpha=0.4)
plt.plot(x, y, color='blue')
plt.title('Area Chart')
plt.show()

import pandas as pd

df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 15, 13, 18, 16]})
df.plot(x='x', y='y', kind='line', title='Line Plot')

df = pd.DataFrame({'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 15, 7, 12]})
df.plot(x='Category', y='Values', kind='bar', color='skyblue', title='Bar Chart')

df = pd.DataFrame({'data': np.random.normal(100, 20, 200)})
df.plot(kind='hist', bins=10, color='lightgreen', edgecolor='black', title='Histogram')

df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
df.plot(kind='scatter', x='x', y='y', color='orange', title='Scatter Plot')

df = pd.Series([20, 30, 25, 25], index=['A', 'B', 'C', 'D'])
df.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'], title='Pie Chart')

df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [3, 5, 2, 8, 7]})
df.set_index('x').plot(kind='area', alpha=0.4, title='Area Chart')