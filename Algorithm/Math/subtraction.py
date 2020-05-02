a_location = [(1, 1), (2, 2), (3, 3)]
b_location = [(1, 1), (2, 2), (3, 3)]
for i in range(3):
    a = a_location[0]
    b = a_location[2]
    a_location[0] = b
    a_location[2] = a
