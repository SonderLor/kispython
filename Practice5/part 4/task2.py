import numpy as np
import matplotlib.pyplot as plt


def draw_sprite(canvas, x, y, colors):
    for i in range(SIZE):
        for j in range(int(np.ceil(SIZE / 2))):
            canvas[x + i][y + j] = np.random.randint(0, colors)
            canvas[x + i][y + 4 - j] = canvas[x + i][y + j] if j < 3 else canvas[x + i][y + j]


SIZE = 5
MARGIN = 5
WIDTH = 10
LENGTH = 20

SCREEN_WIDTH = WIDTH * SIZE + MARGIN * (WIDTH - 1) + 4
SCREEN_LENGTH = LENGTH * SIZE + MARGIN * (LENGTH - 1) + 4

canvas = np.ones((SCREEN_WIDTH, SCREEN_LENGTH))

for x in range(2, SCREEN_WIDTH, SIZE + MARGIN):
    for y in range(2, SCREEN_LENGTH, SIZE + MARGIN):
        draw_sprite(canvas, x, y, 2)

plt.imshow(canvas, cmap='Greys', interpolation='nearest')
plt.axis('off')
plt.show()
