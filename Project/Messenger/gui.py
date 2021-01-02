from datetime import datetime
from tkinter import *
import tkinter


def client_exit():
    exit()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.accept = True
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
        file.add_command(label="Login", command=self.login)
        menu.add_cascade(label="Account", menu=file)

        self.accept = False

    def login(self):
        while not self.accept:
            self.canvas = tkinter.Canvas(root, width=400, height=300, relief='raised')
            self.canvas.pack()

            title = tkinter.Label(root, text='Login')
            title.config(font=('helvetica', 14))
            self.canvas.create_window(200, 25, window=title)

            email_label = tkinter.Label(root, text='Email:')
            email_label.config(font=('helvetica', 10))
            self.canvas.create_window(125, 80, window=email_label)
            email = tkinter.Entry(root)
            self.canvas.create_window(225, 80, window=email)

            password_label = tkinter.Label(root, text='Password:')
            password_label.config(font=('helvetica', 10))
            self.canvas.create_window(125, 120, window=password_label)
            password = tkinter.Entry(root)
            self.canvas.create_window(235, 120, window=password)

            self.pack(fill=BOTH, expand=1)
            button = Button(root, text="Login", command=lambda: self.login_permission(email, password), bg='brown', fg='white', font=('helvetica', 9, 'bold'))
            button.place(x=170, y=170)

            root.update()
            root.mainloop()

    def login_permission(self, email, password):
        self.email = email.get()
        self.password = password.get()
        try:
            if self.account[self.email] == self.password:
                self.label = tkinter.Label(root, text='You successfully logged in!', font=('helvetica', 10))
                self.canvas.create_window(200, 250, window=self.label)
                self.accept = True
                pass
            else:
                self.label = tkinter.Label(root, text='Error: You entered the wrong password.', font=('helvetica', 10))
                self.canvas.create_window(200, 250, window=self.label)
                self.label = tkinter.Label(root, text="", font=('helvetica', 10))
                pass
        except KeyError:
            self.label = tkinter.Label(root, text="Error: You entered the wrong email.", font=('helvetica', 10))
            self.canvas.create_window(200, 250, window=self.label)
            self.label = tkinter.Label(root, text="", font=('helvetica', 10))
            pass

    def register(self):
        while not self.accept:
            root = tkinter.Tk()
            root.title("Register")

            self.canvas = tkinter.Canvas(root, width=400, height=300, relief='raised')
            self.canvas.pack()

            title = tkinter.Label(root, text='Register')
            title.config(font=('helvetica', 14))
            self.canvas.create_window(200, 25, window=title)

            email_label = tkinter.Label(root, text='Email:')
            email_label.config(font=('helvetica', 10))
            self.canvas.create_window(125, 80, window=email_label)
            email = tkinter.Entry(root)
            self.canvas.create_window(225, 80, window=email)

            password_label = tkinter.Label(root, text='Password:')
            password_label.config(font=('helvetica', 10))
            self.canvas.create_window(125, 120, window=password_label)
            password = tkinter.Entry(root)
            self.canvas.create_window(235, 120, window=password)

            self.email = email.get()
            self.password = password.get()

            button = tkinter.Button(text='Register', command=self.register_permission, bg='brown', fg='white',
                                    font=('helvetica', 9, 'bold'))
            self.canvas.create_window(200, 180, window=button)

    def register_permission(self):
        self.email, self.password = map(str, input("Please enter your email and password: ").split())
        if self.email not in self.account.keys():
            self.account[self.email] = self.password
            label = tkinter.Label(root, text='You successfully created an account!', font=('helvetica', 10))
            self.canvas.create_window(200, 210, window=label)
            self.accept = True
        else:
            label = tkinter.Label(root, text='Error: Duplicate email. Please try again.', font=('helvetica', 10))
            self.canvas.create_window(200, 210, window=label)

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
