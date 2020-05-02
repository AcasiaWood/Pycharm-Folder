result = [[], [], [], [], []]
add = 0
for i in range(0, 5):
    a, b, c, d = map(int, raw_input().split())
    add = a + b + c + d
    result[i].append(add)
print(result)
max_value = result[0]
for j in range(0, len(result)):
    if max_value < result[j]:
        max_value = result[j]
print(max[0])