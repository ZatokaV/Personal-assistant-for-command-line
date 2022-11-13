from classes import ADDRESS_BOOK, NOTE_BOOK
from functions import (
    add_adress,
    add_birthday,
    add_email,
    add_phone,
    create_contact,
    delete_contact,
    edit_contact,
    edit_note,
    hello_message,
    notifications,
    recreate_contacts,
    recreate_notes,
    searcher_notes,
    searcher_people,
    show_all,
    show_bday_names,
)
from sorter_files import main_sortuvalka
from spellchecker import SpellChecker

instructions = """
Phone book:
Add a new contact: "add" 
Add other phone for contact: "phone"
Add contact address: "address"
Add e-mail: "email"
Add date of birth: "birthday"
Birthday alerts for your contacts:"bdays"
Edit contact: "edit"
Show all records: "all"
Search in records: "search"
Delet record: "delete"

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
    
def incorrect_input(user_message):
    my_functions = list(USER_INPUT.keys())
    my_functions.extend(["good bye", "close", "exit"])
    spell = SpellChecker()
    suggestions = spell.candidates(user_message)
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
        print(f"Sorry can't execute this function: {user_message}")



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
    "delete": delete_contact,
    "search": searcher_people,
    "bdays": show_bday_names,
    "help": get_help,
    "noteedit": edit_note,
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

        if user_message not in USER_INPUT:
            incorrect_input(user_message)

if __name__ == "__main__":
    main()
