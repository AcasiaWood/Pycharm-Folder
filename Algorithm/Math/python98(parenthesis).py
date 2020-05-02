def check_parenthesis(parenthesis_string):
    stack = []
    for i in range(len(parenthesis_string)):
        if parenthesis_string[i] == '(':
            stack.append(parenthesis_string[i])
        elif parenthesis_string[i] == ')':
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
    result.append(check_parenthesis(parenthesis))
    case -= 1

for i in result:
    print(i)