# k67s55-beadando-addressbook

# Alap információk
Hallgató neve: Vámos Balázs
Neptun kód: K67S55

# Feladat
Python környezetben megvalósítva lett egy egyszerű, grafikai névjegyzék alkalmazás ami MYSQL/MariaDB adatbázissal kommunikál. 
Két nézetből áll:
    - Bejelentkezési ablak
    - Kezdő ablak (Maga a kontaktlista)

# Szükséges modulok
Az alkalmazás **mariadb** külső modult használ, amely pip paranccsal telepíthető:
```
pip3 install mariadb
```

# Használt osztályok: 
- windows/login.py -  Login_user: Bejelentkezésért felelős osztály, ablakkezeléssel.
- windows/home.py - Home_page: Névjegyzék ablakért felelős osztály.
- models/Contact.py - Contact: Kontakt model sémája

# Saját készítésű használt modulok:
- modules/database_manager.py: Adatbázis kezelő modul. Függvényei:
        - connect(): Adatbázishoz való csatlakozás
        - check_login(neptuncode, password): Bejelentkezés információk ellenőrzése
        - get_user_fullname(neptuncode): Teljes nevet vissza adja Neptun kód alapján
        - get_contacts(neptuncode): Vissza adja az összes kontaktot neptun kód alapján
        - create_blank(neptuncode): Létrehoz egy üres kontaktot adatbázisban
        - delete_contact(id): Törli a kontaktot ID alapján
        - update_contact(new_contact): Meglévő kontaktot frissíti Contact osztály felhasználásával.
- modules/user_manager.py: Felhasználó kezeléséért és saját készítésű adatbáziskezelő modul között hidat biztosít, ez kommunikál a nézettel és az adatbáziskezelővel, nézet nem kommunikál közvetlen az adatbáziskezelővel.
        - login(neptuncode, password): Bejelentkezés neptun kód alapján majd ennek függvényében nézet értesítése
        - get_user_name(): Aktuális felhasználó teljes neve lekérése
        - add_new_contact(): Új kontakt létrehozása majd ennek függvényében értesíti a nézetet.
        - delete_contact(id): Kontakt törlése ID alapján
        - save_contact(nid, new_lastname, new_firstname, new_postcode, new_city, new_address, new_birthday, new_phone, new_secondphopne, new_notes): Ez alapjén új Contant osztály létrehozása majd tárolása.


Home nézetben (osztályban) használt függvények: onSelect, get_contact_id(name), set_listbox_values, delete_entries, add_new, delete_contact, save_contact, load_listbox, TK kezelések

Login nézetben (osztályban) használt függvények: login, TK kezelések, messagebox meghívások
