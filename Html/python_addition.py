case = int(input())
num_list = [1, 2, 4]
_list = []
num = 0
a = 0
for i in range(case):
    n = int(input())
    _list.append(n)
for i in range(max(_list)):
    num = 0
    for j in range(a, len(num_list)):
        num += num_list[j]
    num_list.append(num)
    a += 1
for i in range(case):
    print(num_list[_list[i]-1])