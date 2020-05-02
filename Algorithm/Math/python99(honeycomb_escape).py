# formula a(n) = a(n-1) + 6*n
room = int(input())
a = 1
n = 1
while a < room:
    a = a + 6*n
    n += 1
print(n)