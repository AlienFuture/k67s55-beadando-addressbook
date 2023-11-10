from tkinter import *
from tkinter import messagebox
from src.modules import user_manager

class Login_user:
    def login_user(self):
        window = Tk()
        window.title('Bejelentkezés')

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (400/2)
        y = (screen_height/2) - (140/2)

        def login():
            if user_manager.login(entry_neptuncode.get(), entry_password.get()):
                messagebox.showinfo("showinfo", "Bejelentkezés sikeres!")
                window.destroy()
            else:
                messagebox.showerror("showerror", "Bejelentkezés sikertelen!")


        label_welcomemsg = Label(window, text="Névjegyzék - Bejelentkezés", font=("Arial", 25))
        label_welcomemsg.grid(row=0, column=0, columnspan=2)
        label_neptuncode = Label(window, text="Neptun:")
        label_password = Label(window, text="Jelszó:")

        entry_neptuncode = Entry(window, width=30)
        entry_password = Entry(window, width=30)

        button_ok = Button(window, text="Bejelentkezés", command=login)

        label_neptuncode.grid(row=1, column=0, padx=20, sticky=E)
        label_password.grid(row=2, column=0, padx=20, sticky=E)
        entry_neptuncode.grid(row=1, column=1, padx=20, sticky=W)
        entry_password.grid(row=2, column=1, padx=20, sticky=W)
        button_ok.grid(row=3, column=0, columnspan=2, padx=20)

        window.geometry('%dx%d+%d+%d' % (400, 140, x, y))
        window.mainloop()
