from functions import (
    hello_message,
    create_contact,
    add_phone,
    add_adress,
    add_email,
    add_birthday,
    add_note,
    show_bday_names,
    searcher_people,
    searcher_notes,
    edit_contact,
    delete_contact,
    show_all
)


instructions = """
Add a new contact: "add" 
Add other phone for contact: "phone"
Add contact address: "address"

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
    "all": show_all
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
