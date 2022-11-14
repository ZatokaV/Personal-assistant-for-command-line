import pickle
import re
from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value



class Name(Field):
    def __init__(self, value):
        self.value = value

    @Field.value.setter
    def value(self, value):
        if not value:
            raise ValueError('The "name" field cannot be empty')
        if value in ADDRESS_BOOK:
            raise ValueError("Such a contact already exists")
        if value.isdigit():
            raise ValueError("The name cannot consist only of numbers")
        self._value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value

    @Field.value.setter
    def value(self, value):
        MIN_LEN = 7
        MAX_LEN = 13
        value = value.replace("+", "").replace("(", "").replace(")", "")
        if not (value.isdigit() and (MAX_LEN >= len(value) >= MIN_LEN)):
            raise ValueError
        self._value = [value]


class Birthday(Field):
    def __init__(self, value):
        self.value = value
    
    @Field.value.setter
    def value(self, value):
        today = datetime.now()
        if value > datetime.date(today):
            raise ValueError
        self._value = value


class Adress(Field):
    pass


class Email(Field):
    def __init__(self, value):
        self.value = value
    
    @Field.value.setter
    def value(self, value):
        result = re.findall(
            r"[a-zA-Z]{1,}[\w\.]{1,}@[a-zA-Z]{2,}.[a-zA-Z]{2,}", value
        )
        if not result:
            raise ValueError
        self._value = value


class Tag(Field):
    def __init__(self, value):
        self.value = value
    
    @Field.value.setter
    def value(self, value):
        if not value:
            tegs = f"NoneTag-{datetime.now().strftime('%m/%d/%Y, %H:%M')}"
        if (
            " " not in value
            and value
            or "," in value
        ):
            tegs = [tag.strip() for tag in value.split(",")]
            tegs.sort()
            tegs = str(tegs)
            
        if " " in value and "," not in value:
            print("Separated tags by commas")
            raise ValueError
        self._value = tegs


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

    def change_name(self,new_name):

        new_name_obj = Name(new_name)

        new_record = Record(
            new_name_obj, self.phone, self.birthday, self.adress, self.email
            )

        del ADDRESS_BOOK[self.name.value]
        ADDRESS_BOOK.add_record(new_record)
        return "Name successfully changed."
        

    def change_phone(self,old_phone,new_phone): #ПОТРІБНО ПЕРЕПИСАТИ, ЯКЩО логіка класу буде змінена!!!
       
        index = self.phone.value.index(old_phone)
    
        self.phone.value.pop(index)
        self.phone.value.append(new_phone)
        return f"Phone successfully changed from {old_phone} --> {new_phone}"
   
      

    def change_birthday(self,new_birthday):

        if len(new_birthday) == 3:
            try:
                person_birthday = datetime(
                    year=int(new_birthday[0]),
                    month=int(new_birthday[1]),
                    day=int(new_birthday[2]),
                ).date()
                
                self.birthday = Birthday(person_birthday)
                return "Birthday successfully changed."
               
            except:
                print("Birth date creation error")
        else:
            print("Invalid date")

    def change_adress(self,new_adress):
        self.adress = Adress(new_adress)
        return "Adress successfully changed."

    def change_email(self,new_email):
        self.email = Email(new_email)
        return "Email successfully changed."
       


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
