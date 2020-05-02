import queue
width, height = map(int, input().split())
farm = []
arrow = [[0, 1], [1, 0], [0, -1], [-1, 0]]
save = []
day = 0
flag = 0
q = queue.Queue()
for i in range(height):
    a = list(map(int, input().split()))
    farm.append(a)
for i in range(0, height):
    for j in range(0, width):
        if farm[i][j] == 1:
            q.put((i, j, day))
while not q.empty():
    a, b, day = q.get()
    for i in range(0, 4):
        x = a + arrow[i][0]
        y = b + arrow[i][1]
        if 0 <= x < len(farm) and 0 <= y < len(farm[0]):
            if farm[x][y] == 0:
                farm[x][y] = 1
                q.put((x, y, day+1))
for i in range(0, height):
    for j in range(0, width):
        if farm[i][j] == 0:
            flag = 1
            break
    if flag == 0:
        print(day)
        break
    elif flag == 1:
        print(-1)
        break
