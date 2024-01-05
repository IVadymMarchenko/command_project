from abc import ABC, abstractmethod
from AddressBook import *


class AbstractUserInterface(ABC):

    def __init__(self,data):
        self.data=data

    @abstractmethod
    def handle(self):
        pass





class ConsoleUI(AbstractUserInterface):

    def handle(self):
        result = self.display_contacts()
        return result

    def display_contacts(self):
        if not self.data.data:
            print(f"{bcolors.WARNING}📋 Addressbook is empty😞 {bcolors.RESET}")
            print(f"{bcolors.GREEN}🤗 But, you can add a contact if you want ✏️ {bcolors.RESET}")
            return
        else:
            print(f"{bcolors.GREEN}📖 All contacts in book:🚀 {bcolors.RESET}")
            table = []
            for contact in self.data.data:
                phone_numbers = ", ".join(
                    str(phone) for phone in contact.get("phone", [])
                )
                emails = ", ".join(str(email) for email in contact.get("email", []))
                table.append(
                    [
                        str(contact["id"]),
                        str(contact["name"]),
                        phone_numbers,
                        str(contact.get("birthday", "")),
                        emails,
                    ]
                )
            headers = [
                emojize(f":id: {bcolors.BLUE}ID{bcolors.RESET}", language="alias"),
                emojize(f":bust_in_silhouette: {bcolors.BLUE}Name{bcolors.RESET}", language="alias"),
                emojize(f":telephone_receiver: {bcolors.BLUE}Phone{bcolors.RESET}", language="alias"),
                emojize(f":birthday_cake: {bcolors.BLUE}Birthday{bcolors.RESET}", language="alias"),
                emojize(f":e-mail: {bcolors.BLUE}Email{bcolors.RESET}", language="alias"),
            ]
            print(tabulate(table, headers=headers, tablefmt='pretty'))

