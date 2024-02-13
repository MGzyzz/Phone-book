import re

contact = [{
    "name": "John", "phone": ["123456", "678910"]}, {
    "name": "Jane", "phone": ["564321"]}, {
    "name": "Bob", "phone": ["+1234", "+1235", "+1236"]}, ]


def contact_user():
    return contact


def check_words(check):
    if re.match(r'^[\d+-]+$', check):
        return check
    else:
        return print(
            "Действие невозможно так как введенный вами номер содержит букву или другой символ. Пожалуйста напишите номер повторно")


def check_numbers(check):
    if re.match(r'^[a-zA-Z]+$', check):
        return check
    else:
        return print("Действие невозможно так как введенный вами имя содержит цифры или другой символ. Пожалуйста напишите имя повторно")


def continue_user():
    choose = input("Вы точно хотите совершить это действие? y/n\n").lower()

    if choose == "y" or choose == "ok" or choose == "yes":
        return True
    else:
        print("Действие отменено!")
        return False


def contact_number():
    result = f'\n{"Name":<5}|{"Phone":>5}\n{"-" * 35}\n'
    contact_user().sort(key=lambda x: x["name"])

    for name in contact_user():
        phone_numbers = " ".join(name['phone'])
        result += f"{name['name']:<5}|{phone_numbers:>5}\n"
    return print(result)


def find_user(find):
    if index_user(find):
        for i in contact_user():
            if index_user(find) == i["name"]:
                return print(f"\nКонтакт найден:\nИмя: {i['name']}\nНомера: {' '.join(f'[{x + 1}] {n}' for x, n in enumerate(i['phone']))}\n")
    else:
        return print("Введеный вами контакт не существует. Попробуйте снова")


def index_user(index_user):
    for i in contact_user():
        if index_user in i["name"]:
            return i["name"]
        elif index_user in i["phone"]:
            return i["phone"]


def add_user():
    add_name = input("Пожалуйста введите имя\n").capitalize()

    if not index_user(add_name):
        if check_numbers(add_name):
            add_phone = input("Введите номер телефона\n")
            if check_words(add_phone):
                new_contact = {"name": add_name, "phone": [add_phone]}
                contact_user().append(new_contact)
                return print("Пользователь был успешно добавлен!")
    else:
        print("Пользователь с таким именнем существует")


def notFound():
    return print("Введеный вами контакт не существует. Попробуйте снова")


def add_phone():
    user = input("Пожалуйста введите имя контакта\n").capitalize()
    find_user(user)

    for i in contact_user():
        if index_user(i["name"]) == user:
            addnumber = input("\nВведите номер для добавление\n")
            if check_words(addnumber):
                i["phone"].append(addnumber)
                return print("Номер успешно добавлен!")


def edit_user():
    choose_contact = input("Напишите контакт который вы хотите изменить\n").capitalize()

    if index_user(choose_contact):
        find_user(choose_contact)
        choose_reset = input("Что вы хотите изменить? Выбор = имя/номер\n").lower()

        for i in contact_user():
            if choose_reset == "имя" or choose_reset == "name":
                choose_name = input("Введите новое имя пользователя\n").capitalize()
                if index_user(choose_contact) and check_numbers(choose_name):
                    i["name"] = choose_name
                    return print("Имя изменено!")
                else:
                    break

            elif choose_reset == "номер" or choose_reset == "phone":
                if i["name"] == choose_contact:
                    choose = input("\nКакой номер вы хотите изменить? Выбор осуществляется с помощью индексов\n")
                    if int(choose) <= len(i["phone"]):
                        choose_phone = input("Введите новый номер телефона\n")
                        if check_words(choose_phone):
                            a = int(choose) - 1
                            i["phone"][a] = choose_phone
                            return print("Номер изменен!")
                        else:
                            break
                    else:
                        print("Введенный вами номер не существует")

        else:
            print("Неверная команда попробуйте снова")
    else:
        notFound()


def show_number(find):
    for i in contact_user():
        if index_user(find) == i["name"]:
            return i["phone"]


def delete_user():
    delete_name = input("Какого пользователя вы хотите удалить?\n").capitalize()

    if index_user(delete_name):
        find_user(delete_name)
        for i in contact_user():
            if i["name"] == delete_name:
                if continue_user():
                    remove_user = contact_user().index(i)
                    contact_user().pop(remove_user)
                    return print("Действие завершено")
        else:
            return
    else:
        notFound()


def delete_number():
    user = input("Введите контакт для удаление номер\n").capitalize()

    if index_user(user):
        find_user(user)
        for i in contact_user():
            choose_number = input("Какой номер вы хотите удалить? Выбор осуществляется с помощью индексов\n")
            if len(show_number(user)) == 1:
                return print("Действие невозможно, так как у пользователя один номер")
            elif int(choose_number) <= len(i["phone"]) and continue_user():
                choose_number = int(choose_number) - 1
                i["phone"].pop(choose_number)
                return print("Номер удален!")
            else:
                break

    else:
        notFound()


def choose_user():
    choose = input(
        "\n[1] Вывести контакты\n[2] Найти контакт\n[3] Добавить контакт\n[4] Добавить номер для контакта\n[5] Изменить "
        "контакт\n[6] Удалить контакт\n[7] Удалить номер контакта\n[0] Выход\n")
    return choose


def main_menu():
    print("Добро пожаловать в телефонную книгу, Пожалуйста сделайте выбор по индексам ниже")
    while True:
        match choose_user():
            case "1":
                contact_number()
            case "2":
                find = input("Пожалуйста напишите имя контакта\n").capitalize()
                find_user(find)
            case "3":
                add_user()
            case "4":
                add_phone()
            case "5":
                edit_user()
            case "6":
                delete_user()
            case "7":
                delete_number()
            case "0":
                if continue_user():
                    break
            case _:
                print("Введеная вами команда не существует. Пожалуйста попробуете снова")


main_menu()
