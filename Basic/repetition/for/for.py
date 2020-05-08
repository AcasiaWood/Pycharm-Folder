# typical for statement

fruit_list = ['apple', 'banana', 'peach']
for fruit in fruit_list:
    print(fruit)

# use of various for statements

coordinate = [(1, 2), (3, 4), (5, 6)]
for (first, second) in coordinate:
    print(first + second)

# for statement and continue

alphabets = ['a', 'b', 'c', 'd', 'e']
for alphabet in alphabets:
    if alphabet.isupper():
        continue
    print("%s is lowercase" % alphabet)

# for statement and break

alphabets = ['a', 'b', 'c', 'd', 'e']
for alphabet in alphabets:
    if not alphabet.isupper():
        break
    print("%s is uppercase" % alphabet)

# range function frequently used with for statement

number = range(10)  # set a range
print(number)

# example range function

data_list = [34, 53, 94, 21, 49]
for data in range(len(data_list)):  # the len function stands for the last data.
    print(data_list[data])

# using list nesting

numbers = [1, 2, 3, 4, 5]
result = [number * 2 for number in numbers]
print(result)
