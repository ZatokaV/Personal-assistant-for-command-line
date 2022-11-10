from collections import UserDict


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


class Tegs(Field):
    pass


class Notes(Field):
    pass


class Notifications:
    def __init__(self, notes: Notes, tegs: Tegs = None) -> None:
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
        self.data[record.name.value] = record

    def record_book_to_file(self):
        pass

    def read_book_from_file(self):
        pass


ADDRESS_BOOK = AdressBook()
