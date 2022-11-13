import pickle
import re
from collections import UserDict
from datetime import datetime
from random import randint


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.value = [value]

    @staticmethod
    def phone_validator(verification_number):
        MIN_LEN = 9
        MAX_LEN = 13
        verification_number = (
            verification_number.replace("+", "").replace("(", "").replace(")", "")
        )
        if not (
            verification_number.isdigit()
            and (MAX_LEN >= len(verification_number) >= MIN_LEN)
        ):
            return False
        return True


class Birthday(Field):
    @staticmethod
    def birthday_validator(verification_birthday):
        today = datetime.now()
        if verification_birthday < datetime.date(today):
            return True
        return False


class Adress(Field):
    pass


class Email(Field):
    @staticmethod
    def email_validator(verification_mail):
        result = re.findall(
            r"[a-zA-Z]{1,}[\w\.]{1,}@[a-zA-Z]{2,}.[a-zA-Z]{2,}", verification_mail
        )
        if result:
            return True
        return False


class Tag(Field):
    @staticmethod
    def tags_validator(verifications_tags):
        if len(verifications_tags) == 0:
            tegs_obj = Tag(f"NoneTag-Id{randint(1111, 9999)}")
        if (
            not " " in verifications_tags
            and len(verifications_tags) > 0
            or "," in verifications_tags
        ):
            tags_list = [tag.strip() for tag in verifications_tags.split(",")]
            tags_list.sort()
            tegs_obj = Tag(str(tags_list))
        if " " in verifications_tags and not "," in verifications_tags:
            print("Separated tags by commas")
            return False
        return tegs_obj


class NoteText(Field):
    pass


class Notification:
    def __init__(self, notes: NoteText, tags: Tag = None) -> None:
        self.tags = tags
        self.notes = notes


class Record:
    def __init__(
        self,
        name: Name,
        phone: Phone,
        birthday: Birthday = None,
        adress: Adress = None,
        email: Email = None,
    ) -> None:
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.adress = adress
        self.email = email

    def change_name(self):
        new_name = Name(input("Enter new name\n"))
        new_record = Record(
            new_name, self.phone, self.birthday, self.adress, self.email
        )
        ADDRESS_BOOK.add_record(new_record)
        del ADDRESS_BOOK[self.name.value]
        return "Name successfully changed."

    def change_phone(self):
        old_phone = input("Enter phone that you want to edit\n")
        index = self.phone.value.index(old_phone)
        if not old_phone in self.phone.value:
            return "Phone not found"

        new_phone = input("Enter new phone\n")

        if Phone.phone_validator(new_phone):
            self.phone.value.pop(index)
            self.phone.value.append(new_phone)
            return f"Phone successfully changed from {old_phone} --> {new_phone}"
        else:
            return "Incorrect phone"

    def change_birthday(self):

        new_birthday = input("Enter new birthday\n")

        if Birthday.birthday_validator(new_birthday):
            self.birthday = Birthday(new_birthday)
            return "Birthday successfully changed."
        else:
            return "Incorrect birthday"

    def change_adress(self):

        new_adress = Adress(input("Enter new adress\n"))
        self.adress = new_adress
        return "Adress successfully changed."

    def change_email(self):

        new_email = input("Enter new email\n")

        if Email.email_validator(new_email):
            self.email = new_email
            return "Email successfully changed."
        else:
            return "Incorrect email"


class RecordLoadFile:
    def write_contacts_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)

    def read_contacts_from_file(self, filename):
        try:
            with open(filename, "rb") as file:
                contacts_archive = pickle.load(file)
                return contacts_archive
        except FileNotFoundError:
            pass


class AdressBook(UserDict, RecordLoadFile):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


class NoteBook(UserDict, RecordLoadFile):
    def add_note(self, notification: Notification):
        self.data[notification.tags.value] = notification


NOTE_BOOK = NoteBook()
ADDRESS_BOOK = AdressBook()
