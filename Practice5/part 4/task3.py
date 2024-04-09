from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
import random

colors = ["#000000", "#1D2B53", "#7E2553", "#008751",
          "#AB5236", "#5F574F", "#C2C3C7", "#FFF1E8",
          "#FF004D", "#FFA300", "#FFEC27", "#00E436",
          "#29ADFF", "#83769C", "#FF77A8", "#FFCCAA"]
my_cmap = ListedColormap(colors, name="PICO-8")


def draw_sprite(canvas, x, y):
    pallete = random.choices([i for i in range(1, 16)], k=COLORS)
    pallete.insert(0, 0)

    for i in range(SIZE):
        for j in range(int(np.ceil(SIZE / 2))):
            canvas[x + i][y + j] = pallete[np.random.randint(COLORS + 1)]
            canvas[x + i][y + SIZE - j - 1] = canvas[x + i][y + j] if j < np.ceil(SIZE / 2) else canvas[x + i][y + j]


SIZE = 5
MARGIN = 5
WIDTH = 10
LENGHT = 20
COLORS = 3

SCREEN_WIDTH = WIDTH * SIZE + MARGIN * (WIDTH - 1) + 4
SCREEN_LENGTH = LENGHT * SIZE + MARGIN * (LENGHT - 1) + 4

canvas = np.zeros((SCREEN_WIDTH, SCREEN_LENGTH))

for x in range(2, SCREEN_WIDTH, SIZE + MARGIN):
    for y in range(2, SCREEN_LENGTH, SIZE + MARGIN):
        draw_sprite(canvas, x, y)

plt.imshow(canvas, cmap=my_cmap, interpolation='nearest')
plt.axis('off')
plt.show()
