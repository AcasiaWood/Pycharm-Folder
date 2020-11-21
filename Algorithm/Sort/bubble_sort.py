import random

sort = []

for i in range(10):
    sort.append(random.randint(1, 10))

for i in range(len(sort)):
    for j in range(len(sort) - 1):
        if sort[j] > sort[j + 1]:
            sort[j], sort[j + 1] = sort[j + 1], sort[j]

print(sort)
