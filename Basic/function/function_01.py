def addition(a, b):
    c = a + b
    return c
def subtraction(a, b):
    c = a - b
    return c
def multiply(a, b):
    c = a * b
    return c
def division(a, b):
    c = a / b
    return c

class test:

    def __init__(self):

        self.health = 100

        self.atk = random.randrange(10, 15)

    def attack(self):

        return self.atk

    def defend(self, damage):

        self.health = self.health - damage

    def skill(self):

        self.atk = random.randrange(10, 15)

        self.atk = self.atk + random.randrange(0, 5)

        return self.atk

    def see_health(self):

        print("")
        print("----------------------")
        print("")
        print("Health :", self.health)
        print("")
        print("Attack :", self.atk)
        print("")

def battle_stat(Battle_Stat):
    print("")
    print("----------------------")
    print("")
    print("Battle Status :", Battle_Stat)
    print("")
    print("----------------------")
    return Battle_Stat

def list_append(a):
    for i in range(1, a):
        if a % i == 0:
            c.append(i)
    print(c)
    return total

def check_total(total):
    for i in range(0, len(c)):
        total = total + c[i]
    print(total)
    return total

def check(total):
    if a == total:
        print("it`s correct")
    elif a != total:
        print("it`s incorrect")

def numcreate():
    import random
    a = []
    for i in range(5):
        num = random.randrange(150)
        a.append(num)
    return a

def searching(a):
    print(a)
    max = []
    for c in range(5):
        high = 0
        for i in range(len(a)):
            if(a[high] < a[i]):
                high = i
    max.append([a[high], high])
    a[high] = -1
    return max

def total(max):
    total = 0
    for i in range(len(max)):
        total += max[i][0]
    return total

def cleaning(max):
    print(total)
    for i in range(len(max)):
        print(max[i][1])