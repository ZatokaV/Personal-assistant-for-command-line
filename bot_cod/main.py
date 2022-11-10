from functions import (
    add_adress,
    add_birthday,
    add_email,
    add_note,
    add_phone,
    create_contact,
    delete_contact,
    edit_contact,
    hello_message,
    searcher_notes,
    searcher_people,
    show_all,
    show_bday_names,
)

instructions = """
Add a new contact: "add" 
Add other phone for contact: "phone"
Add contact address: "address"
Add e-mail: "email"
Add date of birth: "birthday"

Show all records: "all"
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


if __name__ == "__main__":
    main()
