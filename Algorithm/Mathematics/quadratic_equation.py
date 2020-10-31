import math

a, b, c = map(int, input('Enter the quadratic term coefficient, linear term coefficient, and constant term: ').split())
print('When calculated, the irrational square root is expressed as √.')

formula = b ** 2 - 4 * a * c

if formula < 0:
    print('Impossible to calculate.')
else:
    if math.sqrt(formula) ** 2 == formula:
        first_root = (-b + math.sqrt(formula)) / (2 * a)
        second_root = (-b - math.sqrt(formula)) / (2 * a)
        if first_root == second_root:
            print('multiple root = ' + str(first_root))
        else:
            print('roots = ' + str(first_root) + ' or ' + str(second_root))
    else:
        equation = '(' + str(b) + ' ± ' + '√' + str(formula) + ')' + ' / ' + str(2 * a)
        print('equation' + ' = ' + equation)