class GetCommand:

    def handle(self):
        result=self.display_commands()
        print(result)
        #return result

    def display_commands(self, language='en'):

        if language == 'en':
            command_list = [
                bcolors.ORANGE + "cli" + bcolors.RESET,
                bcolors.ORANGE + "change-language" + bcolors.RESET,
                bcolors.ORANGE + "contact-add" + bcolors.RESET,
                bcolors.ORANGE + "contact-find" + bcolors.RESET,
                bcolors.ORANGE + "contact-show-all" + bcolors.RESET,
                bcolors.ORANGE + "contact-phone-add" + bcolors.RESET,
                bcolors.ORANGE + "contact-phone-remove" + bcolors.RESET,
                bcolors.ORANGE + "contact-email-add" + bcolors.RESET,
                bcolors.ORANGE + "contact-email-remove" + bcolors.RESET,
                bcolors.ORANGE + "contact-phone-edit" + bcolors.RESET,
                bcolors.ORANGE + "contact-email-edit" + bcolors.RESET,
                bcolors.ORANGE + "contact-birthday-edit" + bcolors.RESET,
                bcolors.ORANGE + "contact-remove" + bcolors.RESET,
                bcolors.ORANGE + "display-birthdays" + bcolors.RESET,
                bcolors.ORANGE + "note-add" + bcolors.RESET,
                bcolors.ORANGE + "note-find" + bcolors.RESET,
                bcolors.ORANGE + "note-show-all" + bcolors.RESET,
                bcolors.ORANGE + "note-edit" + bcolors.RESET,
                bcolors.ORANGE + "note-remove" + bcolors.RESET,
                bcolors.ORANGE + "tag-add" + bcolors.RESET,
                bcolors.ORANGE + "tag-edit" + bcolors.RESET,
                bcolors.ORANGE + "tag-remove" + bcolors.RESET,
                bcolors.ORANGE + "tag-find-sort" + bcolors.RESET,
                bcolors.ORANGE + "file-sort" + bcolors.RESET,
                bcolors.ORANGE + "file-extension-show" + bcolors.RESET,
                bcolors.ORANGE + "file-extension-add" + bcolors.RESET,
                bcolors.ORANGE + "file-extension-remove" + bcolors.RESET,
                bcolors.ORANGE + "quit" + bcolors.RESET,
                bcolors.ORANGE + "exit" + bcolors.RESET,
                bcolors.ORANGE + "q" + bcolors.RESET,
            ]

            command_explain = [
                bcolors.BLUE + "виводить список всіх доступних команд" + bcolors.RESET,
                bcolors.BLUE + "змінити мову додатка" + bcolors.RESET,
                bcolors.BLUE + "зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів" + bcolors.RESET,
                bcolors.BLUE + "здійснює пошук контакту серед контактів книги" + bcolors.RESET,
                bcolors.BLUE + "показує всі існуючі контакти в книзі контактів" + bcolors.RESET,
                bcolors.BLUE + "додати іще 1-ин phone до існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючого phone" + bcolors.RESET,
                bcolors.BLUE + "додати іще 1-ин email до існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючого email" + bcolors.RESET,
                bcolors.BLUE + "редагування phone існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "редагування email існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "редагування birthday існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "виводить список контактів, у яких день народження через задану кількість днів від поточної дати" + bcolors.RESET,
                bcolors.BLUE + "зберігає нотатку за іменем автора" + bcolors.RESET,
                bcolors.BLUE + "здійснює пошук нотатки серед існуючих нотатків" + bcolors.RESET,
                bcolors.BLUE + "показує всі існуючі нотатки" + bcolors.RESET,
                bcolors.BLUE + "редагування існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "додавання тегів до існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "редагування тегів існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "видалення тегів з існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "пошук та сортування нотаток за тегами" + bcolors.RESET,
                bcolors.BLUE + "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)." + bcolors.RESET,
                bcolors.BLUE + "показати всі розширення" + bcolors.RESET,
                bcolors.BLUE + "додавання додатково розширення для сортування" + bcolors.RESET,
                bcolors.BLUE + "видалення розширення із списку для сортування" + bcolors.RESET,
                bcolors.BLUE + "вихід з програми" + bcolors.RESET,
                bcolors.BLUE + "вихід з програми" + bcolors.RESET,
                bcolors.BLUE + "вихід з програми" + bcolors.RESET,
            ]



        elif language == 'ua':
            command_list = [
                bcolors.ORANGE + "можливості" + bcolors.RESET,
                bcolors.ORANGE + "зміти мову" + bcolors.RESET,
                bcolors.ORANGE + "додати контакт" + bcolors.RESET,
                bcolors.ORANGE + "пошук контакта" + bcolors.RESET,
                bcolors.ORANGE + "показати всі контакти" + bcolors.RESET,
                bcolors.ORANGE + "додати телефон" + bcolors.RESET,
                bcolors.ORANGE + "видалити телефон" + bcolors.RESET,
                bcolors.ORANGE + "додати електронну пошту" + bcolors.RESET,
                bcolors.ORANGE + "видалити електронну пошту" + bcolors.RESET,
                bcolors.ORANGE + "редагувати телефон" + bcolors.RESET,
                bcolors.ORANGE + "редагувати електронну пошту" + bcolors.RESET,
                bcolors.ORANGE + "редагувати день народження" + bcolors.RESET,
                bcolors.ORANGE + "видалити контакт" + bcolors.RESET,
                bcolors.ORANGE + "показати дні народження" + bcolors.RESET,
                bcolors.ORANGE + "додати нотатку" + bcolors.RESET,
                bcolors.ORANGE + "знайти нотатку" + bcolors.RESET,
                bcolors.ORANGE + "показати всі нотатки" + bcolors.RESET,
                bcolors.ORANGE + "редагувати нотатку" + bcolors.RESET,
                bcolors.ORANGE + "видалити нотатку" + bcolors.RESET,
                bcolors.ORANGE + "додати тег" + bcolors.RESET,
                bcolors.ORANGE + "редагувати тег" + bcolors.RESET,
                bcolors.ORANGE + "видалити тег" + bcolors.RESET,
                bcolors.ORANGE + "знайти та сортувати по тегам" + bcolors.RESET,
                bcolors.ORANGE + "відсортувати файли" + bcolors.RESET,
                bcolors.ORANGE + "показати всі розширення" + bcolors.RESET,
                bcolors.ORANGE + "додати розширення файла" + bcolors.RESET,
                bcolors.ORANGE + "видалити розширення файла" + bcolors.RESET,
                bcolors.ORANGE + "до зустрічі" + bcolors.RESET,
            ]

            command_explain = [
                bcolors.BLUE + "виводить список всіх доступних команд" + bcolors.RESET,
                bcolors.BLUE + "змінити мову додатка" + bcolors.RESET,
                bcolors.BLUE + "зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів" + bcolors.RESET,
                bcolors.BLUE + "здійснює пошук контакту серед контактів книги" + bcolors.RESET,
                bcolors.BLUE + "показує всі існуючі контакти в книзі контактів" + bcolors.RESET,
                bcolors.BLUE + "додати іще 1-ин phone до існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючого phone" + bcolors.RESET,
                bcolors.BLUE + "додати іще 1-ин email до існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючого email" + bcolors.RESET,
                bcolors.BLUE + "редагування phone існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "редагування email існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "редагування birthday існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючого контакту" + bcolors.RESET,
                bcolors.BLUE + "виводить список контактів, у яких день народження через задану кількість днів від поточної дати" + bcolors.RESET,
                bcolors.BLUE + "зберігає нотатку за іменем автора" + bcolors.RESET,
                bcolors.BLUE + "здійснює пошук нотатки серед існуючих нотатків" + bcolors.RESET,
                bcolors.BLUE + "показує всі існуючі нотатки" + bcolors.RESET,
                bcolors.BLUE + "редагування існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "видалення існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "додавання тегів до існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "редагування тегів існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "видалення тегів з існуючої нотатки" + bcolors.RESET,
                bcolors.BLUE + "пошук та сортування нотаток за тегами" + bcolors.RESET,
                bcolors.BLUE + "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)." + bcolors.RESET,
                bcolors.BLUE + "показати всі наявні розширеннядля сортування" + bcolors.RESET,
                bcolors.BLUE + "додавання додатково розширення для сортування" + bcolors.RESET,
                bcolors.BLUE + "видалення розширення із списку для сортування" + bcolors.RESET,
                bcolors.BLUE + "бот іде відпочивати" + bcolors.RESET,
            ]

        if language:
            return "".join(
                "|{:<10} - {:<20}|\n".format(command_list[item], command_explain[item])
                for item in range(len(command_list)))

