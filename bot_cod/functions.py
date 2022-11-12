from datetime import datetime as dt
from random import randint

from classes import (
    ADDRESS_BOOK,
    NOTE_BOOK,
    Adress,
    Birthday,
    Email,
    Name,
    NoteText,
    Notification,
    Phone,
    Record,
    Tag,
)


def hello_message():
    print("How can I help you?")


# + Готово, працює
# Створення контакту
def create_contact():
    name = input("Enter the name of the new contact\n")
    if len(name) == 0:
        print('The "name" field cannot be empty')
        return False
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
            print("The number should not contain letters or the number is too long!")


# + Готово, працює
# Додавання телефону
def add_phone():
    name = input("For which contact should I add another number?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        new_phone = input(f"Enter new phone number for {name.capitalize()}\n")
        if Phone.phone_validator(new_phone):
            if new_phone not in ADDRESS_BOOK[name].phone.value:
                ADDRESS_BOOK[name].phone.value.append(new_phone)
                print(
                    f"Phone number {new_phone} has been added to contact {name.capitalize()}"
                )
            else:
                print("The number is duplicated")
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

# + готово, працює
# редагування контакту
def edit_contact():
    name = input("For which contact I should edit\n")
    if name not in ADDRESS_BOOK.data:
        print("No such contact exists!")
    else:
        record = ADDRESS_BOOK[name]

        parameters_to_edit = {
            "name": record.change_name,
            "phone": record.change_phone,
            "birthday": record.change_birthday,
            "adress": record.change_adress,
            "email": record.change_email,
        }
        parameter = input(
            "What you want to edit (name, phone, birthday, adress, email)\n"
        )

        if parameter in parameters_to_edit:
            output = parameters_to_edit[parameter]()
            print(output)
        else:
            print("Incorrect parameter")


# видаляти записи з книги контактів
def delete_contact():
    pass


# + готово, працює
# здійснювати пошук нотаток
def searcher_notes():
    key_word = input("Enter a keyword or part to search in notes\n...")
    for notes in NOTE_BOOK.values():
        if key_word in notes.tags.value:
            print(f"Found by tags:\n{notes.tags.value}\n\t{notes.notes.value}")
        elif key_word in notes.notes.value:
            print(f"Found in note texts:\n{notes.tags.value}\n\t{notes.notes.value}")


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


# + готово, працює, але страшно мені не подобається
# Додавання нотаток, видалення нотаток, перегляд всіх нотаток
def notifications():
    action = input(
        "Actions with notes:\nEnter 1 to add a note\nEnter 2 to delete note\nEnter 3 to show all notes\n..."
    )
    if action == "1":
        text_note = input("Enter note text\n...")
        text_note_obj = NoteText(text_note)
        tags = input(
            "Not necessary. Enter tags for the note. (can be several, separated by commas)\n..."
        )
        if len(tags) == 0:
            tegs_obj = Tag(f"NoneTag-Id{randint(1111, 9999)}")
        if not " " in tags and len(tags) > 0 or "," in tags:
            tags_list = [tag.strip() for tag in tags.split(",")]
            tags_list.sort()
            tegs_obj = Tag(str(tags_list))
        if " " in tags and not "," in tags:
            print("Separated tags by commas")
            return False

        note_record = Notification(notes=text_note_obj, tags=tegs_obj)
        NOTE_BOOK.add_note(note_record)
        print(f'Added note "{text_note}"')

    if action == "2":
        temp_dict = {}
        items = [notes.notes.value for notes in NOTE_BOOK.values()]
        for i, item in enumerate(items):
            print(i + 1, item)
            temp_dict[i + 1] = item
        number_note_to_del = input("Enter the note number you want to delete\n...")
        if int(number_note_to_del) in temp_dict:
            for notes in NOTE_BOOK.values():
                if temp_dict[int(number_note_to_del)] == notes.notes.value:
                    key_for_del = notes.tags.value

            NOTE_BOOK.pop(key_for_del)
            print("Done!")

    if action == "3":
        for notes in NOTE_BOOK.values():
            print(f"{notes.tags.value}\n\t{notes.notes.value}")
