from classes import ADRESS_BOOK, Record


def hello_message():
    print("How can I help you?")


# Створення контакту
def create_contact():
    name = input("Enter the name of the new contact\n")
    if name in ADRESS_BOOK:
        print("Such a contact already exists")
        return False
    else:
        phone = input(f"Enter the phone number for {name}\n")
        new_contact = Record(name=name, phone=phone)
        ADRESS_BOOK.add_record(new_contact)
    print(
        f"Contact {ADRESS_BOOK[name].name} with phone {ADRESS_BOOK[name].phone} added!"
    )


# Додавання телефону
def add_phone():
    pass


# Додавання адреси
def add_adress():
    pass


# додавання імейлу
def add_email():
    pass


# додавання дня народження
def add_birthday():
    pass


# виводити список контактів, у яких день народження через
# задану кількість днів від поточної дати;
def show_bday_names():
    pass


# здійснювати пошук контактів з книги контактів;
def searcher_people():
    pass


# видаляти записи з книги контактів
def delete_contact():
    pass


# додавання нотатки
def add_note():
    pass


# здійснювати пошук нотаток
def searcher_notes():
    pass


# здійснювати сортування нотаток за ключовими словами (тегами)
def sorting_notes():
    pass
