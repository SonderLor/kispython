import matplotlib.pyplot as plt
import math
from decimal import Decimal

k = [6, 0, -4 - 3, 5, 6, -6, -13, 7, 44, 64, 44, 7, -13, -6, 6, 5, -3, -4, 0, 6]


def float_range(start, stop, step):
    while start <= stop:
        yield round(start, 12)
        start += step


omega_list = list(float_range(Decimal(0.1), Decimal(2 + 0.1), Decimal(0.1)))

ex_list = []
for omega in omega_list:
    for t in range(1, 100):
        y = 0
        for b in range(0, 20):
            x = round(1000 * math.sin(omega * (t + b)))
            y += x * k[b]
        ex_list.append(y)

plt.figure(figsize=(18, 6))
plt.plot(ex_list)
plt.show()
