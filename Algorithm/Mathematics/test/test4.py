def check_answer(a, b, c, o):
    a = int(a)
    b = int(b)
    c = int(c)
    if o == "+":
        if a + b == c:
            return True
        else:
            return False
    elif o == "-":
        if a - b == c:
            return True
        else:
            return False


for i in range(4):
    a1, b1, c1, o1 = map(str, input().split())
    print(check_answer(a1, b1, c1, o1))