from CODE_CRAFTERS_CORE.Record import Record
from CODE_CRAFTERS_CORE.RecordData import *
from collections import UserList
from tabulate import tabulate
from emoji import emojize
import pickle


class AddressBook(UserList):
    def __init__(self):
        self.data=[]
        self.id = 1


    def birthdays(self, days):
        result = []
        for contact in self.data:
            compare = contact.days_to_birthday()
            if str(compare) == days:
                result.append(contact)
        print(result)

                                  
    def save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"{bcolors.GREEN}💾 Contacts added to:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")

    def read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            print(f"{bcolors.GREEN}📖 Reading contacts from:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
            return pickle.load(file)

        

                
