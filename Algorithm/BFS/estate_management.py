# variable setting, arrow = [x, y]
import queue
estate = []
estate_count = []
estate_ = []
arrow = [[0, 1], [1, 0], [-1, 0], [0, -1]]
whole_estate = 0
flag = 0
leading = int(input())
q = queue.Queue()
a, b = 0, 0
x, y = 0, 0
# create estate
for i in range(leading):
    a = list(map(str, input().split()))
    estate_.append(a)
for i in range(leading):
    estate.append([])
print(estate_)
for i in range(len(estate_[0][0])):
    for j in range(leading):
        estate[i].append(int(estate_[i][i][j]))
        print(estate_[i][j])
# first, find list item which was named number one. (flag variable)
for i in range(0, len(estate)):
    for j in range(0, len(estate[0])):
        if estate[i][j] == 1:
            q.put((i, j))
            flag = 1
            break
    if flag == 1:
        break
# second, set x, y variable and keep these rules.
# index is not out of range, index is not on the place where computer went.
# index is not on the place where is number zero.
# after work, find list item again. (above coding)
count = 0
while not q.empty():
    a, b = q.get()
    for k in range(0, len(arrow)):
        x = a + arrow[k][0]
        y = b + arrow[k][1]
        if x < len(estate) and y < len(estate[0]) and x >= 0 and y >= 0:
            if estate[x][y] == 1:
                estate[x][y] = 0
                count = count + 1
                q.put((x, y))
    if q.empty():
        flag = 0
        estate_count.append(count)
        count = 0
        whole_estate = whole_estate + 1
        for i in range(0, len(estate)):
            for j in range(0, len(estate[0])):
                if estate[i][j] == 1:
                    q.put((i, j))
                    flag = 1
                    break
            if flag == 1:
                break
print(whole_estate)
for k in estate_count:
    print(k)
