from datetime import datetime as dt

from classes import ADDRESS_BOOK, Adress, Birthday, Email, Name, Phone, Record


def hello_message():
    print("How can I help you?")


# + Готово, працює
# Створення контакту
def create_contact():
    name = input("Enter the name of the new contact\n")
    if name in ADDRESS_BOOK:
        print("Such a contact already exists")
    else:
        name_obj = Name(name)
        phone = input(f"Enter the phone number for {name}\n")
        if Phone.phone_validator(phone):
            phone_obj = Phone(phone)
            new_contact = Record(name=name_obj, phone=phone_obj)
            ADDRESS_BOOK.add_record(new_contact)
            print(f"Contact {name.capitalize()} with phone {phone} added!")
        else:
            print("Invalid number")


# + Готово, працює
# Додавання телефону
def add_phone():
    name = input("For which contact should I add another number?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        new_phone = input(f"Enter new phone number for {name.capitalize()}\n")
        if Phone.phone_validator(new_phone):
            ADDRESS_BOOK[name].phone.value.append(new_phone)
            print(
                f"Phone number {new_phone} has been added to contact {name.capitalize()}"
            )
        else:
            print("Invalid number")


# + Готово, працює
# Додавання адреси
def add_adress():
    name = input("For which contact should I add an address?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        address = input(f"Add address for {name.capitalize()}\n")
        address_obj = Adress(address)
        ADDRESS_BOOK[name].adress = address_obj
        print(f"Address {address} is added for contact {name.capitalize()}")


# + Готово, працює
# додавання імейлу
def add_email():
    name = input("For which contact should I add e-mail?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        email = input(f"Enter e-mail for {name.capitalize()}\n")
        if Email.email_validator(email):
            email_obj = Email(email)
            ADDRESS_BOOK[name].email = email_obj
            print(f"E-mail {email} has been added to contact {name.capitalize()}")
        else:
            print("Invalid e-mail")


# + Готово, працює
# додавання дня народження
def add_birthday():
    name = input("For which contact should I add a date of birth?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        birthday = input("Enter YYYY/MM/DD" "\n").split("/")
        person_birthday = dt(
            year=int(birthday[0]), month=int(birthday[1]), day=int(birthday[2])
        )
        person_birthday = dt.date(person_birthday)
        if Birthday.birthday_validator(person_birthday):
            birthday_obj = Birthday(person_birthday)
            ADDRESS_BOOK[name].birthday = birthday_obj
            print(
                f"Date of birth {person_birthday} added for contact {name.capitalize()}"
            )
        else:
            print("Invalid date")


# виводити список контактів, у яких день народження через
# задану кількість днів від поточної дати;
def show_bday_names():
    pass


# здійснювати пошук контактів з книги контактів;
def searcher_people():
    pass


# редагування контакту
def edit_contact():
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


# + готово, працює
# Вивід всіх контактів, з усією наявною інформацією (окрім нотаток)
def show_all():
    for records in ADDRESS_BOOK.values():
        print(records.name.value.capitalize())
        print(f"\t{records.phone.value}")
        if records.email:
            print(f"\t{records.email.value}")
        if records.adress:
            print(f"\t{records.adress.value}")
        if records.birthday:
            print(f"\t{records.birthday.value}")
