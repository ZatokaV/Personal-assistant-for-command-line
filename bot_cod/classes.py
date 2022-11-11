from collections import UserDict
import re
from datetime import datetime
from string import ascii_letters



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
        if len(verification_number) > 17:
            return False
        for i in verification_number:
            if i in ascii_letters:
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
        result = re.findall(r"[a-zA-Z]{1,}[\w\.]{1,}@[a-zA-Z]{2,}.[a-zA-Z]{2,}", verification_mail)
        if result:    
            return True
        return False


class Teg(Field):
    pass


class Note(Field):
    pass

class Notification:
    def __init__(self, notes: Note, tegs: Teg = None) -> None:
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
        notifications: Notification = None,
    ) -> None:
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.adress = adress
        self.email = email
        self.notifications = [notifications]
    
    def change_name(self):
        new_name = Name(input("Enter new name\n"))
        new_record = Record(new_name,self.phone,self.birthday,self.adress,self.email,self.notifications)
        ADDRESS_BOOK.add_record(new_record) 
        del ADDRESS_BOOK[self.name.value] # так як ключ до record в ADRESS_BOOK це record.name.value то я не можу просто змінити self.name
        return "Name successfully changed."# бо вийде так, що доступ до контакну з новим name буде тільки по старому name. 
        

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
    


class AdressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def record_book_to_file(self):
        pass

    def read_book_from_file(self):
        pass


ADDRESS_BOOK = AdressBook()
