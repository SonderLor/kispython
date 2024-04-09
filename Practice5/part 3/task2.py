import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


def time_of_day(hour):
    if 5 <= hour < 12:
        return 'Утро'
    elif 12 <= hour < 18:
        return 'День'
    elif 18 <= hour < 24:
        return 'Вечер'
    else:
        return 'Ночь'


messages = pd.read_csv("messages.csv")
messages.columns = ['id', 'task', 'variant', 'group', 'time']

checks = load_csv('checks.csv')
statuses = load_csv('statuses.csv')
messages['time'] = messages['time'].apply(parse_time)
messages['time_of_day'] = messages['time'].dt.hour.apply(time_of_day)

activity_by_time_of_day = messages['time_of_day'].value_counts().reindex(['Утро', 'День', 'Вечер', 'Ночь'])

activity_by_time_of_day.plot(kind='bar', color='skyblue')
plt.title('Распределение активности студентов по времени суток')
plt.xlabel('Время суток')
plt.ylabel('Количество записей')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
