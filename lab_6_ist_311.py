# -*- coding: utf-8 -*-
"""lab#6 IST-311

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VNxvteBy-Yt1O4qvYF503TPOfZHp-h48
"""

import matplotlib.pyplot as plt

celsius = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
fahrenheit = [[-88.6], [-29.2], [32.0], [93.2], [129.2], [152.6], [212.0]]

plt.figure(figsize=(15,8), dpi=50)
plt.scatter(celsius, fahrenheit, label='Входные значения', color='green', marker='$f$');
plt.xlabel('celsius')
plt.ylabel('fahrenheit')
plt.legend()
plt.grid(True)
plt.show()

for c, f in zip(celsius, fahrenheit):
  print(f'цельсия {c}= фаренгейт {f}')

import sklearn

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(celsius, fahrenheit)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
celsius_test = [[-50], [10], [30], [20], [10], [70], [87]]
fahrenheit_test = lr.predict(celsius_test)
fahrenheit_test

import numpy as np

x_range = np.arange(-70, 120)
y_range = x_range*1.8+32

plt.figure(figsize=(15,8), dpi=200)
plt.scatter(x_range, y_range, label='уравнения', linewidth = '1')
plt.scatter(celsius, fahrenheit, label='входные данные', color='green')
plt.scatter(celsius_test, fahrenheit_test, label='предсказанное значение', color='blue')
plt.xlabel('Цельсия')
plt.ylabel('Фаренгейта')
plt.legend()
plt.grid(True)
plt.show()

"""Задания для самостоятельного выполнения"""

import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression

fahrenheit = [[-100], [-70], [-30], [0], [40], [80], [120]]
kelvin = [[199.8], [216.5], [238.7], [255.4], [277.6], [299.8], [322]]

for f, k in zip(fahrenheit, kelvin):
  print(f'фаренгейт {f}= кельвин {k}')

plt.figure(figsize=(15,8), dpi=50)
plt.scatter(fahrenheit, kelvin, label='Входные значения', color='red', marker='$f$');
plt.xlabel('fahrenheit')
plt.ylabel('kelvin')
plt.legend()
plt.grid(False)
plt.show()

x_range = np.arange(-100, 120)
y_range = (x_range-32) * 5/9 + 273.15

lr = LinearRegression()
lr.fit(fahrenheit, kelvin)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
fahrenheit_test = [[-50], [10], [30], [20], [10], [70], [87]]
kelvin_test = lr.predict(fahrenheit_test)
kelvin_test

plt.figure(figsize=(15,8), dpi=200)
plt.scatter(x_range, y_range, label='уравнения', linewidth = '1')
plt.scatter(fahrenheit, kelvin, label='входные данные', color='yellow')
plt.scatter(fahrenheit_test, kelvin_test, label='предсказанное значение', color='blue')
plt.xlabel('Фаренгейта')
plt.ylabel('Кельвин')
plt.legend()
plt.grid(False)
plt.show()