a = [(1, 1), (2, 2), (3, 3)]
b = [(3, 5), (9, 2), (1, 8)]
sort = a
num1 = 0
num2 = 0
x = 0
y = 0
col_list = []
for i in range(len(a)):
    col_list.append([])
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[j][0] >= b[j][0]:
            x = a[j][0] - b[j][0]
        elif a[j][0] <= b[j][0]:
            x = b[j][0] - a[j][0]
        if a[j][1] >= b[j][1]:
            y = a[j][1] - b[j][1]
        elif a[j][1] <= b[j][1]:
            y = b[j][1] - a[j][1]
        col_list[i].append((x, y))
    if i == len(col_list)-1:
        break
    num1 = a[i]
    num2 = a[i+1]
    a[i] = num2
    a[i+1] = num1
print(min(col_list))