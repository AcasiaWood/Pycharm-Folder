# Distance between two points

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(distance)

# Distance between a point and a line

x, y = map(int, input().split())
a, b, c = map(int, input().split())
distance = abs((a * x + b * y + c)) / (a ** 2 + b ** 2) ** 0.5

print(distance)

# Distance between two lines (parallel)

a, b, c1 = map(int, input().split())
c2 = int(input("Same Same "))
distance = abs(c1 - c2) / (a ** 2 + b ** 2) ** 0.5

print(distance)