import numpy as np
import matplotlib.pyplot as plt


def noise(width, height):
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    xx, yy = np.meshgrid(x, y)
    noise = np.sin(xx * 12.9898 + yy * 78.233) * 43758.5453
    noise = noise - np.floor(noise)
    return noise


white_noise = noise(50, 50)
plt.figure(figsize=(18, 6))
plt.plot(white_noise.ravel())
plt.title('Белый шум')
plt.show()
