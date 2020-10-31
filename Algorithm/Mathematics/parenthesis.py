# Baekjoon

def check(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        elif string[i] == ')':
            try:
                stack.pop()
            except IndexError:
                return 'NO'
    if len(stack):
        return 'NO'
    else:
        return 'YES'

case = int(input())
result = []

while case:
    parenthesis = str(input())
    result.append(check(parenthesis))
    case -= 1

for i in result:
    print(i)
