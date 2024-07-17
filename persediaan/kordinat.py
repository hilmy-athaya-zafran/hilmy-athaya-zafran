def gotoxy(x=0, y=0, user_string="Teks Default"):
    x = int(x)
    y = int(y)
    if x >= 255: x = 255
    if y >= 255: y = 255
    if x < 0: x = 0
    if y < 0: y = 0

    horiz = str(x)
    vert = str(y)
    # plot user_string pada posisi horiz,vert
    print(f"\033[{vert};{horiz}f{user_string}")

def myinput(x=0, y=0, user_string="Teks Default"):
    x = int(x)
    y = int(y)
    if x >= 255: x = 255
    if y >= 255: y = 255
    if x < 0: x = 0
    if y < 0: y = 0

    horiz = str(x)
    vert = str(y)
    # plot user_string pada posisi horiz,vert
    teks = input(f"\033[{vert};{horiz}f{user_string}")
    return teks

def mycenter(brs, teks):
    kolcenter = int((100 - len(teks)) / 2)
    gotoxy(kolcenter, brs, teks)

# Contoh penggunaan

