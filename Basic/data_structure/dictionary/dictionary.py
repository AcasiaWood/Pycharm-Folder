# create dictionary

countries = {'korea': '대한민국', 'united kingdom': '영국', 'india': '인도'}
print(countries)

# add dictionary value

numbers = {1: -1, 2: -2, 3: -3}
a[4] = -4
print(numbers)

# delete dictionary value

multiple = {1: 2, 2: 4, 3: 6}
del multiple[1]
print(multiple)

# get key and value

fruits = ['apple': '사과', 'orange': '오랜지', 'pineapple': '파인애플']
print(fruits['apple'])
print(fruits['사과'])

# get all keys and values

vegetables = ['carrot': '당근', 'potato': '감자', 'corn': '옥수수']
print(vegetables.keys())
print(vegetables.values())

# clear dictionary value

numbers = {1: 2, 3: 4, 5: 6}
numbers.clear()
print(numbers)
