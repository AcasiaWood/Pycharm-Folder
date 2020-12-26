import os
import getpass

user = getpass.getuser()

num = 0

limit = len(os.listdir("/home/" + user + "/PycharmProjects/project/file/foodwaste/egg"))

path = "/home/" + user + "/PycharmProjects/project/file/"

file = open("../file/sample1.csv", 'w')
file.write("filename,label")
file.close()

file = open("../file/sample2.csv", 'w')
file.write("filename,label")
file.close()

for d1 in os.listdir(path):
    r1 = path + d1
    try:
        if d1 == "foodwaste":
            num = 0
        elif d1 == "generalwaste":
            num = 1
        for d2 in os.listdir(r1):
            r2 = r1 + '/' + d2
            for d3 in os.listdir(r2):
                r3 = r2 + '/' + d3
                number = ""
                for i in range(len(d3)):
                    if d3[i].isdigit():
                        number += d3[i]
                if int(number) < limit / 2 + 1:
                    file = open("../file/sample1.csv", 'a')
                    file.write("\n{},{}".format(r3, num))
                    file.close()
                elif int(number) > limit / 2:
                    file = open("../file/sample2.csv", 'a')
                    file.write("\n{},{}".format(r3, num))
                    file.close()
    except NotADirectoryError:
        pass