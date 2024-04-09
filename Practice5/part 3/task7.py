import pandas as pd
import matplotlib.pyplot as plt

statuses = pd.read_csv("statuses.csv", names=['task', 'variant', 'group', 'time', 'status', 'achievements'])

correct_statuses = statuses[statuses['status'].isin([0, 2, 5])]
task_correct_counts = correct_statuses['task'].value_counts()
sorted_tasks = task_correct_counts.sort_values(ascending=False)

sorted_tasks.plot(kind='bar')
plt.title('Количество правильных решений по задачам')
plt.xlabel('Задача')
plt.ylabel('Количество правильных решений')
plt.tight_layout()
plt.show()
