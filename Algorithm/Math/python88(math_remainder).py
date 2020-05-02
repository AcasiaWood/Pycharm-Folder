remainder_list = []
number = 0
value = 0

for i in range(10):
    n = input()
    remainder_list.append(n%42)

for i in range(0, len(remainder_list)):
    number = remainder_list[i]
    for j in range(0, len(remainder_list)):
        if number == remainder_list[j] and i != j:
            remainder_list[i] = '*'
            break

for k in range(0, len(remainder_list)):
    if remainder_list[k] != '*':
        value = value + 1
print(value)