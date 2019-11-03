if input == 1:
    print(addition(a, b))
elif input == 2:
    print(subtraction(a, b))
elif input == 3:
    print(multiply(a, b))
else:
    print(division(a, b))
if (mid == Enter):
    print("it`s correct.")
    print(i+1)
    break
elif (mid > Enter):
    end = mid
else:
    start = mid
if zone[loc_zone - 1] == 0:
    print("")
    print("Enter Location Number :", loc_zone)
    zone[loc_zone - 1] = 2
    print(zone)
if 1 <= loc_zone <= 9:
    if zone[loc_zone - 1] == 0:
        zone[loc_zone - 1] = 1
        print(zone)
    if random.randrange(0, 2) == 0:
        print("user turn")
        return 0

    if input_str == "in":
        num = int(input("Enter Value : "))
        enqueue(num)
    if input_str == "de":
        dequeue()

if(item[i] == buy):
    if(cost[i] <= money):
        number = i
        print(buy, ":" ,cost[i])
    elif(cost[i] > money):
        print(buy, ":" , "Not Enough Money")

if A < 0:
    B = int(input())
    print(A+B)

if len(queue) == 0:
    print("underflow")
    return
else:
    print(queue[0])
    del queue[0]
    return

    if len(queue) > max:
        print("overflow")
        return
    else:
        queue.append(num)

if(control == "buy"):
        print(item_list)
        reply = input("Enter Weapon :")
        if(reply == "sword"):

            if (len(stack) == 0):

                print("You can`t pop them")

            else:

                print(stack)

                del stack[len(stack) - 1]

                print(stack)

if(len(stack) > limit):

            print("overflow")

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 - speed
                if event.key == pygame.K_RIGHT:
                    x_change = 5 + speed
                if event.key == pygame.K_UP:
                    y_change = -5 - speed
                if event.key == pygame.K_DOWN:
                    y_change = 5 + speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0

        if x > display_width - car_width or x < 0 or x > 680 or y < -20 or y > 480:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            speed += 0.5
            thing_speed += 0.5
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width \
                    or x + car_width > thing_startx \
                    and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()

if(Status == 0):
        while(unit1.health > 0 or unit2.health <= 0):
            unit1.see_health()
            key = int(input("Enter the Number : "))
            if(key == 1):
                a = unit1.attack()
                if(random.randrange(3) == random.randrange(3)):
                    print("")
                    print("Attack Successed")
                    unit2.defend(a)
                else:
                    print("")
                    print("Attack Missed")
            elif(key == 2):
                a = unit1.skill()
                if(random.randrange(5) == random.randrange(5)):
                    print("")
                    print("Skill Attack Successed")
                    unit2.defend(a)
                else:
                    print("")
                    print("Skill Attack Missed")

            unit2.see_health()
            key = random.randrange(1,2)
            if(key == 1):
                a = unit2.attack()
                if (random.randrange(3) == random.randrange(3)):
                    print("Computer Skill Successed")
                    unit1.defend(a)
                else:
                    print("Computer Attack Missed")
            elif(key == 2):
                a = unit2.skill()
                if (random.randrange(5) == random.randrange(5)):
                    print("Computer Skill Successed")
                    unit1.defend(a)
                else:
                    print("Computer Skill Missed")
            if(unit1.health <= 0):
                Battle_Stat = "Failed"
                battle_stat(Battle_Stat)
                break
            elif(unit2.health <= 0):
                Battle_Stat = "Victory"
                battle_stat(Battle_Stat)
                Battle_Victory = Battle_Victory + 1
                break
    elif(Status == 1):
        print("")
        print("----------------------")
        print("")
        print(item)
        print("")
        print("----------------------")
        print("")
        print("Weapon : Pole, Spear, Axe, Sword")
        print("")
        print("----------------------")
        print("")
        weapon = str(input("Enter the Weapon : "))

        if(weapon == "Pole"):
            if(Battle_Victory >= 3):
                item.append("Pole")
                Battle_Victory = Battle_Victory - 3
            else:
                print("")
                print("----------------------")
                print("")
                print("Not Enough Cash")
        elif(weapon == "Spear"):
            if(Battle_Victory >= 5):
                item.append("Spear")
                Battle_Victory = Battle_Victory - 5
            else:
                print("")
                print("----------------------")
                print("")
                print("Not Enough Cash")
        elif(weapon == "Axe"):
            if(Battle_Victory >= 8):
                item.append("Axe")
                Battle_Victory = Battle_Victory - 8
            else:
                print("")
                print("----------------------")
                print("")
                print("Not Enough Cash")
        elif(weapon == "Sword"):
            if(Battle_Victory >= 10):
                item.append("Sword")
                Battle_Victory = Battle_Victory - 10
            else:
                print("")
                print("----------------------")
                print("")
                print("Not Enough Cash")

    if i == a[len(a)-1]:
        break

    if b%i == 0:
        a.append(i)
        print(a)
        i = 0

if(temp > max):
        max = temp
    elif(temp <= 0):
        temp = 0

    if (len(stack) == 0):

        print("You can`t pop them")

    else:

        print(stack)

        del stack[len(stack) - 1]

        print(stack)

    if (len(stack) > limit):
        print("overflow")

    b = random.randrange(10)

    stack.append(b)