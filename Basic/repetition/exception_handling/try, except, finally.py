# error exception handling techniques

vegetable_list = ['carrot', 'cabbage', 'cucumber', 'onion', 'tomato']
try:
    print(vegetable_list[5])
except IndexError:
    print('vegetable does not exist.')
finally:
    print('add vegetables')

# intentional error

raise Exception
