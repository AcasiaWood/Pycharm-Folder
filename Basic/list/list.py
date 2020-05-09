# a way to use a list

numbers = [1, 2, 3]

# list indexing

grades = [93, 48, 64]
print(grades[0])

# list slicing

toys = ['car', 'robot', 'block']
print(toys[0:2])

# add list

prime_numbers = [2, 3, 5]
synthetic_numbers = [4, 6, 8]
print(prime_numbers + synthetic_numbers)

# multiply list

alphabets = ['a', 'b', 'c']
print(alphabets * 3)

# find list length

marks = ['!', '@', '#']
print(len(marks))

# delete list values

languages = ['korean', 'chinese', 'english']
del languages[1]

# add list element

coordinate = [(1, 2), (3, 4), (5, 6)]
coordinate.append((7, 8))

# sort list

numbers = [3, 7, 1, 5]
numbers.sort()

# reverse list

characters = ['a', 'b', 'c']
characters.reverse()

# return position

numbers = [1, 2, 3]
print(numbers.index(2))

# insert element into list

numbers = [1, 2, 3]
numbers.insert(0, 3)

# count the number of elements x in the list

alphabets = ['a', 'b', 'c', 'd', 'e']
print(alphabets.count('a'))
