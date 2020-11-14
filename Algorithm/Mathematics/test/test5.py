import random


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


def multiply(w):
    for i in range(w - 3, 0, -1):
        line = (" " * abs(i - 2)) + "*" + (" " * i * 2) + "*"
        print(line)
    for i in range(0, w - 2, 1):
        line = (" " * abs(i - 2)) + "*" + (" " * i * 2) + "*"
        print(line)


def divide(w):
    for i in range(0, w, 1):
        print((" " * i) + "*")


def check(r):
    if r == 1:
        number_1(width)
    elif r == 2:
        number_2(width)
    elif r == 3:
        number_3(width)
    elif r == 4:
        number_4(width)
    elif r == 5:
        number_5(width)
    elif r == 6:
        number_6(width)
    elif r == 7:
        number_7(width)
    elif r == 8:
        number_8(width)
    elif r == 9:
        number_9(width)


def check_answer(n1, n2, n3, o):
    global s1, s2, s3, s4
    if o == 1:
        if n1 + n2 == n3:
            print("Correct!\n")
            s1 += 1
            return True
        else:
            print("Incorrect!\n")
            return False
    elif o == 2:
        if n1 - n2 == n3:
            print("Correct!\n")
            s2 += 1
            return True
        else:
            print("Incorrect!\n")
            return False
    elif o == 3:
        if n1 * n2 == n3:
            print("Correct!\n")
            s3 += 1
            return True
        else:
            print("Incorrect!\n")
            return False
    elif o == 4:
        if n1 / n2 == n3:
            print("Correct!\n")
            s4 += 1
            return True
        else:
            print("Incorrect!\n")
            return False


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
    for i in range(w - 3):
        horizontal_line(w)
        two_vertical_lines(w - 4, w)
    horizontal_line(w)


def number_9(w):
    horizontal_line(w)
    two_vertical_lines(w - 4, w)
    horizontal_line(w)
    vertical_line(w - 1, w - 3)


s1 = 0
s2 = 0
s3 = 0
s4 = 0
add = 0
sub = 0
mul = 0
div = 0
add_e = 0
sub_e = 0
mul_e = 0
div_e = 0


while True:
    attempt = int(input("How many problems would you like to attempt?: "))
    if attempt > 0:
        break
    else:
        print("Invalid number!\n")

while True:
    width = int(input("How wide do you want your digits to be? 5-10: "))
    if 5 <= width <= 10:
        break
    else:
        print("Invalid number!\n")

while True:
    drill = str(input("Do you want to activate the drill mode? (y/n): "))
    if drill == "y":
        drill = True
        break
    elif drill == "n":
        drill = False
        break

print("")

for k in range(attempt):
    a = random.randint(1, 9)
    check(a)
    print("")
    operator = random.randint(1, 4)
    if operator == 1:
        plus(width)
        add += 1
    elif operator == 2:
        minus(width)
        sub += 1
    elif operator == 3:
        multiply(width)
        mul += 1
    elif operator == 4:
        divide(width)
        div += 1
    print("")
    b = random.randint(1, 9)
    if a % b != 0 and operator == 4:
        while True:
            b = random.randint(1, 9)
            if a % b == 0:
                break
    check(b)
    print("")
    while True:
        c = int(input("What is the answer?: "))
        flag = check_answer(a, b, c, operator)
        if drill:
            if flag:
                break
            else:
                if operator == 1:
                    add_e += 1
                elif operator == 2:
                    sub_e += 1
                elif operator == 3:
                    mul_e += 1
                elif operator == 4:
                    div_e += 1
                continue
        else:
            break

if s1 == 0:
    print("No addition problems presented\n")
else:
    print("Total addition problems presented: {}".format(add))
    if drill:
        if add_e == 0:
            print("# of extra attempts needed: {} (perfect!)\n".format(add_e))
        else:
            print("# of extra attempts needed: {}\n".format(add_e))
    else:
        print("Correct addition problems: {} ({})\n".format(s1, (s1 / add) * 100))

if s2 == 0:
    print("No subtraction problems presented\n")
else:
    print("Total addition problems presented: {}".format(sub))
    if drill:
        if sub_e == 0:
            print("# of extra attempts needed: {} (perfect!)\n".format(sub_e))
        else:
            print("# of extra attempts needed: {}\n".format(sub_e))
    else:
        print("Correct addition problems: {} ({})\n".format(s2, (s2 / sub) * 100))

if s3 == 0:
    print("No multiplication problems presented\n")
else:
    print("Total addition problems presented: {}".format(mul))
    if drill:
        if mul_e == 0:
            print("# of extra attempts needed: {} (perfect!)\n".format(mul_e))
        else:
            print("# of extra attempts needed: {}\n".format(mul_e))
    else:
        print("Correct addition problems: {} ({})\n".format(s3, (s3 / mul) * 100))

if s4 == 0:
    print("No division problems presented\n")
else:
    print("Total addition problems presented: {}".format(div))
    if drill:
        if div_e == 0:
            print("# of extra attempts needed: {} (perfect!)\n".format(div_e))
        else:
            print("# of extra attempts needed: {}\n".format(div_e))
    else:
        print("Correct addition problems: {} ({})\n".format(s4, (s4 / div) * 100))

print("You got {} out of {} points!".format(s1 + s2 + s3 + s4, attempt))