def sugar_braga():
    sugar = int(9)
    water = int(21)
    volume = water + sugar * 0.6
    alcohol_content = (sugar * 0.6) / volume * 100
    print(volume, "\t alcohol_content")


def alco(c, a):
    a = a + 5.7
    for i in range(1, c):
        a -= 0.3
    print(round(a, 2))

alco(15, 40)