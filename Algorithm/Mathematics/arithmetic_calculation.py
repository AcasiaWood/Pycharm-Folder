def addition(a, b):
    return a + b


def subtraction(a, b):
    return abs(a - b)


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


x, y = map(int, input().split())

print(addition(x, y))
print(subtraction(x, y))
print(multiplication(x, y))
print(division(x, y))
