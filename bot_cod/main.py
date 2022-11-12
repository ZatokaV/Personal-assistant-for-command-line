from functions import (
    add_adress,
    add_birthday,
    add_email,
    add_phone,
    create_contact,
    delete_contact,
    edit_contact,
    hello_message,
    notifications,
    recreate_contacts,
    searcher_notes,
    searcher_people,
    show_all,
    show_bday_names,
    recreate_notes,
)
from sorter_files import main_sortuvalka
from classes import ADDRESS_BOOK, NOTE_BOOK

instructions = """
Phone book:
Add a new contact: "add" 
Add other phone for contact: "phone"
Add contact address: "address"
Add e-mail: "email"
Add date of birth: "birthday"
Edit contact: "edit"
Show all records: "all"

Note book:
Operations with notes: "note"
Search in notes: "findnote"

Files on PC:
For sorting files on you PC: "sort"

See this message again: "help"

Save and exit: "good bye", "close", "exit"
"""


def get_help():
    print(instructions)


USER_INPUT = {
    "hello": hello_message,
    "add": create_contact,
    "phone": add_phone,
    "address": add_adress,
    "email": add_email,
    "birthday": add_birthday,
    "all": show_all,
    "edit": edit_contact,
    "sort": main_sortuvalka,
    "note": notifications,
    "findnote": searcher_notes,
}


def main():

    print(instructions)
    recreate_contacts()
    recreate_notes()

    while True:
        user_message = input("...\n").lower()

        if user_message.endswith(" "):
            user_message = user_message.rstrip()
        if not user_message or user_message.startswith(" "):
            continue

        if user_message in ("good bye", "close", "exit"):
            print("Good bye!")
            ADDRESS_BOOK.write_contacts_to_file("data_phonebook.bin")
            NOTE_BOOK.write_contacts_to_file("data_notebook.bin")
            break

        if user_message in USER_INPUT:
            USER_INPUT[user_message]()


if __name__ == "__main__":
    main()