class AddContact(AbstractUserInterface):

    id=1

    def handle(self):
        result=self.add_contacts()
        return result

    def add_contacts(self):
        attempts = 0
        flag_name = False
        flag_phone = False
        flag_birthday = False
        flag_email = False

        while attempts < 3:
            try:
                while not flag_name:
                    print(f"{bcolors.ORANGE}📝 Please enter your name that contains more than two characters:✍️  {bcolors.RESET}")
                    name = input(f"{bcolors.BOLD}📝 Please enter your name:✍️  {bcolors.RESET}")

                    record = Record(name)
                    for contact in self.data:
                        if contact["name"].name == name:
                            print(f"{bcolors.WARNING}❌ Contact with this name already exists, try to enter another name!😞 {bcolors.RESET}")
                            print(f"{bcolors.WARNING}📝 Please enter the name again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️  {bcolors.RESET}")
                            if name in ['q', 'back', 'exit', 'quit']:
                                return
                            break
                    else:
                        flag_name = True

                if not flag_phone:
                    while True:
                        print(f"{bcolors.ORANGE}📞 Exsamples of the input: (+380) or (380) or (10 digits)✅ {bcolors.RESET}")
                        phone = input(f"{bcolors.BOLD}📞 Please enter phone:✍️  {bcolors.RESET}")
                        if phone in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            record.add_phone(phone)
                            flag_phone = True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {error}{bcolors.RESET}")
                            print(f"{bcolors.WARNING}📞 Please enter the phone number again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️ {bcolors.RESET}")

                if not flag_birthday:
                    while True:
                        print(f"{bcolors.ORANGE}🎂 Please enter birthday in format (YYYY-MM-DD):✍️  {bcolors.RESET}")
                        birthday = input(f"{bcolors.BOLD}🎂 Please enter birthday:✍️  {bcolors.RESET}")
                        if birthday in ['q', 'back', 'exit', 'quit']:
                            return
                        if birthday:
                            try:
                                record.birthday = Birthday(birthday)
                                flag_birthday = True
                                break
                            except ValueError as error:
                                print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                                print(f"{bcolors.WARNING}🎂 Please enter the birthday again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️  {bcolors.RESET}")

                if not flag_email:
                    while True:
                        print(f"{bcolors.ORANGE}📧 Please enter email in format (example@example.com):✍️  {bcolors.RESET}")
                        email = input(f"{bcolors.BOLD}📧 Please enter email:✍️  {bcolors.RESET}")
                        if email in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            record.add_email(email)
                            flag_email = True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                            print(f"{bcolors.WARNING}📧 Please enter the email again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️ {bcolors.RESET}")

                contacts = {
                    "id": AddContact.id,
                    "name": record.name,
                    "phone": record.phones,
                    "birthday": record.birthday,
                    "email": [str(email) for email in record.email],
                }
                self.data.append(contacts)
                AddContact.id += 1
                print(f"{bcolors.GREEN}👤 Contact added successfully!✅{bcolors.RESET}")
                break
            except Exception as e:
                attempts += 1
                print(f"{bcolors.FAIL}Error❗ - {bcolors.RESET}{e}")
                print(f"{bcolors.WARNING}🔄 Please enter the information again!🔄 {bcolors.RESET}")

