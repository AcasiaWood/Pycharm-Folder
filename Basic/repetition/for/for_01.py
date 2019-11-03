for i in range(0,100):
    a.append(i)
    print(i)

for i in range(1, 101):
    a.append(i)

for i in range(end):
    mid = int((start + end )/ 2)
    print(mid)
    if (mid == Enter):
        print("it`s correct.")
        print(i+1)
        break
    elif (mid > Enter):
        end = mid
    else:
        start = mid

for i in range(0, 9):
    zone.append("*")
return zone

for i in range(1, 100):
    Squared_Number = i * i
    if int(Squared[i] / 10) == m / 10:
        Squared.append(Squared[i])

for i in range(len(temp)):
    flag = 0
    for j in range(len(email)):
        if language[j] == email[i]:
            flag = 1
    if flag == 0:
        see.append(email[i])

for i in range(0, len(item)):
    if(item[i] == buy):
        if(cost[i] <= money):
            number = i
            print(buy, ":" ,cost[i])
        elif(cost[i] > money):
            print(buy, ":" , "Not Enough Money")

for i in range(10):
    b = random.randrange(-100, 100)
    a.append(b)
print(a)
max = a[0]
temp = a[0]

for i in range(1, len(a)):
    temp = temp + a[i]
    if(temp > max):
        max = temp
    elif(temp <= 0):
        temp = 0

for i in range(1, 100):
    Squared_Number = i * i
    if m <= Squared_Number <= n:
        Squared.append(Squared_Number)
print(Squared)

for i in range(0, len(Squared)):
    Value += Squared[i]
print("Squared Number :" ,Value)
print("Minimum Number :" ,Squared[0])

for i in range(len(temp)):
    flag = 0
    for j in range(len(email)):
        if language[j] == email[i]:
            flag = 1
    if flag == 0:
        see.append(email[i])

for i in range(0, len(temp)):
    email.append(temp[i])

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

for i in range(1, b+1):
    if b%i == 0:
        a.append(i)
        print(a)
        i = 0

for i in range(10):
    b = random.randrange(-100, 100)
    a.append(b)
print(a)
max = a[0]
temp = a[0]

for i in range(1, len(a)):
    temp = temp + a[i]
    if(temp > max):
        max = temp
    elif(temp <= 0):
        temp = 0

for c in range(len(a)):
    if(a[c] > high):
        high = a[c]
print(high)

low = a[0]
for c in range(len(a)):
    if(a[c] < low):
        low = a[c]
print(low)