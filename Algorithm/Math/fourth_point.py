coordinate_x = []
coordinate_y = []
new_x, new_y = 0, 0
for i in range(3):
    x, y = map(int, input().split())
    coordinate_x.append(x)
    coordinate_y.append(y)
comparison = coordinate_x[0]
if coordinate_x.count(comparison) == 1:
    new_x = comparison
comparison = coordinate_y[0]
if coordinate_y.count(comparison) == 1:
    new_y = comparison
print(new_x, new_y)
