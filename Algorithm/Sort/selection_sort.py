import random

sort = []

for i in range(10):
    sort.append(random.randint(1, 10))

for i in range(len(sort)):
    index = i
    for j in range(i, len(sort)):
        if sort[index] > sort[j]:
            index = j
    sort[i], sort[index] = sort[index], sort[i]

print(sort)
