from datetime import datetime

class User:
    def __init__(self):
        self.email = ""
        self.password = ""
        self.account = {"Admin": "1234"}
        self.texts = ["Hello, World!"]
        self.likes = [0]
        self.dislikes = [0]
        self.likes_account = [[]]
        self.dislikes_account = [[]]
        self.times = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        self.login()
        self.view()

    def login(self):
        accept = False
        while not accept:
            pick = int(input("Register(0), Login(1): "))
            if pick == 0:
                self.email, self.password = map(str, input("Please enter your email and password: ").split())
                if self.email not in self.account.keys():
                    self.account[self.email] = self.password
                    print("You successfully created an account!")
                    accept = True
                else:
                    print("Error: Duplicate email. Please try again.\n")
                    continue
            elif pick == 1:
                try:
                    self.email, self.password = map(str, input("Please enter your email and password: ").split())
                    if self.account[self.email] == self.password:
                        print("You successfully logged in!")
                        accept = True
                    else:
                        print("Error: You entered the wrong password.\n")
                        continue
                except KeyError:
                    print("Error: You entered the wrong email.\n")
                    continue
        f = open("account", 'w')
        f = open("account", 'a')
        f.write(str(self.account))
        f.close()
        print()

    def like(self):
        try:
            index = int(input("Which post: "))
            self.likes[index - 1] += 1
            if user.email not in self.likes_account[index - 1]:
                self.likes_account[index - 1].append(user.email)
            self.refresh(index)
        except IndexError:
            print("Error: The post does not exist.")
        print()

    def dislike(self):
        try:
            index = int(input("Which post: "))
            self.dislikes[index - 1] += 1
            if user.email not in self.dislikes_account[index - 1]:
                self.dislikes_account[index - 1].append(user.email)
            self.refresh(index)
        except IndexError:
            print("Error: The post does not exist.")
        print()

    def write(self):
        post = str(input("Please enter your post: "))
        self.texts.insert(0, post)
        self.likes.insert(0, 0)
        self.dislikes.insert(0, 0)
        self.times.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.likes_account.insert(0, [])
        self.dislikes_account.insert(0, [])
        print()

    def view(self):
        f = open("post", 'w')
        f = open("post", 'a')
        f.write("========================================\n")
        print("========================================")
        for i, text in enumerate(self.texts):
            print(str(i + 1) + ": " + text)
            print("Like: {} {}, Dislike: {} {}".format(self.likes[i], self.likes_account[i],
                                                       self.dislikes[i], self.dislikes_account[i]))
            print("Date: {}".format(self.times[i]))
            print("========================================")
            f.write(str(i + 1) + ": " + text + "\n")
            f.write("Like: {} {}, Dislike: {} {}\n".format(self.likes[i], self.likes_account[i],
                                                         self.dislikes[i], self.dislikes_account[i]))
            f.write("Date: {}\n".format(self.times[i]))
            f.write("========================================\n")
        f.close()
        print()

    def refresh(self, index):
        modify = self.texts[index - 1]
        del self.texts[index - 1]
        self.texts.insert(0, modify)
        modify = self.likes[index - 1]
        del self.likes[index - 1]
        self.likes.insert(0, modify)
        modify = self.dislikes[index - 1]
        del self.dislikes[index - 1]
        self.dislikes.insert(0, modify)
        del self.times[index - 1]
        self.times.insert(0, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        modify = self.likes_account[index - 1]
        del self.likes_account[index - 1]
        self.likes_account.insert(0, modify)
        modify = self.dislikes_account[index - 1]
        del self.dislikes_account[index - 1]
        self.dislikes_account.insert(0, modify)


user = User()

while True:
    option = int(input("Like(0), Dislike(1), Write(2), View(3), Logout(4): "))
    if option == 0:
        user.like()
    elif option == 1:
        user.dislike()
    elif option == 2:
        user.write()
    elif option == 3:
        print()
        user.view()
    elif option == 4:
        print()
        user.login()
    else:
        continue
