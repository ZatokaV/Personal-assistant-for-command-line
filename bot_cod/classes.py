from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def phone_validator():
        pass


class Birthday(Field):
    def birthday_validator():
        pass


class Adress(Field):
    pass


class Email(Field):
    def email_validator():
        pass


class Tegs:
    pass


class Notes:
    pass


class Notifications(Field):
    def __init__(self, tegs: Tegs = None, notes: Notes = None) -> None:
        self.tegs = tegs
        self.notes = notes


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
        self.data[record.name] = record

    def record_book_to_file(self):
        pass

    def read_book_from_file(self):
        pass


ADRESS_BOOK = AdressBook()
