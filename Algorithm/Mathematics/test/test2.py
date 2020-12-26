def horizontal_line(w):
    line = ""
    for i in range(w):
        line += "*"
    print(line)


def vertical_line(s, h):
    for i in range(h):
        print((s * " ") + "*")


def two_vertical_lines(h, w):
    line = "*"
    for i in range(w - 2):
        line += " "
    line += "*"
    for j in range(h):
        print(line)


def number_0(w):
    horizontal_line(w)
    two_vertical_lines(w - 2, w)
    horizontal_line(w)


def number_1(w):
    vertical_line(w - 1, w)


def number_2(w):
    horizontal_line(w)
    vertical_line(w - 1, w - 4)
    horizontal_line(w)
    for i in range(w - 4):
        print("*")
    horizontal_line(w)


def number_3(w):
    horizontal_line(w)
    vertical_line(w - 1, w - 4)
    horizontal_line(w)
    for i in range(w - 4):
        print((w - 1) * " " + "*")
    horizontal_line(w)


def number_4(w):
    two_vertical_lines(w - 3, w)
    horizontal_line(w)
    vertical_line(w - 1, w - 3)


def number_5(w):
    horizontal_line(w)
    for i in range(w - 4):
        print("*")
    horizontal_line(w)
    for i in range(w - 4):
        print((w - 1) * " " + "*")
    horizontal_line(w)


def number_6(w):
    horizontal_line(w)
    for i in range(w - 4):
        print("*")
    horizontal_line(w)
    two_vertical_lines(w - 4, w)
    horizontal_line(w)


def number_7(w):
    horizontal_line(w)
    vertical_line(w - 1, w - 1)


def number_8(w):
    for i in range(w - 4):
        horizontal_line(w)
        two_vertical_lines(w - 4, w)
    horizontal_line(w)


def number_9(w):
    horizontal_line(w)
    two_vertical_lines(w - 4, w)
    horizontal_line(w)
    vertical_line(w - 1, w - 3)


width = 6
number_0(width)
print("")
number_1(width)
print("")
number_2(width)
print("")
number_3(width)
print("")
number_4(width)
print("")
number_5(width)
print("")
number_6(width)
print("")
number_7(width)
print("")
number_8(width)
print("")
number_9(width)