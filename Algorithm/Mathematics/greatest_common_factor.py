# gcf

a, b = map(int, input().split())
a_list = []
b_list = []
result = []
for i in range(1, a+1):
    if a % i == 0:
        a_list.append(i)
for j in range(1, b+1):
    if b % j == 0:
        b_list.append(j)
print(a_list, b_list)
for n in a_list:
    for m in b_list:
        if n == m and n != 1 and m != 1:
            result.append(n)
print(result)
