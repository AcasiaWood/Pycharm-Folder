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


for k in range(3):
    width = int(input())
    print("[Horizontal Line] width = {}".format(width))
    horizontal_line(width)
    print("")

for k in range(3):
    shift, height = map(int, input().split())
    print("[Vertical Line] shift = {}, height = {}".format(shift, height))
    vertical_line(shift, height)
    print("")

for k in range(3):
    height, width = map(int, input().split())
    print("[Two Vertical Lines] height = {}, width = {}".format(height, width))
    two_vertical_lines(height, width)
    print("")