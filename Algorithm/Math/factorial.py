def factorial_function(a, b, value):
    if a - b > 0:
        a -= b
        value *= a
        return factorial_function(a, b, value)
    else:
        return value

formula = str(input())
factorial = formula.count('!')
number = int(formula.split('!')[0])
result = factorial_function(a=number, b=factorial, value=number)
print(result)
