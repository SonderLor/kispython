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


def paint_func(x: float, y: float) -> Tuple[int, int, int]:
    if 0.1 < x < 0.9 and 0.1 < y < 0.9:
        return 0, 0, 0
    return 1, 1, 1


label = tk.Label()
img = tk.PhotoImage(data=pyshader(paint_func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
