# variable setting, arrow = [x, y]
# create estate
def create_estate():
    for i in range(leading):
        a = list(map(int, raw_input().split()))
        estate.append(a)
    return estate
# first, find list item which was named number one. (flag variable)
def find_item(estate):
    for i in range(0, len(estate)):
        for j in range(0, len(estate[0])):
            if estate[i][j] == 1:
                q.put((i, j))
                flag = 1
                break
        if flag == 1:
            break
    return q
# second, set x, y variable and keep these rules.
# index is not out of range, index is not on the place where computer went.
# index is not on the place where is number zero.
# after work, find list item again. (above coding)
def working(q, estate, whole_estate):
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
    for k in range(0, len(estate_count)):
        print(estate_count[k])
import Queue
estate = []
estate_count = []
arrow = [[0, 1], [1, 0], [-1, 0], [0, -1]]
whole_estate = 0
flag = 0
leading = input()
q = Queue.Queue()
a, b = 0, 0
x, y = 0, 0
estate = create_estate()
q = find_item(estate)
working(q, estate, whole_estate)
