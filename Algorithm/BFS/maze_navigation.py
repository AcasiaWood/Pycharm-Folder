from collections import deque

a, b = map(int, input().split())

visit = [list(map(int, input())) for _ in range(a)]
count = [[0] * b for _ in range(a)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q = deque()

q.append((0, 0))

while q:
    nx, ny = q.popleft()
    for m in move:
        mx = nx + m[0]
        my = ny + m[1]
        if 0 <= mx < a and 0 <= my < b and visit[mx][my] == 1:
            visit[mx][my] = 0
            count[mx][my] = count[nx][ny] + 1
            q.append((mx, my))

print(count[a - 1][b - 1] + 1)
