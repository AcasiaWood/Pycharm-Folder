import math

case = int(input())

for i in range(case):

    # in order, the first x-coordinate, y-coordinate, and radius are input, respectively.
    # and the second x-coordinate, y-coordinate, and radius are input.
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # use the distance formula.
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if distance == 0 and r1 == r2:  # if the circles overlap completely
        print(-1)

    elif max(r1, r2) - min(r1, r2) == distance or r1 + r2 == distance:  # when the circle is inscribed or circumscribed
        print(1)

    # if the circle does not meet is completely isolated or implied
    elif r1 + r2 < distance or max(r1, r2) - min(r1, r2) > distance:
        print(0)

    # The rest of the cases have two points of intersection
    else:
        print(2)  
