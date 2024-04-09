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


def paint_func(x: float, y: float) -> Tuple[float, float, float]:
    r, g, b = 0.0, 0.0, 0.0
    pacman_center_x = 0.5
    pacman_center_y = 0.5
    pacman_radius = 0.4
    mouth_angle = math.pi / 6
    eye_radius = 0.065
    eye_offset_x = 0.15
    eye_offset_y = 0.25

    distance_to_center = math.sqrt((x - pacman_center_x) ** 2 + (y - pacman_center_y) ** 2)

    if distance_to_center <= pacman_radius:
        r, g, b = 1.0, 1.0, 0.0

    angle_to_point = math.atan2(y - pacman_center_y, x - pacman_center_x)
    if 0 <= angle_to_point <= mouth_angle or 0 >= angle_to_point >= -mouth_angle:
        r, g, b = 0.0, 0.0, 0.0

    eye_center_x = pacman_center_x + eye_offset_x
    eye_center_y = pacman_center_y - eye_offset_y
    distance_to_eye = math.sqrt((x - eye_center_x) ** 2 + (y - eye_center_y) ** 2)
    if distance_to_eye <= eye_radius:
        r, g, b = 0.0, 0.0, 0.0

    return r, g, b


label = tk.Label()
img = tk.PhotoImage(data=pyshader(paint_func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
