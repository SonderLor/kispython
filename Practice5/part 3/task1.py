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

messages['time'] = pd.to_datetime(messages['time'])
messages['day_of_week'] = messages['time'].dt.day_name()
activity_by_day = messages['day_of_week'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

activity_by_day.plot(kind='bar')
plt.title('Распределение активности студентов по дням недели')
plt.xlabel('День недели')
plt.ylabel('Количество записей')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
