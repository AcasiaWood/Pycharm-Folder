import getpass

user = getpass.getuser()

src = open("/home/{}/PycharmProjects/project/file/sample2.csv".format(user), 'r').readlines()
tar = open("/home/{}/PycharmProjects/project/file/sample.csv".format(user), 'r').readlines()
limit = 201
var = 0

for i in range(limit):
    if src[i].split(',')[1].replace('\n', '') == tar[i].replace('\n', ''):
        var += 1

percentage = var / limit * 100

print("percentage: {}%".format(round(percentage)))