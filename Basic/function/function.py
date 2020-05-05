# example of function use
# a and b are parameters, and 1 and 2 are arguments

def add(a, b):
    return a + b
sum = add(1, 2)
print(sum)

# function with no input

def hello_world():
    return 'hello_world'
string = hello_world()
print(string)

# function with no result

def subtract(a, b):  # first case
    print("the remainder of %d and %d is %d." % (a, b, a - b))
subtract(3, 4)

def subtract(a, b):  # second case
    print("the remainder of {0} and {1} is {2}.".format(a, b, a - b))
subtract(5, 6)

# parameter assignment call

def multiply(a, b):
    return a * b
double = multiply(a=7, b=8)
print(double)

# a function that takes multiple inputs

def add_many(*args):
    result = 0
    for data in args:
        result = result + data
    return result
sum = add_many(7, 8, 9)
print(sum)

# keyword parameters

def print_keyword(**keyword):
    print(keyword)
print_keyword(age=3)

# parameter initial value setting

def self_introduction(name='John'):
    print("my name is %s." % name)
self_introduction()

# a way to change variables inside functions outside functions

def add(a, b):
    a += 1
    b -= 1
    return a + b
sum = add(1, 2)
print(sum)

# lambda function

sum = lambda a, b: a + b
print(sum(3, 4))
