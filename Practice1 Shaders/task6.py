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


def mix(x, y, a):
    return x * (1 - a) + y * a


def noise(x, y):
    return math.sin(x * 987654321 + y * 123456789) * 12345.12345 % 1


def val_noise(x, y):
    i = [int(x), int(y)]
    f = [x % 1, y % 1]
    a = noise(i[0], i[1])
    b = noise(i[0] + 1, i[1])
    c = noise(i[0], i[1] + 1)
    d = noise(i[0] + 1, i[1] + 1)
    u = [f[0] ** 2 * (3. - 2. * f[0]), f[1] ** 2 * (3. - 2. * f[1])]
    return mix(a, b, u[0]) + (c - a) * u[1] * (1.0 - u[0]) + \
           (d - b) * u[0] * u[1]


def fbm(vec):
    octaves = 6
    value = 0.0
    amplitude = .7
    for i in range(octaves):
        value += amplitude * val_noise(vec[0], vec[1])
        vec[0] *= 2.
        vec[1] *= 2.
        amplitude *= 0.5
    return value


def paint_func(x: float, y: float) -> Tuple[float, float, float]:
    scale = 3
    seed = 12100
    pos = [x * scale + seed, y * scale + seed]
    color = fbm(pos)
    return color, color, 1


label = tk.Label()
img = tk.PhotoImage(data=pyshader(paint_func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
