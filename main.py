from functions import (
    add_adress,
    add_birthday,
    add_email,
    add_phone,
    create_contact,
    delete_contact,
    edit_contact,
    hello_message,
    searcher_people,
    show_all,
    show_bday_names,
    notifications
)
from sorter_files import main_sortuvalka
from spellchecker import SpellChecker

instructions = """
Add a new contact: "add" 
Add other phone for contact: "phone"
Add contact address: "address"
Add e-mail: "email"
Add date of birth: "birthday"
Edit contact: "edit"
Show all records: "all"
Operations with notes: "note"
For sorting files on you PC: "sort"
See this message again: "help"
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
    "note": notifications
}


def main():

    print(instructions)

    while True:
        user_message = input("...\n").lower()

        if user_message.endswith(" "):
            user_message = user_message.rstrip()
        if not user_message or user_message.startswith(" "):
            continue

        if user_message in ("good bye", "close", "exit"):
            print("Good bye!")
            break

        if user_message in USER_INPUT:
            USER_INPUT[user_message]()

        if user_message not in USER_INPUT:
            my_functions = list(USER_INPUT.keys())
            my_functions.extend(["good bye", "close", "exit"])
            spell = SpellChecker()
            suggestions = spell.candidates(user_message)
            for suggest in suggestions:
                if suggest in my_functions:
                    print(f"{user_message} is not a right function, maybe you mean: '{suggest}'?")
                    break
                if len(user_message) <= 2:
                    print(f"{user_message} is not a right function, maybe you mean: 'add' or 'all'?")
                    break
            else:
                print(f"Sorry can't execute this function: {user_message}")

if __name__ == "__main__":
    main()
