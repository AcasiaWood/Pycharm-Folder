def factorial(a, b, value):
    if a - b > 0:
        a -= b
        value *= a
        return factorial(a, b, value)
    else:
        return value


formula = str(input())
cnt = formula.count('!')
number = int(formula.split('!')[0])
result = factorial(a=number, b=cnt, value=number)
print(result)
