gender, age, major, hobby = map(str, input().split())
gender = gender[0].upper() + gender[1:len(gender)]
major = major[0].upper() + major[1:len(major)]
hobby = hobby[0].upper() + hobby[1:len(hobby)]

members = ['A', 'B', 'C', 'D', 'E']
mentors = [['Male', '26', 'Mathematics', 'Debate'], ['Male', '30', 'Science', 'Reading'],
           ['Female', '32', 'History', 'Sports'], ['Male', '29', 'Literature', 'Cooking'],
           ['Female', '28', 'English', 'Crafts']]
majors = {'Mathematics': 10, 'Science': 9, 'History': 8, 'English': 11, 'Moral': 9, 'Literature': 10}
hobbies = {'Sports': 11, 'Coding': 13, 'Debate': 12, 'Cooking': 11, 'Crafts': 13, 'Reading': 12}
scores = [0, 0, 0, 0, 0]
percentage = [2, 1.5, 1, 0.5]

for i in range(len(mentors)):
    if gender == mentors[i][0]:
        scores[i] += 10
    else:
        scores[i] += 5

ages = []
for i in range(len(mentors)):
    ages.append(abs(int(age) - int(mentors[i][1])))

for i in range(20, 41, 10):
    if i <= int(age) <= i + 10:
        i = int(i / 10) - 1
        if int(min(age)) == 0:
            value = 5
        else:
            value = int(min(age))
        scores[ages.index(min(ages))] += (value * percentage[i])
        break

for i in range(len(ages)):
    if min(ages) != ages[i]:
        scores[i] += 5

for i in range(len(mentors)):
    if mentors[i][2] == major:
        scores[i] += majors[major]
    else:
        scores[i] += 5
    if mentors[i][3] == hobby:
        scores[i] += hobbies[hobby]
    else:
        scores[i] += 5

for i in range(10):
    for j in range(len(members)-1):
        if scores[j] > scores[j + 1]:
            score = scores[j]
            scores[j] = scores[j + 1]
            scores[j + 1] = score
            member = members[j]
            members[j] = members[j + 1]
            members[j + 1] = member

print("Mentor: {}".format(members[len(members) - 1]))
print(members)
print(scores)
