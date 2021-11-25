from graph import *

winx = 1200
winy = 1000
windowSize(winx, winy)
canvasSize(winx, winy)
penColor('black')
r = g = b = 0


def room():
    """Рессует комнату"""

    brushColor(180, 150, 0)
    rectangle(0, 0, winx, 450)
    brushColor(150, 120, 0)
    rectangle(0, 450, winx, winy)


def windows(x, y):
    """Рессуем окно"""

    for i in range(1):
        brushColor(220, 255, 255)
        rectangle(x, y, x + 300, y + 400)
        brushColor(180, 240, 255)
        rectangle(x + 20, y + 20, x + 140, y + 160)
        rectangle(x + 160, y + 20, x + 280, y + 160)
        rectangle(x + 20, y + 180, x + 140, y + 380)
        rectangle(x + 160, y + 180, x + 280, y + 380)


def tail(x, y, Z, c):
    """Рессуем овалы под углом 45 градуссов"""

    penColor(c, c, c)
    brushColor(c, c, c)
    arc(x, y, x + Z, y + Z, 180, 270, [CHORD])
    arc(x - Z / 2, y + Z / 2, x + Z / 2, y + Z * 1.5, 0, 90, [CHORD])
    penColor('black')


def bobi(x, y, R):
    """Рессуем тело кота"""

    x1 = y1 = R

    def torso():
        """Рессуем туловище и хвост кота"""

        tail(x + x1 * 5.3, y - y1, R * 4, 192)
        penColor('black')
        brushColor(192, 192, 192)
        oval(x + x1, y + (y1 - y1), x + (x1 * 6), y + (y1 * 3))
        oval(x + x1, y + (y1 * 2.2), x + (x1 * 2.25), y + (y1 * 3))
        oval(x + x1, y + (y1 * 1.25), x + (x1 * 0.2), y + (y1 * 2.5))
        circle(x + x1, y + (y1 * 1.2), R)
        circle(x + x1 * 5.5, y + (y1 * 2.22), R / 5 * 4)
        oval(x + (x1 * 6), y + (y1 * 2.25), x + (x1 * 6.5), y + (y1 * 3.5))

    torso()

    def ears():
        """Рессуем уши кота"""

        r = g = b = 0

        polygon([(x + x1 - x1, y + y1 * 0.2), (x + x1 * 0.52, y + y1 * 0.375), (x + x1 * 0.18, y + y1 * 0.73),
                 (x + x1 - x1, y + y1 * 0.2)])
        polygon([(x + x1 * 1.944, y + y1 * 0.2), (x + x1 * 1.416, y + y1 * 0.375), (x + x1 * 1.77, y + y1 * 0.728),
                 (x + x1 * 1.944, y + y1 * 0.2)])
        brushColor(r + 220, g + 220, b + 220)
        polygon([(x + x1 * 0.075, y + y1 * 0.275), (x + x1 * 0.432, y + y1 * 0.394), (x + x1 * 0.196, y + y1 * 0.634),
                 (x + x1 * 0.075, y + y1 * 0.275)])
        polygon([(x + x1 * 1.86, y + y1 * 0.275), (x + x1 * 1.504, y + y1 * 0.394), (x + x1 * 1.74, y + y1 * 0.634),
                 (x + x1 * 1.86, y + y1 * 0.275)])

    ears()

    def eyes():
        """Рессуем глаза кота"""

        R1 = R / 3
        x2 = x1
        y2 = y1

        for i in range(2):
            brushColor(r + 180, g + 255, b)
            circle(x + x2 * 0.5, y + y2 * 1.1, R1)
            brushColor(r, g, b)
            oval(x + x2 * 0.5, y + y2 * 0.82, x + (x2 / 2 + x1 / 8), y + y2 * 1.375)
            tail(x + x1 / 3, y + y1 / 1.57, R1, 255)
            tail(x + x1 + R1, y + y1 / 1.57, R1, 255)
            x2 += x1 * 2

    eyes()

    def nose():
        """Рессуем нос и усы"""

        brushColor(r + 220, g + 220, b + 220)
        polygon([(x + x1, y + y1 * 1.75), (x + x1 * 0.89, y + y1 * 1.6), (x + x1 * 1.11, y + y1 * 1.6),
                 (x + x1, y + y1 * 1.75)])
        line(x + x1, y + y1 * 1.75, x + x1, y + y1 * 1.87)
        penColor('black')
        arc(x + x1, y + y1 * 1.75, x + x1 * 0.75, y + y1 * 2.025, 0, -110, [ARC])
        arc(x + x1, y + y1 * 1.75, x + x1 * 1.25, y + y1 * 2.025, 180, 290, [ARC])
        y2 = y1 * 1.5

        for i in range(3):
            arc(x - x1 * 0.6, y + y2, x + x1 * 0.8, y + y1 * 2.2, 10, 120, [ARC])
            arc(x + x1 * 1.2, y + y2, x + x1 * 2.6, y + y1 * 2.2, 170, 60, [ARC])
            y2 += y2 * 0.066

    nose()


room()

windows(850, 20)
bobi(50, 500, 60)

run()
