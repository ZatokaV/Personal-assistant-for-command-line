from collections import UserDict


class Name:
    pass


class Phone:
    pass


class Birthday:
    pass


class Adress:
    pass


class Email:
    pass


class Birthday:
    pass


class Tegs:
    pass


class Notes:
    pass


class Notifications:
    def __init__(self, tegs: Tegs = None, notes: Notes = None) -> None:
        self.tegs = tegs
        self.notes = notes


class Record:
    def __init__(
        self,
        name: Name,
        phone: Phone = None,
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
    pass


ADRESS_BOOK = AdressBook()
