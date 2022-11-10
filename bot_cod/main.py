from classes import ADRESS_BOOK
from functions import hello_message, create_contact

USER_INPUT = {
    "hello": hello_message,
    "add": create_contact,
}


def main():
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