class SearchContact(AbstractUserInterface):

    def handle(self):
        result=self.search_contact()
        return result

    def search_contact(self):
        name = input(f"{bcolors.BOLD}🔍 Please enter the name of the contact you want to find:✍️  {bcolors.RESET}")
        matching_contacts = [contact for contact in self.data if contact["name"].name.lower() == name.lower()]

        if not matching_contacts:
            print(f"{bcolors.WARNING}😞 No contacts found with the name 👤 '{name}'{bcolors.RESET}")
            print(emojize(f"{bcolors.WARNING}😞 Contact with name '{name}' does not found❌ {bcolors.RESET}"))
            print(f"{bcolors.GREEN}🤗 But, you can add a contact if you want ✏️ {bcolors.RESET}")
            return

        print(f"{bcolors.GREEN}🔍 Search results for '{name}':🚀  {bcolors.RESET}")
        print(f"{bcolors.GREEN}🎉 Find contact with name🤗  {name}{bcolors.RESET}")
        table = []
        for contact in matching_contacts:
            phone_numbers = ", ".join(str(phone) for phone in contact.get("phone", []))
            emails = ", ".join(str(email) for email in contact.get("email", []))
            table.append([
                str(contact["id"]),
                str(contact["name"]),
                phone_numbers,
                str(contact.get("birthday", "")),
                emails,
            ])

        headers = [
            emojize(f":id: {bcolors.BLUE}ID{bcolors.RESET}", language="alias"),
            emojize(f":bust_in_silhouette: {bcolors.BLUE}Name{bcolors.RESET}", language="alias"),
            emojize(f":telephone_receiver: {bcolors.BLUE}Phone{bcolors.RESET}", language="alias"),
            emojize(f":birthday_cake: {bcolors.BLUE}Birthday{bcolors.RESET}", language="alias"),
            emojize(f":e-mail: {bcolors.BLUE}Email{bcolors.RESET}", language="alias"),
        ]

        print(tabulate(table, headers=headers, tablefmt='pretty'))


