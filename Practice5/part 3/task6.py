import pandas as pd
import matplotlib.pyplot as plt

statuses = pd.read_csv("statuses.csv", names=['task', 'variant', 'group', 'time', 'status', 'achievements'])
"""
    Submitted = 0
    Checked = 2
    Failed = 3
    NotSubmitted = 4
    CheckedSubmitted = 5
    CheckedFailed = 6
"""
correct_statuses = statuses[statuses['status'].isin([0, 2, 5])]
group_correct_counts = correct_statuses['group'].value_counts()

group_correct_counts.plot(kind='bar')
plt.title('Количество правильных решений по группам')
plt.xlabel('Группа')
plt.ylabel('Количество правильных решений')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
