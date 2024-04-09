import pandas as pd
import matplotlib.pyplot as plt

statuses = pd.read_csv("statuses.csv", names=['task', 'variant', 'group', 'time', 'status', 'achievements'])
group_achievements = statuses.groupby('group')['achievements'].apply(lambda x: sum(len(eval(a)) for a in x))

group_achievements.plot(kind='bar')
plt.title('Общее количество достижений по группам')
plt.xlabel('Группа')
plt.ylabel('Общее количество достижений')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
