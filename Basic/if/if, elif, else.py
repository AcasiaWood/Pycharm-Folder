# if, elif, else

ticket = True
if ticket:
    print('You have a ticket.')
else:
    print('You don`t have a ticket.')

# comparison operator
# x < y	: x is less than y.
# x > y	: x is greater than y.
# x == y : x is equal to y
# x != y : x is not equal to y
# x >= y : x is greater than or equal to y.
# x <= y : x is less than or equal to y.

# operator
# x or y : even if only one of x and y is true, it is true
# x and y : both x and y must be true
# not x	: true if x is false

# in, not in
# x in list	: x not in list
# x in tuple : x not in tuple
# x in string : x not in string

# elif to judge various conditions

bag = ['laptop', 'cellphone']
if 'desktop' in bag:
    print('You have a desktop.')
elif 'laptop' in bag:
    print('You have a laptop.')
else:
    print('You don`t have any computer.')

# writing conditional statements in one line

pocket = ['key', 'watch']
if 'key' in pocket: pass
else: print('The door cannot be opened.')
