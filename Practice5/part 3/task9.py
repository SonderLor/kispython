import pandas as pd
import matplotlib.pyplot as plt

statuses = pd.read_csv("statuses.csv", names=['task', 'variant', 'group', 'time', 'status', 'achievements'])
student_ratings = statuses.groupby(['group', 'variant'])['achievements'].apply(lambda x: sum(len(eval(a)) for a in x))

top_10_students = student_ratings.nlargest(10)

top_10_students.plot(kind='bar')
plt.title('Топ 10 студентов')
plt.xlabel('Студенты')
plt.ylabel('Рейтинг')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
