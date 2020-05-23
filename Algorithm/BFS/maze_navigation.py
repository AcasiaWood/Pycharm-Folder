n, m = map(int, input('미로의 가로와 세로를 입력하세요: ').split())
x, y = 0, 0
a, b = 0, 0
number = 0
maze = [[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]]
arrow = [[1, 0], [0, 1], [-1, 0], [0, -1]]
queue = [(0, 0, 0)]

for panel in maze:
    print(panel)

while len(queue) != 0:
    a, b, count = queue[0]
    for direct in arrow:
        x = a + direct[0]
        y = b + direct[1]
        if n > x >= 0 and m > y >= 0:
            if maze[x][y] == 1:
                if (x, y) not in queue:
                    queue.pop()
                    queue.append((x, y, count+1))
                    print(queue)
                    maze[x][y] = 0
                    print(x, y)
                    break
    if x == (n - 1) and y == (m - 1):
        break
print(count)
