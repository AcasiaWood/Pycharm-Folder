prime_number = []
for i in range(2, 30):
    tried = 1
    for j in range(2, i+1):
        if i % j == 0:
            tried = tried + 1
    if tried == 2:
        prime_number.append(i)
print(prime_number)

n = int(input())
a = [False, False] + [True]*n
l = []
for i in range(2, n+1):
    if a[i] == True:
        l.append(i)
        for j in range(i, n+1, i):
            a[j] = False
print(i)
