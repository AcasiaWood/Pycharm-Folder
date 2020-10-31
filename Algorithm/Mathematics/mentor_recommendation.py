gender, age, major, hobby = map(str, input().split())

members = ['A', 'B', 'C', 'D', 'E']
mentors = [['Male', '26', 'Mathematics', 'Debate'], ['Male', '30', 'Science', 'Reading'],
           ['Female', '32', 'History', 'Sports'], ['Male', '29', 'Literature', 'Cooking'],
           ['Female', '28', 'English', 'Crafts']]
majors = {'Mathematics': 10, 'Science': 9, 'History': 8, 'English': 11, 'Moral': 9, 'Literature': 10}
hobbies = {'Sports': 11, 'Coding': 13, 'Debate': 12, 'Cooking': 11, 'Crafts': 13, 'Reading': 12}
scores = [0, 0, 0, 0, 0]

for i in range(len(mentors)):
    if gender == mentors[i][0]:
        scores[i] += 10
    else:
        scores[i] += 5

ages = []
for i in range(len(mentors)):
    ages.append(abs(int(age) - int(mentors[i][1])))

if 20 <= min(ages) < 30:
    scores[ages.index(min(ages))] += min(ages)
elif 30 <= min(ages) < 40:
    scores[ages.index(min(ages))] += (min(ages) * 0.1)
elif 40 <= min(ages) < 50:
    scores[ages.index(min(ages))] += (min(ages) * 0.2)
elif 50 <= min(ages) < 60:
    scores[ages.index(min(ages))] += (min(ages) * 0.3)
elif min(ages) >= 60:
    scores[ages.index(min(ages))] += (min(ages) * 0.5)

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

print("Mentor: {}".format(members[scores.index(max(scores))]))
print(members)
print(scores)
