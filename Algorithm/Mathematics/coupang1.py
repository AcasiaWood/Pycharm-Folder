grade_list = {'A+': 4.5, 'A0': 4.2, 'A-': 4.0,
              'B+': 3.5, 'B0': 3.2, 'B-': 3.0,
              'C+': 2.5, 'C0': 2.2, 'C-': 2.0,
              'D+': 1.5, 'D0': 1.2, 'D-': 1.0,
              'F': 0.5}

grades = ["DS7651 A0", "CA0055 D+", "AI5543 C0",
          "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-",
          "AI5543 D+", "DS7651 A+", "OS1808 B-"]

new_grades = []

for i in range(len(grades)):
    subject = grades[i].split(' ')[0]
    grade = grades[i].split(' ')[1]
    flag = True
    for j in range(len(new_grades)):
        new_subject = new_grades[j].split(' ')[0]
        new_grade = new_grades[j].split(' ')[1]
        if subject == new_subject:
            flag = False
            if grade_list[new_grade] < grade_list[grade]:
                new_grades[j] = new_subject + " " + grade
    if flag:
        new_grades.append(subject + " " + grade)

for i in range(10):
    for j in range(len(new_grades) - 1):
        if grade_list[new_grades[j].split(' ')[1]] < grade_list[new_grades[j + 1].split(' ')[1]]:
            new_grades[j], new_grades[j + 1] = new_grades[j + 1], new_grades[j]

for item in new_grades:
    print(item)