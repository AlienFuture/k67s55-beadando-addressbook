from . import database_manager as db
from src.models import Contact
current_neptuncode = ""
current_contacts = {}

def login(neptuncode, password):
    """Bejelentkezés neptun kód alapján"""
    db.connect()
    if db.check_login(neptuncode, password):
        print("Bejelentkezés sikeres.")
        global current_neptuncode
        current_neptuncode = neptuncode
    else:
        print("Bejelentkezés sikertelen.")
        return False
    
    return True

def get_user_name():
    """Teljes név lekérése"""
    return db.get_user_fullname(current_neptuncode)

def get_contacts():
    """Kontaktok lekérése"""
    global current_contacts
    if current_contacts == {}:
        current_contacts = db.get_contacts(current_neptuncode)
    return current_contacts

def add_new_contact():
    """Új kontakt létrehozása"""
    contact_id = db.create_blank(current_neptuncode)
    print(contact_id)
    current_contacts[contact_id] = Contact.Contact(contact_id, "Kontakt", "Új", None, None, None, None, None, None, None)

def delete_contact(id):
    """kontaktok törlése"""
    deleted_row = db.delete_contact(id)
    print(deleted_row)
    del(current_contacts[id])

def save_contact(nid, new_lastname, new_firstname, new_postcode, new_city, new_address, new_birthday, new_phone, new_secondphopne, new_notes):
    """Kontakt mentése"""
    new_contact = Contact.Contact(id=nid, lastname=new_lastname, firstname=new_firstname, postcode=new_postcode, city=new_city, address=new_address, birthday=new_birthday, phone=new_phone, secondphone=new_secondphopne, notes=new_notes)
    db.update_contact(new_contact)
    current_contacts[nid] = new_contact