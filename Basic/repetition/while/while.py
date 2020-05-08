# creating a while statement

number = 0
while number < 3:
    number += 1
    print(number)

# forcibly exiting the while statement

card = 3000
while card:
    card -= 100
    if card == 0:
        print('there is no money on the card. charge the card.')
        break

# return to the beginning of the while statement

number = int(input())
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

# infinite loop

while True:
    print('exit the loop')
