# for loop: 2

a = list(map(int, input().split()))
n = int(input())
cases = []

for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        cnt = a[i]
        cnt += a[j]
        if cnt not in cases:
            cases.append(cnt)

if n in cases:
    print(True)
else:
    print(False)

# for loop: 1

a = list(map(int, input().split()))
dictionary = dict.fromkeys(a, True)
n = int(input())
b = n
flag = False

for i in range(0, len(a)):
    n = b
    n -= a[i]
    try:
        if dictionary[n] and n != a[i]:
            flag = True
            break
        else:
            flag = False
    except KeyError:
        flag = False

print(flag)