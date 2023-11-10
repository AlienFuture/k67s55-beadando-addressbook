import mariadb
from src.models import Contact
import src.config as config


def connect():
    """Adatbázishoz való csatlakozás"""
    try:
        global sql_conn
        sql_login = config.Sql_login
        sql_conn = mariadb.connect(
        user=sql_login.username,
        password=sql_login.password,
        host=sql_login.hostname,
        port=sql_login.port,
        database=sql_login.database
        )

        print("Adatbázishoz való csatlakozás megtörtént.")

        global sql_cursor
        sql_cursor = sql_conn.cursor()
    except mariadb.Error as e:
        print(f"Adatbázishoz való csatlaközés sikertelen: {e}")


def check_login(neptuncode, password):
    """Bejelentkezési információ ellenőrzése"""
    sql_cursor.execute(f"SELECT neptuncode FROM users WHERE neptuncode = '{neptuncode}' AND password = '{password}'",)
    for(neptuncode) in sql_cursor:
        return True
    return False
    
def get_user_fullname(neptuncode):
    """Teljes nevet ad vissza Neptun kód alapján."""
    print(f"the neptun code is {neptuncode}")
    sql_cursor.execute(f"SELECT full_name FROM users WHERE neptuncode = '{neptuncode}'")
    for (full_name,) in sql_cursor.fetchall():
        return(full_name)
        
    return "N/A"
    
def get_contacts(neptuncode):
    """Vissza adja az összes kontaktot neptun kód alapján"""
    sql_cursor.execute(f"SELECT id, firstname, lastname, postcode, city, address, phone, secondphone, birthday, notes FROM contacts WHERE user_id = '{neptuncode}'")
    contacts = {}

    for (id, firstname, lastname, postcode, city, address, phone, secondphone, birthday, notes) in sql_cursor:
        contacts[id] = Contact.Contact(id, firstname, lastname, postcode, city, address, birthday, phone, secondphone, notes )

    return contacts
    
def create_blank(neptuncode):
    """Üres kontakt létrehozása neptun kódnak"""
    sql_cursor.execute(f"INSERT INTO contacts (firstname, lastname, postcode, city, address, phone, secondphone, birthday, notes, user_id) VALUES (?,?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, ?)", ("Új", "Kontakt", neptuncode))
    row_id = sql_cursor.lastrowid
    sql_conn.commit()
    return row_id

def delete_contact(id):
    """Kontakt  törlése kontakt ID alapján"""
    sql_cursor.execute(f"DELETE FROM contacts WHERE id = {id}")
    row_id = sql_cursor.lastrowid
    sql_conn.commit()
    return row_id

def update_contact(new_contact):
    """Meglévő Kontakt frissítése Contact osztály alapján"""
    sql_cursor.execute(f"UPDATE contacts SET firstname='{new_contact.firstname}', lastname='{new_contact.lastname}', postcode='{new_contact.postcode}', city='{new_contact.city}', address='{new_contact.address}', birthday='{new_contact.birthday}', phone='{new_contact.phone}', secondphone='{new_contact.secondphone}', notes='{new_contact.notes}' WHERE id={new_contact.id}")
    row_id = sql_cursor.lastrowid
    sql_conn.commit()
    return row_id