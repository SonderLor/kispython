import requests
import re


url = "https://kispython.ru/"
req = requests.get("{url}".format(url=url))
text = req.text
groups = re.findall(r"И[ВКМН]БО-\d\d-22", text)
k = 0
for i, group in enumerate(groups):
    if i != 0 and groups[i - 1][1] != group[1]:
        k = 1
        print("\n\n" + group, end=" ")
        continue
    if k == 10:
        k = 0
        print()
    k += 1
    print(group, end=" ")
