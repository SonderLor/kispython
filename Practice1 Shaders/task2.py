import math
import tkinter as tk
from typing import Callable, Tuple


def pyshader(func: Callable, w: int, h: int):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def gaussian(x, y, center_x, center_y, radius):
    distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2
    sigma = radius * 0.4
    intensity = math.exp(-distance_squared / (2 * sigma ** 2))
    return intensity


def paint_func(x: float, y: float) -> Tuple[int, int, int]:
    r, g, b = 0, 0, 0
    red_circle_center_x = 0.53
    red_circle_center_y = 0.53
    green_circle_center_x = 0.47
    green_circle_center_y = 0.47
    circle_radius = 0.5
    r = gaussian(x, y, red_circle_center_x, red_circle_center_y, circle_radius)
    g = gaussian(x, y, green_circle_center_x, green_circle_center_y, circle_radius)

    r = max(0, min(1, r))
    g = max(0, min(1, g))

    return r, g, b


label = tk.Label()
img = tk.PhotoImage(data=pyshader(paint_func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
