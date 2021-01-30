a = [3, 2, 1, 5, 6, 8, 3]
n = 14
s = []
cnt = 0

for i in range(10):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

for i in range(0, len(a) - 1):
    cnt = a[i]
    length = 1
    for j in range(i + 1, len(a)):
        cnt += a[j]
        length += 1
        if cnt >= n:
            print(cnt, length)
            s.append(length)
print(s)