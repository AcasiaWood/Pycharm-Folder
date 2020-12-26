a = [(1, 1), (2, 2), (3, 3)]
b = [(3, 5), (9, 2), (1, 8)]
x, y = 0, 0
coordination = []

for i in range(len(a)):
    coordination.append([])
    
for i in range(len(a)):
    for j in range(len(b)):
        if a[j][0] >= b[j][0]:
            x = a[j][0] - b[j][0]
        elif a[j][0] <= b[j][0]:
            x = b[j][0] - a[j][0]
        if a[j][1] >= b[j][1]:
            y = a[j][1] - b[j][1]
        elif a[j][1] <= b[j][1]:
            y = b[j][1] - a[j][1]
        coordination[i].append((x, y))
    if i == len(coordination) - 1:
        break
    temp = a[i]
    a[i] = a[i + 1]
    a[i + 1] = temp
    
print(min(coordination))
