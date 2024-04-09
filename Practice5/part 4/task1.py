import numpy as np
import matplotlib.pyplot as plt

sprite = np.random.randint(0, 2, (5, 5))
symmetric_sprite = np.zeros((5, 5))

for i in range(5):
    for j in range(5):
        symmetric_sprite[i][4 - j] = sprite[i][j] if j < 3 else symmetric_sprite[i][j]

plt.imshow(symmetric_sprite, cmap='Greys', interpolation='nearest')
plt.axis('off')
plt.show()
