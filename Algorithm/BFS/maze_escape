import queue
x, y = 0, 0
move = 1
maze = [[1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1]]
for i in range(len(maze)):
    print(maze[i])
arrow = [[0, 1], [1, 0], [0, -1], [-1, 0]]
a, b = 0, 0
q = queue.Queue()
q.put((0, 0, move))
n, m = map(int, input().split())
while not q.empty():
    a, b, move = q.get()
    for i in range(4):
        x = a + arrow[i][0]
        y = b + arrow[i][1]
        if x == n-1 and y == m-1:
            move = move+1
            break
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            if maze[x][y] == 1:
                maze[0][0] = 0
                maze[x][y] = 0
                q.put((x, y, move+1))
print(move)
