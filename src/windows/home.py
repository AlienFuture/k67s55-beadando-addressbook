from tkinter import *
from src.modules import user_manager

class Home_page:
    """Névjegyzék kezdőlapja"""
    def __init__(self):
        self.contacts = {}

    """Névjegyzék ablak indítása és kezelése"""
    def home_screen(self):
        self.window = Tk()
        self.window.title(f"Névjegyzék - {user_manager.get_user_name()}")
        self.selected = -1
        
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (600/2)
        y = (screen_height/2) - (300/2)

        def onSelect(evt):
            try:
                w = evt.widget
                index = int(w.curselection()[0])
                value = w.get(index)
                all = w.get(0, "end") # Vissza adja az összes kontaktot
                delete_entries()
                self.selected = get_contact_id(value)
                print(f"Kijelölt kontakt: {self.selected}")
                set_listbox_values(self.selected)
                button_save.config(state=NORMAL)
            except:
                self.selected = -1
                button_save.config(state=DISABLED)
                delete_entries()

        def get_contact_id(name):
            for key in self.contacts:
                if f"{self.contacts[key].lastname} {self.contacts[key].firstname}" == name:
                    return key
                

        def set_listbox_values(employee_index):
            contact = self.contacts[employee_index]
            if contact.firstname != None:
                entry_firstname.insert(0, contact.firstname)
            if contact.lastname != None:
                entry_lastname.insert(0, contact.lastname)
            if contact.postcode != None:
                entry_postcode.insert(0, contact.postcode)
            if contact.city != None:
                entry_city.insert(0, contact.city)
            if contact.address != None:
                entry_address.insert(0, contact.address)
            #entry_birthday.insert(0, contact.birthday)
            if contact.phone != None:
                entry_phone.insert(0, contact.phone)
            if contact.secondphone != None:
                entry_secondphone.insert(0, contact.secondphone)
            if contact.notes != None:
                entry_notes.insert(0, contact.notes)

        def delete_entries():
            entry_firstname.delete(0, END)
            entry_lastname.delete(0, END)
            entry_postcode.delete(0, END)
            entry_city.delete(0, END)
            entry_address.delete(0, END)
            entry_phone.delete(0, END)
            entry_secondphone.delete(0, END)
            entry_notes.delete(0, END)

        def add_new():
            user_manager.add_new_contact()
            delete_entries()
            load_listbox()

        def delete_contact():
            if self.selected == -1:
                print("Nincs kijelölve senki sem.")
            else:
                user_manager.delete_contact(self.selected)
                delete_entries()
                load_listbox()

        def save_contact():
            print(self.selected)
            user_manager.save_contact(self.selected, entry_lastname.get(), entry_firstname.get(), entry_postcode.get(), entry_city.get(), entry_address.get(), entry_birthday.get(), entry_phone.get(), entry_secondphone.get(), entry_notes.get())
            load_listbox()


        def load_listbox():
            listbox_contactlist.delete(0, END)
            self.contacts = user_manager.get_contacts()
            for key in self.contacts:
                listbox_contactlist.insert(END, f"{self.contacts[key].lastname} {self.contacts[key].firstname}")

        listbox_contactlist = Listbox(self.window, height=30)
        listbox_contactlist.grid(row=0, rowspan=13, column=0, padx=10, sticky=W)

        listbox_contactlist.bind('<<ListboxSelect>>', onSelect)

        load_listbox()
        
        frame_buttoncontrol = Frame(self.window)
        frame_buttoncontrol.grid(column=0, row=15)

        button_add = Button(frame_buttoncontrol, text="Új", command=add_new)
        button_remove = Button(frame_buttoncontrol, text="Törlés", command=delete_contact)

        button_add.pack(side= LEFT)
        button_remove.pack(side=LEFT)

        # Adress design
        label_lastname = Label(self.window, text="Vezetéknév:")
        label_firstname = Label(self.window, text="Keresztnév:")
        label_postcode = Label(self.window, text="Körzetszám:")
        label_city = Label(self.window, text="Település:")
        label_address = Label(self.window, text="Cím:")
        label_birthday = Label(self.window, text="Születési dátum:")
        label_phone = Label(self.window, text="Telefonszám:")
        label_secondphone = Label(self.window, text="Másodlagos telefonszám:")
        label_notes = Label(self.window, text="Megjegyzések")

        label_lastname.grid(row=0, column=2, padx=20, pady=5)
        label_firstname.grid(row=1, column=2, padx=20, pady=5)
        label_postcode.grid(row=2, column=2, padx=20, pady=5)
        label_city.grid(row=3, column=2, padx=20, pady=5)
        label_address.grid(row=4, column=2, padx=20, pady=5)
        label_birthday.grid(row=5, column=2, padx=20, pady=5)
        label_phone.grid(row=6, column=2, padx=20, pady=5)
        label_secondphone.grid(row=7, column=2, padx=20, pady=5)
        label_notes.grid(row=8, column=2, padx=20, pady=5)

        entry_lastname = Entry(self.window)
        entry_firstname = Entry(self.window)
        entry_postcode = Entry(self.window)
        entry_city = Entry(self.window)
        entry_address = Entry(self.window)
        entry_birthday = Entry(self.window)
        entry_phone = Entry(self.window)
        entry_secondphone = Entry(self.window)
        entry_notes = Entry(self.window)

        entry_lastname.grid(row=0, column=3)
        entry_firstname.grid(row=1, column=3)
        entry_postcode.grid(row=2, column=3)
        entry_city.grid(row=3, column=3)
        entry_address.grid(row=4, column=3)
        entry_birthday.grid(row=5, column=3)
        entry_phone.grid(row=6, column=3)
        entry_secondphone.grid(row=7, column=3)
        entry_notes.grid(row=8, column=3)

        button_save = Button(text="Változtatások mentése", state=DISABLED, command=save_contact)
        button_save.grid(row=9, column=2, columnspan=2)

        self.window.geometry('%dx%d+%d+%d' % (600, 600, x, y))
        self.window.mainloop()



