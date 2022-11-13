from calendar import isleap
from datetime import datetime as dt

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
from spellchecker import SpellChecker


def hello_message():
    print("How can I help you?")


def create_contact():
    name = input("Enter the name of the new contact\n")
    if Name.name_validator(name):
        name_obj = Name(name)
        phone = input(f"Enter the phone number for {name}\n")
        if Phone.phone_validator(phone):
            phone_obj = Phone(phone)
            new_contact = Record(name=name_obj, phone=phone_obj)
            ADDRESS_BOOK.add_record(new_contact)
            print(f"Contact {name.capitalize()} with phone {phone} added!")
        else:
            print("Error. Valid number: 7 to 13 digits. Letters cannot be included in the number")


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


def add_adress():
    name = input("For which contact should I add an address?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        address = input(f"Add address for {name.capitalize()}\n")
        address_obj = Adress(address)
        ADDRESS_BOOK[name].adress = address_obj
        print(f"Address {address} is added for contact {name.capitalize()}")


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


def add_birthday():
    name = input("For which contact should I add a date of birth?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        birthday = input("Enter YYYY/MM/DD" "\n").split("/")
        if len(birthday) == 3:
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
    if birthday.month == 2 and birthday.day == 29 and not isleap(dt.now().year):
        Feb29_birthdate = True
        birthday_this_year = dt(dt.now().year, 2, 28).date()
    else:
        birthday_this_year = dt(dt.now().year, birthday.month, birthday.day).date()
    if birthday_this_year < dt.date(dt.now()):
        next_birthday = birthday_this_year.replace(year=birthday_this_year.year + 1)
        if Feb29_birthdate and isleap(next_birthday.year):
            next_birthday = birthday_this_year.replace(day=birthday_this_year.day + 1)
    else:
        next_birthday = birthday_this_year
    return (next_birthday - dt.now().date()).days


def show_bday_names():
    days_from_today = int(
        input(
            "For what number of days from today should I show contacts with birthday?\n"
        )
    )
    for name, record in ADDRESS_BOOK.items():
        if record.birthday:
            if days_to_birthday(record.birthday.value) <= days_from_today:
                show_contact(record)


def searcher_people():
    ueser_input = input("Input something that record contains\n")
    search_result = list()
    for record in ADDRESS_BOOK.data.values():

        list_contacts = list()
        if record.name:
            list_contacts.append(record.name.value)

        if record.phone:
            list_contacts.append(", ".join(record.phone.value))

        if record.adress:
            list_contacts.append(record.adress.value)

        if record.email:
            list_contacts.append(record.email.value)

        if record.birthday:
            list_contacts.append(str(record.birthday.value))

        string = "| ".join(list_contacts)

        if ueser_input in string:
            search_result.append(string)
    return print("\n".join(search_result))


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
            "What you want to edit (name, phone, birthday, address, email)\n"
        )

        if parameter in parameters_to_edit:
            output = parameters_to_edit[parameter]()
            print(output)
        else:
            print("Incorrect parameter")


def delete_contact():
    user_input = input("Enter contact that you want to delete\n")

    if not user_input in ADDRESS_BOOK:
        return print("Contact not exist")

    del ADDRESS_BOOK[user_input]

    print("Contact successfully delete")


def searcher_notes():
    key_word = input("Enter a keyword or part to search in notes\n...")
    for notes in NOTE_BOOK.values():
        if key_word in notes.tags.value:
            print(f"Found by tags:\n{notes.tags.value}\n\t{notes.notes.value}")
        elif key_word in notes.notes.value:
            print(f"Found in note texts:\n{notes.tags.value}\n\t{notes.notes.value}")


def show_contact(record: Record):
    print(record.name.value.capitalize())
    print(f"\t{record.phone.value}")
    if record.email:
        print(f"\t{record.email.value}")
    if record.adress:
        print(f"\t{record.adress.value}")
    if record.birthday:
        print(f"\t{record.birthday.value}")


def show_all():
    for record in ADDRESS_BOOK.values():
        show_contact(record)


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
        if Tag.tags_validator(tags):
            tags_obj = Tag.tags_validator(tags)
        else:
            print("Incorrect tags")
            return False

        note_record = Notification(notes=text_note_obj, tags=tags_obj)
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


def edit_note():
    action = input(
        "What do you want to edit?\nEnter 1 - tags\nEnter 2 - note text\n..."
    )

    if action == "1":
        temp_dict = {}
        items_for_user = [
            f"{notes.tags.value} | {notes.notes.value}" for notes in NOTE_BOOK.values()
        ]
        for i, item in enumerate(items_for_user):
            print(i + 1, item)
        items_for_program = [notes.tags.value for notes in NOTE_BOOK.values()]
        for i, item in enumerate(items_for_program):
            temp_dict[i + 1] = item
        number_note_to_edit = input("Enter the note number you want to edit tags\n...")
        if int(number_note_to_edit) in temp_dict:
            for notes in NOTE_BOOK.values():
                if temp_dict[int(number_note_to_edit)] == notes.tags.value:
                    note_text_obj = notes.notes
                    key_for_edit = notes.tags.value

        new_tags = input("Enter new tags for your note\n...")

        if Tag.tags_validator(new_tags):
            tags_obj = Tag.tags_validator(new_tags)
        else:
            print("Incorrect tags")
            return False

        edited_note_obj = Notification(notes=note_text_obj, tags=tags_obj)
        NOTE_BOOK.pop(key_for_edit)
        NOTE_BOOK.add_note(edited_note_obj)
        print("Tags have been changed!")

    if action == "2":
        temp_dict = {}
        items = [notes.notes.value for notes in NOTE_BOOK.values()]
        for i, item in enumerate(items):
            print(i + 1, item)
            temp_dict[i + 1] = item
        number_note_to_edit = input("Enter the note number you want to edit\n...")
        if int(number_note_to_edit) in temp_dict:
            for notes in NOTE_BOOK.values():
                if temp_dict[int(number_note_to_edit)] == notes.notes.value:
                    key_for_edit = notes.tags.value
                    tags_obj = notes.tags

        new_notetext = input("Enter new note text:\n...")
        new_notetext_obj = NoteText(new_notetext)
        edited_note_obj = Notification(notes=new_notetext_obj, tags=tags_obj)
        NOTE_BOOK.pop(key_for_edit)
        NOTE_BOOK.add_note(edited_note_obj)


def recreate_contacts():
    contacts_in_file = ADDRESS_BOOK.read_contacts_from_file("data_phonebook.bin")
    if contacts_in_file:
        for key, value in contacts_in_file.items():
            ADDRESS_BOOK.data[key] = value


def recreate_notes():
    notes_in_file = NOTE_BOOK.read_contacts_from_file("data_notebook.bin")
    if notes_in_file:
        for key, value in notes_in_file.items():
            NOTE_BOOK.data[key] = value


def get_help(instructions: str):
    print(instructions)


def incorrect_input(user_message: str, user_input: dict):
    my_functions = list(user_input.keys())
    my_functions.extend(["good bye", "close", "exit"])
    spell = SpellChecker()
    suggestions = spell.candidates(user_message)
    if suggestions:
        for suggest in suggestions:
            if suggest in my_functions:
                print(
                    f"{user_message} is not a right function, maybe you mean: '{suggest}'?"
                )
                break
            if len(user_message) <= 2:
                print(
                    f"{user_message} is not a right function, maybe you mean: 'add' or 'all'?"
                )
                break
        else:
            print(f"Sorry can't execute this function: {user_message}.")
    else:
        print(f"Sorry don't know this command: {user_message}")
