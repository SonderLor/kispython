import pandas as pd
import matplotlib.pyplot as plt


messages = pd.read_csv("messages.csv")
messages.columns = ['id', 'task', 'variant', 'group', 'time']

group_message_counts = messages['group'].value_counts()

group_message_counts.plot(kind='bar')
plt.title('Количество сообщений по группам')
plt.xlabel('Группа')
plt.ylabel('Количество сообщений')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
