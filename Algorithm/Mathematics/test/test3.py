def horizontal_line(w):
    line = ""
    for i in range(w):
        line += "*"
    print(line)


def vertical_line(s, h):
    for i in range(h):
        print((s * " ") + "*")


def plus(w):
    vertical_line(w - 3, w - 3)
    horizontal_line(w)
    vertical_line(w - 3, w - 3)


def minus(w):
    for i in range(w - 3):
        print("")
    horizontal_line(w)
    for i in range(w - 3):
        print("")


plus(5)
print("")
minus(5)