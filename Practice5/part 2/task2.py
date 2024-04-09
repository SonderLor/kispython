import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("data.txt", sep=";", header=None)
data_dict = dict()
for i in range(len(data)):
    if data.iloc[i, 3] != "не издана":
        if data.iloc[i, 1] not in data_dict:
            data_dict[data.iloc[i, 1]] = dict()
            data_dict[data.iloc[i, 1]][data.iloc[i, 3]] = 1
        else:
            if data.iloc[i, 3] not in data_dict[data.iloc[i, 1]]:
                data_dict[data.iloc[i, 1]][data.iloc[i, 3]] = 1
            else:
                data_dict[data.iloc[i, 1]][data.iloc[i, 3]] += 1
plots = list()
for game_genre, years in data_dict.items():
    x, y = list(), list()
    for year, n in years.items():
        x.append(year)
        y.append(n)
    plt.bar(x, y, label=game_genre)
plt.legend()
plt.show()
