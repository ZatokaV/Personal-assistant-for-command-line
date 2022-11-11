from collections import UserDict
import re

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
        return True


class Birthday(Field):
    @staticmethod
    def birthday_validator(verification_birthday):
        return True


class Adress(Field):
    pass


class Email(Field):
    @staticmethod
    def email_validator(verification_mail):
        return True


class Tags(Field):
    pass


class Note(Field):
    
    def __init__(self, tags: list = None):
        self.tags = []
    
    def change_text(self, new_value):
        self.value = new_value
        
    def find_text(self, text):
        
        value = self.value
        match = re.fullmatch(text, value)
        if match:
            return value
        
    def add_tags(self, tags):
        
        self.tags.extend(tags)
        tags = str(tags)
        clean_tags = re.sub(r"\[|\]", '', tags)
        return f"{clean_tags} were added"


class Notifications:
    
    def __init__(self, notes: list,) -> None:
        self.notes = []
    
    def add_notes(self, notes: list):
        ...

class Record:
    def __init__(
        self,
        name: Name,
        phone: Phone,
        birthday: Birthday = None,
        adress: Adress = None,
        email: Email = None,
        notifications: Notifications = None,
    ) -> None:
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.adress = adress
        self.email = email
        self.notifications = notifications


class AdressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def record_book_to_file(self):
        pass

    def read_book_from_file(self):
        pass


ADDRESS_BOOK = AdressBook()
