from datetime import datetime
from tkinter import *
import tkinter


def client_exit():
    exit()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.accept = False
        self.email = ""
        self.password = ""
        self.account = {"Admin": "1234"}
        self.texts = ["Hello, World!"]
        self.likes = [0]
        self.dislikes = [0]
        self.likes_account = [[]]
        self.dislikes_account = [[]]
        self.times = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        self.canvas = None
        self.label = None
        self.tab = None
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Messenger")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=client_exit)
        menu.add_cascade(label="File", menu=file)

        file = Menu(menu)
        if not self.accept:
            file.add_command(label="Login", command=self.login)
            menu.add_cascade(label="Account", menu=file)
        else:
            file.add_command(label="Logout", command=self.logout)
            menu.add_cascade(label="Account", menu=file)

            file = Menu(menu)
            file.add_command(label="Like", command=self.like)
            file.add_command(label="Dislike", command=self.dislike)
            file.add_command(label="Write", command=self.write)
            file.add_command(label="View", command=self.view)
            menu.add_cascade(label="Interest", menu=file)

        self.accept = False

    def login(self):
        while not self.accept:
            self.tab = Tk()
            self.tab.geometry("400x300")
            self.tab.title("Login")

            self.canvas = tkinter.Canvas(self.tab, width=400, height=300, relief='raised')
            self.canvas.pack()

            title = tkinter.Label(self.tab, text='Login')
            title.config(font=('helvetica', 14))
            self.canvas.create_window(200, 25, window=title)

            email_label = tkinter.Label(self.tab, text='Email:')
            email_label.config(font=('helvetica', 10))
            self.canvas.create_window(125, 80, window=email_label)
            email = tkinter.Entry(self.tab)
            self.canvas.create_window(225, 80, window=email)

            password_label = tkinter.Label(self.tab, text='Password:')
            password_label.config(font=('helvetica', 10))
            self.canvas.create_window(125, 120, window=password_label)
            password = tkinter.Entry(self.tab)
            self.canvas.create_window(235, 120, window=password)

            self.pack(fill=BOTH, expand=1)
            button = Button(self.tab, text="Login", command=lambda: self.login_permission(email, password),
                            bg='brown', fg='white', font=('helvetica', 9, 'bold'))
            button.place(x=170, y=170)

            self.tab.update()
            self.tab.mainloop()

    def login_permission(self, email, password):
        self.email = email.get()
        self.password = password.get()
        try:
            if self.account[self.email] == self.password:
                self.label = tkinter.Label(self.tab, text='You successfully logged in!', font=('helvetica', 10))
                self.canvas.create_window(200, 250, window=self.label)
                self.accept = True
                self.tab.destroy()
                self.tab.quit()
                self.init_window()
            else:
                self.label = tkinter.Label(self.tab, text='Error: You entered the wrong password.', font=('helvetica', 10))
                self.canvas.create_window(200, 250, window=self.label)
                self.label = tkinter.Label(self.tab, text="", font=('helvetica', 10))
        except KeyError:
            self.label = tkinter.Label(self.tab, text="Error: You entered the wrong email.", font=('helvetica', 10))
            self.canvas.create_window(200, 250, window=self.label)
            self.label = tkinter.Label(self.tab, text="", font=('helvetica', 10))

    def logout(self):
        self.accept = False
        self.init_window()

    def like(self):
        try:
            index = int(input("Which post: "))
            self.likes[index - 1] += 1
            if self.email not in self.likes_account[index - 1]:
                self.likes_account[index - 1].append(self.email)
            self.refresh(index)
        except IndexError:
            print("Error: The post does not exist.")
        print()

    def dislike(self):
        try:
            index = int(input("Which post: "))
            self.dislikes[index - 1] += 1
            if self.email not in self.dislikes_account[index - 1]:
                self.dislikes_account[index - 1].append(self.email)
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


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
