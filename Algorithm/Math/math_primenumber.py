n = int(input())
tried = 1
for i in range(2, n+1):
    if n % i == 0:
        tried = tried + 1
if tried == 2:
    print('it is prime number')
elif tried > 2 or tried == 1:
    print('it is not prime number')
