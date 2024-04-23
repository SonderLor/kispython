from pathlib import Path
import tkinter as tk

SCALE_X = 6
SCALE_Y = 4

COLORS = [
    (0, 0, 0),
    (0, 0, 168),
    (0, 168, 0),
    (0, 168, 168),
    (168, 0, 0),
    (168, 0, 168),
    (168, 84, 0),
    (168, 168, 168),
    (84, 84, 84),
    (84, 84, 252),
    (84, 252, 84),
    (84, 252, 252),
    (252, 84, 84),
    (252, 84, 252),
    (252, 252, 84),
    (252, 252, 252)
]


def draw_line(coords, color_index, canvas):
    canvas.create_line(*[(x * SCALE_X, y * SCALE_Y) for x, y in coords],
                       fill='#%02x%02x%02x' % COLORS[color_index], width=4)


def draw(pic, canvas):
    b = bytearray(pic)
    codes = [hex(i) for i in b]

    def conv(n):
        return int(n, 16)

    color = 0
    can_draw = False
    commands = []

    for code in codes:
        if conv(code) >= 0xf0 and len(commands) != 0:
            action = conv(commands[0])
            match (action):
                case 0xf0:
                    color = conv(commands[1])
                    can_draw = True
                case 0xf1:
                    can_draw = False
                case 0xf2:
                    pass
                case 0xf3:
                    pass
                case 0xf4:
                    x = conv(commands[1])
                    y = conv(commands[2])
                    coords = [(x, y)]
                    is_y = True

                    for i in range(3, len(commands)):
                        if is_y:
                            y = conv(commands[i])
                        else:
                            x = conv(commands[i])
                        is_y = not is_y
                        coords.append((x, y))

                    draw_line(coords, color, canvas)
                case 0xf5:
                    x = conv(commands[1])
                    y = conv(commands[2])
                    coords = [(x, y)]
                    is_y = False

                    for i in range(3, len(commands)):
                        if is_y:
                            y = conv(commands[i])
                        else:
                            x = conv(commands[i])
                        is_y = not is_y
                        coords.append((x, y))

                    draw_line(coords, color, canvas)
                case 0xf6:
                    if len(commands) % 2 == 1 and len(commands) >= 5 and can_draw:
                        coords = [(conv(commands[1]), conv(commands[2]))]
                        for i in range(3, len(commands), 2):
                            coords.append((conv(commands[i]), conv(commands[i + 1])))
                        draw_line(coords, color, canvas)
                case 0xf7:
                    if len(commands) >= 4 and can_draw:
                        x = conv(commands[1])
                        y = conv(commands[2])
                        coords = [(x, y)]

                        for i in range(3, len(commands)):
                            x_add = (conv(commands[i]) >> 4) & 7
                            x_s = -1 if conv(commands[i]) >> 7 == 1 else 1
                            y_add = conv(commands[i]) & 7
                            y_s = -1 if (conv(commands[i]) & 8) >> 3 == 1 else 1

                            x += x_s * x_add
                            y += y_s * y_add
                            coords.append((x, y))

                        draw_line(coords, color, canvas)
                case 0xf8:
                    pass
                case 0xf9:
                    pass

            commands.clear()
        commands.append(code)


def main():
    pic = Path('data/PIC.2').read_bytes()
    canvas = tk.Canvas(width=160 * SCALE_X, height=170 * SCALE_Y)
    canvas.pack()
    draw(pic, canvas)
    tk.mainloop()


if __name__ == "__main__":
    main()
