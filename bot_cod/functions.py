from classes import ADRESS_BOOK, Record, Phone, Name


def hello_message():
    print("How can I help you?")


# + Готово, працює
# Створення контакту
def create_contact():
    name = input("Enter the name of the new contact\n")
    if name in ADRESS_BOOK:
        print("Such a contact already exists")
    else:
        name_obj = Name(name)
        phone = input(f"Enter the phone number for {name}\n")
        if Phone.phone_validator(phone):            
            phone_obj = Phone(phone)
            new_contact = Record(name=name_obj, phone=phone_obj)
            ADRESS_BOOK.add_record(new_contact)
            print(f"Contact {name.capitalize()} with phone {phone} added!")
        else:
            print("Invalid number")

# + Готово, працює
# Додавання телефону
def add_phone():
    name = input("For which contact should I add another number?\n")
    if name not in ADRESS_BOOK:
        print("No such contact exists!")
    else:
        new_phone = input(f"Enter new phone number for {name.capitalize()}\n")
        if Phone.phone_validator(new_phone):
            ADRESS_BOOK[name].phone.value.append(new_phone)
            print(
                f"Phone number {new_phone} has been added to contact {name.capitalize()}"
            )
        else:
            print("Invalid number")


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
    for records in ADRESS_BOOK.values():
        print(records.name.value.capitalize())
        print(f"\t{records.phone.value}")
        if records.email:
            print(f"\t{records.email.value}")
        if records.adress:
            print(f"\t{records.adress.value}")
        if records.birthday:
            print(f"\t{records.birthday.value}")