class ContactPhoneAdd(AbstractUserInterface):

    def handle(self):
        result=self.add_phone()
        return result

    def add_phone(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                phone = input(f"{bcolors.BOLD}🔍 Please enter phone📞: {bcolors.RESET}")
                contact["phone"].append(phone)
                print(f"{bcolors.GREEN}📞 Phone number '{phone}' successfully added!✅{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")

class ContactPhoneRemove(AbstractUserInterface):

    def handle(self):
        result=self.remove_phone()
        return result

    def remove_phone(self):
        name = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contacts in self.data:
            if str(contacts["name"]) == name:
                error_flag = True
                phone_numbers = ", ".join(
                    str(phone) for phone in contacts.get("phone", [])
                )
                print(f"{bcolors.WARNING}Select the phone you want to delete{bcolors.RESET}")
                print(f"{bcolors.BLUE}{phone_numbers}{bcolors.WARNING}")
                phone_to_remove = input(f"{bcolors.BOLD}🔍 Please enter the phone number to remove:✍️  {bcolors.RESET}")
                phone_object_to_remove = None

                for phone_object in contacts["phone"]:
                    if str(phone_object) == phone_to_remove:
                        phone_object_to_remove = phone_object
                        break

                if phone_object_to_remove is not None:
                    contacts["phone"].remove(phone_object_to_remove)
                    print(f"{bcolors.GREEN}📞 The phone number '{name}' was successfully deleted!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}📞 Phone number '{phone_to_remove}' not found❌ {bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}👤 Contact '{name}' isn't here!❌ {bcolors.RESET}")

class ContactEmailAdd(AbstractUserInterface):

    def handle(self):
        result=self.add_email()
        return  result

    def add_email(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email = input(f"{bcolors.BOLD}📧 Please enter email:✍️  {bcolors.RESET}")
                contact["email"].append(email)
                print(f"{bcolors.GREEN}📧 Email '{email}' Successfully added!✅{bcolors.RESET}")

        if not error_flag:
            print(f"{bcolors.FAIL}👤 Contact isn't here!😞{bcolors.RESET}")


class ContactEmailRemove(AbstractUserInterface):

    def handle(self):
        result=self.remove_email()
        return result

    def remove_email(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email_list = ", ".join(
                    str(email) for email in contact.get("email", [])
                )
                print(f"{bcolors.WARNING}Select the emails you want to delete{bcolors.RESET}")
                print(f"{bcolors.BLUE}{email_list}{bcolors.WARNING}")
                email_to_remove = input(f"{bcolors.BOLD}🔍 Please enter the email to remove:✍️  {bcolors.RESET}")
                email_object_to_remove = None

                for email_object in contact["email"]:
                    if str(email_object) == email_to_remove:
                        email_object_to_remove = email_object
                        break

                if email_object_to_remove is not None:
                    contact["email"].remove(email_object_to_remove)
                    print(f"{bcolors.GREEN}📧 Email '{email_to_remove}' successfully delete!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}❌ Email '{email_to_remove}' not found.😞{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")

class ContactPhoneEdit(AbstractUserInterface):

    def handle(self):
        result=self.edit_phone()
        return result

    def edit_phone(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                phone_numbers = ", ".join(
                    str(phone) for phone in contact.get("phone", [])
                )
                print(f"{bcolors.WARNING}Select the phone you want to edit{bcolors.RESET}")
                print(f"{bcolors.BLUE}{phone_numbers}{bcolors.WARNING}")
                edit_to_phone_number = input(f"{bcolors.BOLD}📞 Enter the phone number to edit:✍️  {bcolors.RESET}")
                new_phone_number = input(f"{bcolors.BOLD}📞 Enter the new phone number:✍️  {bcolors.RESET}")
                phone_number_object_to_edit = None

                for i, phone_number_object in enumerate(contact["phone"]):
                    if str(phone_number_object) == edit_to_phone_number:
                        phone_number_object_to_edit = phone_number_object
                        break

                if phone_number_object_to_edit is not None:
                    print(f"{bcolors.WARNING}📞 Old phone number: '{phone_number_object_to_edit}'{bcolors.RESET}")
                    print(f"{bcolors.GREEN}📞 Successfully changed to '{new_phone_number}'✅{bcolors.RESET}")
                    contact["phone"].remove(phone_number_object_to_edit)
                    contact["phone"].append(new_phone_number)
                    print(f"{bcolors.GREEN}📞 Phone number '{new_phone_number}' edited successfully!✅{bcolors.RESET}")
                else:
                    print(
                        f"{bcolors.FAIL}📞 Error editing phone number '{new_phone_number}': Phone Number not found❌{bcolors.RESET}")

        if not error_flag:
            print(f"{bcolors.FAIL}❌ There are no contacts with such name '{user_input}'!{bcolors.RESET}")

class ContactEmailEdit(AbstractUserInterface):

    def handle(self):
        result=self.edit_email()
        return result

    def edit_email(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email_list = ", ".join(
                    str(email) for email in contact.get("email", [])
                )
                print(f"{bcolors.WARNING}Select the emails you want to edit{bcolors.RESET}")
                print(f"{bcolors.BLUE}{email_list}{bcolors.WARNING}")
                edit_to_email = input(f"{bcolors.BOLD}🔍 Enter the email to edit: {bcolors.RESET}")
                new_email = input(f"{bcolors.BOLD}📧 Enter new email:✍️  {bcolors.RESET}")
                email_object_to_edit = None

                for i, email_object in enumerate(contact["email"]):
                    if str(email_object) == edit_to_email:
                        email_object_to_edit = email_object
                        break

                if email_object_to_edit is not None:
                    print(f"{bcolors.BOLD}📧 Old email: '{email_object_to_edit}{bcolors.RESET}'")
                    print(f"{bcolors.GREEN}📧 Email successfully changed to '{new_email}'✅{bcolors.RESET}")

                    contact["email"].remove(email_object_to_edit)
                    contact["email"].append(new_email)

                    print(f"{bcolors.GREEN}📧 Email edited '{edit_to_email}' successfully!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}❌ Error editing email '{edit_to_email}': email not found!❌{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")


class ContactBirthdayEdit(AbstractUserInterface):

    def handle(self):
        result=self.edit_birthday()
        return result

    def edit_birthday(self):  # редагування birthday існуючого контакту
        name = input(f'{bcolors.BOLD}🔍 Enter name of contact:✍️  {bcolors.RESET}')
        error_flag = False
        for contact in self.data:
            if contact['name'].name == name and contact['birthday']:
                new_birthday = input('Enter new birthday: ')
                try:
                    contact['birthday'] = Birthday(new_birthday)
                    print(f'{bcolors.GREEN}🎂 Birthday "{new_birthday}" was changed!✅{bcolors.RESET}')
                except ValueError as ex:
                    print(ex)
                error_flag = True

        if not error_flag:
            print(f"{bcolors.FAIL}❌ There are no contacts with such name '{name}'!{bcolors.RESET}")

class ContactRemove(AbstractUserInterface):

    def handle(self):
        result=self.del_contact()
        return result

    def del_contact(self):
        name = input(f"{bcolors.BOLD }📝 Please enter name:✍️  {bcolors.RESET}")
        contacts=[]
        for contact in self.data:
            if str(contact["name"]) == name:
                contacts.append(contact)
                self.data.remove(contact)
        if contacts:
            for i in contacts:
                print(f"{bcolors.GREEN}👤 Contact '{i['name'].name}' was deleted!✅{bcolors.RESET}")
        else:
            print(f"{bcolors.FAIL}🔍 Contact '{name}' is not found! 😞{bcolors.RESET}")

class DisplayBirthdays(AbstractUserInterface):

    def handle(self):
        result=self.show_contacts_birthdays()
        return result

    def show_contacts_birthdays(self):
        while 1:
            try:
                days = int(input(f"{bcolors.BOLD}🤗 Enter days:✍️  {bcolors.RESET}"))
                break
            except Exception as e:
                print(f"{bcolors.WARNING}Enter the number of days by number and not string!{bcolors.RESET}")
                continue

        contacts = []

        for contact in self.data:
            if 'birthday' in contact and contact['birthday']:
                birthday_date = contact['birthday'].value
                record = Record(contact['name'].name, birthday=birthday_date)
                if record.days_to_date(days, birthday_date):
                    contacts.append(contact)

        if contacts:
            for uzer in contacts:
                print(f'{bcolors.GREEN}Name: {uzer["name"].name}, Birthday:🎂  {uzer["birthday"].value}{bcolors.RESET}')
        else:
            print(f'{bcolors.WARNING}🎂 There are no birthdays in this number of day!{bcolors.RESET}')







