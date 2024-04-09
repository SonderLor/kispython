import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


messages = pd.read_csv("messages.csv")
messages.columns = ['id', 'task', 'variant', 'group', 'time']

checks = load_csv('checks.csv')
statuses = load_csv('statuses.csv')

task_counts = messages['task'].value_counts().sort_index()
plt.bar(task_counts.index, task_counts.values)
plt.xlabel('Задачи')
plt.ylabel('Попытки')
plt.show()
