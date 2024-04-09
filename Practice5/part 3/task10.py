import pandas as pd
import matplotlib.pyplot as plt


statuses = pd.read_csv('statuses.csv', names=['task', 'variant', 'group', 'time', 'status', 'achievements'])

statuses['achievements_str'] = statuses['achievements'].apply(str)
group_variety = statuses.groupby(['group', 'task'])['achievements_str'].apply(lambda x: len(set(x)))

average_variety = group_variety.groupby('group').mean()
sorted_groups = average_variety.sort_values(ascending=False)

sorted_groups.plot(kind='bar')
plt.title('Среднее количество различных способов решения задач по группам')
plt.xlabel('Группа')
plt.ylabel('Среднее количество различных способов')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
