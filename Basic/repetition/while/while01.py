while True:
    loc_zone = random.randrange(0, 10)
    if zone[loc_zone - 1] == 0:
        print("")
        print("Enter Location Number :", loc_zone)
        zone[loc_zone - 1] = 2
        print(zone)
        break

while True:
    print("")
    loc_zone = int(input("Enter Location Number : "))
    if 1 <= loc_zone <= 9:
        if zone[loc_zone - 1] == 0:
            zone[loc_zone - 1] = 1
            print(zone)
            break

while True:
    print(zone[a], zone[a+1], zone[a+2])
    a = a + 3
    if a >= 8:
        break

while True:
    input_str = input()
    if input_str == "in":
        num = int(input("Enter Value : "))
        enqueue(num)
    if input_str == "de":
        dequeue()
        
while True:
    a = input()
    control = input()
    if(control == "buy"):
        print(item_list)
        reply = input("Enter Weapon :")
        if(reply == "sword"):

while True:
    time.sleep(1)
    number = number * save
    print(number)
    
    while not gameExit:

        print(x, y)

        for event in pygame.event.get():
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

        x += x_change
        y += y_change
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)
        things_speed(speed)

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

        pygame.display.update()
        clock.tick(60)
        
while True:
    print("")
    unit1.health = 100
    unit2.health = 100
    print("----------------------")
    print("")
    print("Battle Victory :", Battle_Victory)
    print("")
    print("----------------------")
    print("")
    Status = int(input("Enter the Number : "))
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