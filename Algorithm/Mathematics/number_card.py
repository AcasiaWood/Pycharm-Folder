# Baekjoon

m = int(input())
card_list = list(input().split())
n = int(input())
number_list = list(input().split())
string = ''

for number in range(len(number_list)):
    if number_list[number] in card_list:
        number_list[number] = 1
    else:
        number_list[number] = 0
    string += str(number_list[number]) + ' '
    
print(string)
