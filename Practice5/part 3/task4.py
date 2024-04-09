import pandas as pd
import matplotlib.pyplot as plt

messages = pd.read_csv("messages.csv")
messages.columns = ['id', 'task', 'variant', 'group', 'time']

messages['time'] = pd.to_datetime(messages['time'])
messages['week_number'] = messages['time'].dt.isocalendar().week
activity_by_task_week = messages.groupby(['task', 'week_number']).size().unstack(fill_value=0)

activity_by_task_week.T.plot(kind='bar')
plt.title('Изменение активности студентов по задачам в течение семестра')
plt.xlabel('Неделя семестра')
plt.ylabel('Количество сообщений')
plt.legend(title='Задача', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
