def bubble_sort(sort):
    for i in range(len(sort)):
        for j in range(len(sort) - 1):
            if sort[j] > sort[j + 1]:
                sort[j], sort[j + 1] = sort[j + 1], sort[j]
    return sort


def selection_sort(sort):
    for i in range(len(sort)):
        index = i
        for j in range(i, len(sort)):
            if sort[index] > sort[j]:
                index = j
        sort[i], sort[index] = sort[index], sort[i]
    return sort


def insertion_sort(sort):
    for i in range(1, len(sort)):
        for j in range(i, 0, -1):
            if sort[j] < sort[j - 1]:
                sort[j], sort[j - 1] = sort[j - 1], sort[j]
    return sort


array = []

for i in range(10):
    factor = int(input())
    array.append(factor)

array = bubble_sort(array)
print("bubble sort = {}".format(array))
array = selection_sort(array)
print("selection sort = {}".format(array))
array = insertion_sort(array)
print("insertion sort = {}".format(array))
