from datetime import datetime as dt
from random import randint
from calendar import isleap


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
    name = input("For which contact should I add e-mail?\n").capitalize()
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        email = input(f"Enter e-mail for {name.capitalize()}\n")
        if Email.email_validator(email):
            email_obj = Email(email)
            ADDRESS_BOOK[name].email = email_obj
            print(
                f"E-mail {email} has been added to contact {name.capitalize()}")
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
        if len(birthday) == 3:  # date parts
            try:
                person_birthday = dt(
                    year=int(birthday[0]), month=int(birthday[1]), day=int(birthday[2])
                ).date()
                if Birthday.birthday_validator(person_birthday):
                    ADDRESS_BOOK[name].birthday = Birthday(person_birthday)
                    print(
                        f"Date of birth {person_birthday} added for the contact {name.capitalize()}"
                    )
                else:
                    print("Error validating birth date")
            except:
                print("Birth date creation error")
        else:
            print("Invalid date")


def days_to_birthday(birthday) -> int:
    next_birthday = None
    Feb29_birthdate = False
    if birthday.month == 2 and birthday.day == 29 \
            and not isleap(dt.now().year):
        Feb29_birthdate = True
        birthday_this_year = dt(dt.now().year, 2, 28).date()
    else:
        birthday_this_year = dt(
            dt.now().year,
            birthday.month,
            birthday.day
        ).date()
    # if the birthday this year already occurred take the next year
    if birthday_this_year < dt.date(dt.now()):
        next_birthday = birthday_this_year.replace(
            year=birthday_this_year.year+1)
        if Feb29_birthdate and isleap(next_birthday.year):
            next_birthday = birthday_this_year.replace(
                day=birthday_this_year.day+1)
    else:
        next_birthday = birthday_this_year
    return (next_birthday - dt.now().date()).days


# виводити список контактів, у яких день народження через
# задану кількість днів від поточної дати;
def show_bday_names():
    days_from_today = int(input(
        "For what number of days from today should I show contacts with birthday?\n"))
    for name, record in ADDRESS_BOOK.items():
        if record.birthday:
            if days_to_birthday(record.birthday.value) <= days_from_today:
                show_contact(record)


# здійснювати пошук контактів з книги контактів;
# Воно працює наступним чином: воно виведе юзеру всі контакти в яких щось співпало з тим, що вів юзер.
def searcher_people():
    ueser_input = input("Input something that record contains\n")
    search_result = list()
    for record in ADDRESS_BOOK.data.values():

        list_contacts = list()
        # перевірки на True потрібні, бо в деяких контактах може не бути деяких показників
        if record.name:
            list_contacts.append(record.name.value)

        if record.phone:
            list_contacts.append(", ".join(record.phone.value))

        if record.adress:
            list_contacts.append(record.adress.value)

        if record.email:
            list_contacts.append(record.email.value)

        if record.birthday:
            list_contacts.append(record.birthday.value)

        string = "| ".join(list_contacts)

        if ueser_input in string:
            search_result.append(string)
    return print("\n".join(search_result))


# + готово, працює
# редагування контакту
def edit_contact():
    name = input("For which contact I should edit\n")
    if not name in ADDRESS_BOOK.data:
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
    user_input = input("Enter contact that you want to delete\n")

    if not user_input in ADDRESS_BOOK:
        return print("Contact not exist")

    del ADDRESS_BOOK[user_input]

    print("Contact susesfully delete")


# + готово, працює
# здійснювати пошук нотаток
def searcher_notes():
    key_word = input("Enter a keyword or part to search in notes\n...")
    for notes in NOTE_BOOK.values():
        if key_word in notes.tags.value:
            print(f"Found by tags:\n{notes.tags.value}\n\t{notes.notes.value}")
        elif key_word in notes.notes.value:
            print(
                f"Found in note texts:\n{notes.tags.value}\n\t{notes.notes.value}")


# Вивід інформації для одного контакту
def show_contact(record: Record):
    print(record.name.value.capitalize())
    print(f"\t{record.phone.value}")
    if record.email:
        print(f"\t{record.email.value}")
    if record.adress:
        print(f"\t{record.adress.value}")
    if record.birthday:
        print(f"\t{record.birthday.value}")


# + готово, працює
# Вивід всіх контактів, з усією наявною інформацією (окрім нотаток)
def show_all():
    for record in ADDRESS_BOOK.values():
        show_contact(record)
        """
        print(records.name.value.capitalize())
        print(f"\t{records.phone.value}")
        if records.email:
            print(f"\t{records.email.value}")
        if records.adress:
            print(f"\t{records.adress.value}")
        if records.birthday:
            print(f"\t{records.birthday.value}")
        """


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
        number_note_to_del = input(
            "Enter the note number you want to delete\n...")
        if int(number_note_to_del) in temp_dict:
            for notes in NOTE_BOOK.values():
                if temp_dict[int(number_note_to_del)] == notes.notes.value:
                    key_for_del = notes.tags.value

            NOTE_BOOK.pop(key_for_del)
            print("Done!")

    if action == "3":
        for notes in NOTE_BOOK.values():
            print(f"{notes.tags.value}\n\t{notes.notes.value}")


def recreate_contacts():
    contacts_in_file = ADDRESS_BOOK.read_contacts_from_file(
        "data_phonebook.bin")
    if contacts_in_file:
        for key, value in contacts_in_file.items():
            ADDRESS_BOOK.data[key] = value


def recreate_notes():
    notes_in_file = NOTE_BOOK.read_contacts_from_file("data_notebook.bin")
    if notes_in_file:
        for key, value in notes_in_file.items():
            NOTE_BOOK.data[key] = value
