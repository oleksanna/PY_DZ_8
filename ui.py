

def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных")
    command = int(input('Введите число '))

    while command != 1 and command != 2:
        print("Неправильный ввод")
        command = int(input('Введите число '))

interface()        