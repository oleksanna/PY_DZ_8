from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные?\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число '))
    
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")

    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")       



def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


def delete_data():
    name_to_delete = input("Введите имя или фамилию для удаления данных: ")

    found = False

    with open('data_first_variant.csv', 'r+', encoding='utf-8') as f1:
        lines = f1.readlines()
        f1.seek(0)
        f1.truncate()
        for line in lines:
            if name_to_delete in line:
                found = True
                delete_option = input("Выберите опцию удаления:\n"
                                      "1 - Удалить всю запись\n"
                                      "2 - Удалить только определенные данные\n"
                                      "Введите число: ")

                if delete_option == '1':
                    continue
                elif delete_option == '2':
                    print(f"Какие данные удалить для {name_to_delete}?\n"
                          "1 - Имя\n"
                          "2 - Фамилия\n"
                          "3 - Номер телефона\n"
                          "4 - Адрес\n")
                    data_to_delete = input("Введите число: ")

                    if data_to_delete == '1':
                        line = line.replace(name_to_delete, '')
                    elif data_to_delete == '2':
                        line = line.replace(name_to_delete, '')
                    elif data_to_delete == '3':
                        line = line.replace(name_to_delete, '')
                    elif data_to_delete == '4':
                        line = line.replace(name_to_delete, '')
                    else:
                        print("Некорректный ввод.")

                f1.write(line)

    with open('data_second_variant.csv', 'r+', encoding='utf-8') as f2:
        lines = f2.readlines()
        f2.seek(0)
        f2.truncate()
        for line in lines:
            if name_to_delete in line:
                found = True
                delete_option = input("Выберите опцию удаления:\n"
                                      "1 - Удалить всю запись\n"
                                      "2 - Удалить только определенные данные\n"
                                      "Введите число: ")

                if delete_option == '1':
                    continue
                elif delete_option == '2':
                    print(f"Какие данные удалить для {name_to_delete}?\n"
                          "1 - Имя\n"
                          "2 - Фамилия\n"
                          "3 - Номер телефона\n"
                          "4 - Адрес\n")
                    data_to_delete = input("Введите число: ")

                    if data_to_delete == '1':
                        line = line.replace(name_to_delete, '')
                    elif data_to_delete == '2':
                        line = line.replace(name_to_delete, '')
                    elif data_to_delete == '3':
                        line = line.replace(name_to_delete, '')
                    elif data_to_delete == '4':
                        line = line.replace(name_to_delete, '')
                    else:
                        print("Некорректный ввод.")

                f2.write(line)

    if not found:
        print("Такого контакта не существует!")
    else:
        print(f"Данные для {name_to_delete} удалены успешно.")


def modify_data():
    name_to_modify = input("Введите имя или фамилию для изменения данных: ")

    found = False

    with open('data_first_variant.csv', 'r+', encoding='utf-8') as f1:
        lines = f1.readlines()
        f1.seek(0)
        f1.truncate()
        for line in lines:
            if name_to_modify in line:
                found = True
                modify_option = input("Выберите опцию изменения:\n"
                                      "1 - Изменить всю запись\n"
                                      "2 - Изменить только один параметр\n"
                                      "Введите число: ")

                if modify_option == '1':
                    new_name = input("Введите новое имя: ")
                    new_surname = input("Введите новую фамилию: ")
                    new_phone = input("Введите новый номер телефона: ")
                    new_address = input("Введите новый адрес: ")
                    f1.write(f"{new_name}\n{new_surname}\n{new_phone}\n{new_address}\n\n")
                elif modify_option == '2':
                    print("Выберите параметр для изменения:\n"
                          "1 - Имя\n"
                          "2 - Фамилия\n"
                          "3 - Номер телефона\n"
                          "4 - Адрес\n")
                    param_to_modify = int(input("Введите число: "))
                    new_value = input("Введите новое значение: ")
                    data = line.strip().split('\n')
                    data[param_to_modify - 1] = new_value
                    f1.write('\n'.join(data) + '\n\n')
            else:
                f1.write(line)

    with open('data_second_variant.csv', 'r+', encoding='utf-8') as f2:
        lines = f2.readlines()
        f2.seek(0)
        f2.truncate()
        for line in lines:
            if name_to_modify in line:
                found = True
                modify_option = input("Выберите опцию изменения:\n"
                                      "1 - Изменить всю запись\n"
                                      "2 - Изменить только один параметр\n"
                                      "Введите число: ")

                if modify_option == '1':
                    new_name = input("Введите новое имя: ")
                    new_surname = input("Введите новую фамилию: ")
                    new_phone = input("Введите новый номер телефона: ")
                    new_address = input("Введите новый адрес: ")
                    f2.write(f"{new_name};{new_surname};{new_phone};{new_address}\n\n")
                elif modify_option == '2':
                    print("Выберите параметр для изменения:\n"
                          "1 - Имя\n"
                          "2 - Фамилия\n"
                          "3 - Номер телефона\n"
                          "4 - Адрес\n")
                    param_to_modify = int(input("Введите число: "))
                    new_value = input("Введите новое значение: ")
                    data = line.strip().split(';')
                    data[param_to_modify - 1] = new_value
                    f2.write(';'.join(data) + '\n\n')
            else:
                f2.write(line)

    if not found:
        print("Такого контакта не существует!")
    else:
        print(f"Данные для {name_to_modify} изменены успешно.")