from CODE_CRAFTERS_CORE.AvadaKedavra import shutdown_with_countdown
from CODE_CRAFTERS_CORE.FileSorting import executing_command
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import WordCompleter
from CODE_CRAFTERS_CORE.RecordData import bcolors
from CODE_CRAFTERS_CORE.AddressBook import *
from CODE_CRAFTERS_CORE.NoteFeature import *
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from pathlib import Path
import threading
import asyncio
import random
from interface import ConsoleUI, GetCommand,AddContact,SearchContact,ContactPhoneAdd,ContactPhoneRemove,ContactEmailAdd,ContactEmailRemove,ContactPhoneEdit,ContactEmailEdit,ContactBirthdayEdit,ContactRemove,DisplayBirthdays
from Interface_note import *
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from command_list import command_list



def main():

    exit_flag = False
    language_flag = False
    file_name = "database.bin"
    note_name = "notebase.bin"
    file_database = Path(file_name)
    note_database = Path(note_name)
    command_list_user = command_list
    command_completer = WordCompleter(command_list_user)


    # Deserialization adddressbook
    if file_database.exists() and file_database.is_file():
        with open(file_database, "rb") as fh:
            check_content = fh.read()

        if not check_content:
            book = AddressBook()
        else:
            deserialization = AddressBook()
            book = deserialization.read_from_file(file_name)
    else:
        with open(file_database, "wb") as fh:
            pass
        book = AddressBook()

    # Deserialization notebook
    if note_database.exists() and note_database.is_file():
        with open(note_database, "rb") as fh:
            check_content = fh.read()
        if not check_content:
            note = NoteBook()
        else:
            deserialization = NoteBook()
            note = deserialization.note_read_from_file(note_name)
    else:
        with open(note_database, "wb") as fh:
            pass
        note = NoteBook()

    print(f"{bcolors.PINK}👋 Hello! My name is Bot Jul. Please choose the language and we will begin 🤖 {bcolors.RESET}")

    try:
        while 1:
            if not language_flag:
                language = input(f"{bcolors.BOLD}🏳️  Please choose a language (en/:ru:/ua): {bcolors.RESET}")
                language_flag = True
                language_uzer=language
                if not language in ("en", "ru", 'ua'):
                    while 1:
                        print(f"{bcolors.BOLD}🙃  Wrong language format entered!\nPlease enter en | ru or ua to choose language:{bcolors.RESET}")
                        language = input(f"{bcolors.BOLD}🫠  Please choose a language (en/ru/ua): {bcolors.RESET}")
                        if language in ("en", "ru", 'ua'):
                            language_flag = True
                            language_uzer=language
                            break

            command={'contact-show-all': ConsoleUI(book),
                     'help': GetCommand(),
                     'contact-add': AddContact(book),
                     'contact-find':SearchContact(book),
                     'contact-phone-add':ContactPhoneAdd(book),
                     'contact-phone-remove':ContactPhoneRemove(book),
                     'contact-email-add': ContactEmailAdd(book),
                     'contact-email-remove': ContactEmailRemove(book),
                     'contact-phone-edit': ContactPhoneEdit(book),
                     'contact-email-edit': ContactEmailEdit(book),
                     'contact-birthday-edit': ContactBirthdayEdit(book),
                     'contact-remove': ContactRemove(book),
                     'display-birthdays': DisplayBirthdays(book),
                     'note-add': NoteAdd(note),
                     'note-find': NoteFind(note),
                     'note-edit': NoteEdit(note),
                     'note-remove': NoteRemove(note),
                     'tag-add': TagAdd(note),
                     'tag-edit': TagEdit(note),
                     'tag-remove': TagRemove(note),
                     'tag-find-sort': TagFindSort(note),
                     'note-show-all': NoteShowAll(note),
                    }

            user_input = prompt('Enter command or  "help": ', completer=command_completer)
            if user_input in command:
                command[user_input].handle()

            match user_input:

                case "change-language" | "изменить язык" | "зміти мову":
                    language_flag = False


                case "note-show-all" | "показать все заметки" | "показати всі нотатки":
                     #"показує всі існуючі нотатки"
                    note.note_show_all()

                case "file-sort" | "сортировать файлы" | "відсортувати файли":
                    #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                    executing_command(user_input.lower())

                case "file-extension-show" | "показать все разширения" | "показати всі розширення":
                    #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                    executing_command(user_input.lower())

                case "file-extension-add" | "добавить расширение" | "додати розширення файла":
                    #  "додавання додатково розширення для сортування"
                    executing_command(user_input.lower())

                case "file-extension-remove" | "удалить расширение" | "видалити розширення файла":
                    #  "видалення розширення із списку для сортування"
                    executing_command(user_input.lower())

                case "quit" | "exit" | "q" | "выход" | "в" | "до зустрічі" | "д":
                    print("Good bye!\n")
                    serialization = AddressBook()
                    serialization.save_to_file(file_name, book)
                    note_serialization = NoteBook()
                    note_serialization.note_save_to_file(note_name, note)
                    break

                case _:
                    if language == "en":
                        error_messages = [
                            f"{bcolors.WARNING}😔 Oh! You seem to have introduced the wrong command. Please try again!😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😔 Oops! This is not like the right command. Let's try again😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😟 Error: The command is not recognized. Try again.😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😮 Hmm, I don't understand this command. Let's try something else.😔{bcolors.RESET}"
                        ]
                    elif language == "ua":
                        error_messages = [
                            f"{bcolors.WARNING}😔 Ой! Начебто Ви ввели хибну команду. Будь ласка спробуйте ыще раз!😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😯 Упс! Це не схоже правельну команду. Давайте спробуэмо ыще раз!😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😔 Помилка: Незрозумыла команда. Спробуйте ще раз.😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😔😮 Хмм, я не розумію цю команду. давайте спробуємо щось інше!😔{bcolors.RESET}"
                        ]

                    print(random.choice(error_messages))
                    if exit_flag:
                        timer_thread.cancel()
                        break


    except Exception as ex:
        print(f"{bcolors.FAIL}\n❌ Unnexpected error!{bcolors.RESET}")
        print(ex)
        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)

    except KeyboardInterrupt:
        print(f"{bcolors.FAIL}\n❌ KeyBoard interrupt error, EXITING!\n{bcolors.RESET}")

        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{bcolors.BLUE}The script is interrupted by the user!{bcolors.RESET}")


