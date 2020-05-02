def select_mark():
    mark = input("Select Mark : ")
    if mark == "o":
        return mark
    elif mark == "x":
        return mark
def random_order():
    if random.randrange(0, 2) == 0:
        print("user turn")
        return 0
    else:
        print("computer turn")
        return 1
def make_board():
    for i in range(0, 9):
        zone.append("*")
    return zone
def check_win(zone, mark):
    if zone[0] == mark and zone[1] == mark and zone[2] == mark:
        return True
    elif zone[0] == mark and zone[3] == mark and zone[6] == mark:
        return True
    elif zone[2] == mark and zone[5] == mark and zone[8] == mark:
        return True
    elif zone[6] == mark and zone[7] == mark and zone[8] == mark:
        return True
    elif zone[0] == mark and zone[4] == mark and zone[8] == mark:
        return True
    elif zone[2] == mark and zone[4] == mark and zone[6] == mark:
        return True
    elif zone[1] == mark and zone[4] == mark and zone[7] == mark:
        return True
    elif zone[3] == mark and zone[4] == mark and zone[5] == mark:
        return True
    else:
        return False
def print_board(zone, a):
    while True:
        print(zone[a], zone[a+1], zone[a+2])
        a = a + 3
        if a >= 8:
            break
def player_turn(zone):
    while True:
        print("")
        loc_zone = int(input("Enter Location Number : "))
        if 1 <= loc_zone <= 9:
            if zone[loc_zone-1] == 0:
                zone[loc_zone-1] = 1
                print(zone)
                break
    return loc_zone
def computer_turn(zone):
    while True:
        loc_zone = random.randrange(0, 10)
        if zone[loc_zone-1] == 0:
            print("")
            print("Enter Location Number :", loc_zone)
            zone[loc_zone-1] = 2
            print(zone)
            break
    return loc_zone

import random
zone = []
loc_zone = 0
a = 0

print("*은 채워지지 않은 구역, 마크는 채워진 구역을 의미한다. 하지만 컴퓨터가 구역을 채우면, 구역 번호가 컴퓨터의 마크로 변경된다.")
print("칸은 모두 3 x 3 구역으로 나눠져 있지만, 가로 한 구역에 세 구역, 세로 한 구역도 세 구역으로 나눠진다.")
print("컴퓨터 Ai와 당신은 플레이어로 게임을 진행하게 된다. 컴퓨터 번호는 1, 당신의 번호는 0이다.")
# 경우의 수 : 8

make_board()
print_board(zone, a)
