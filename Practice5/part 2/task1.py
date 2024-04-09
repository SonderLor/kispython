import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("data.txt", sep=";", header=None)
data_dict = dict()
for i in range(len(data)):
    if data.iloc[i, 3] != "не издана":
        data_dict[data.iloc[i, 3]] = data_dict.get(data.iloc[i, 3], 0) + 1
x, y = list(), list()
for key, value in data_dict.items():
    x.append(key)
    y.append(value)
plt.plot(x, y)
plt.show()
