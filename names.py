import json
import os

ppk = "./Names"
# ppk_men = "./Names/Men"
# ppk_women = "./Names/Women"
num = 0


def welcome_menu():

    while True:
        print('(1) - Создание файла')
        print('(2) - Просмотр каталога')
        print('(3) - Редактирование файла')
        print('(4) - Удаление файла')
        print('(5) - Выход из программы')
        print('')
        inp = input('Введите число от 1 до 5: ')
        if inp == '1' or inp == 1:
            add_new_record()
        if inp == '2' or inp == 2:
            show_files()
        if inp == '3' or inp == 3:
            print('Добавление записи пока не реализовано')
        if inp == '4' or inp == 4:
            print('удаление файлов пока не реализовано')
        if inp == '5' or inp == 5:
            break
        else:
            print('Введено неправильное значение. Пожалуйста попробуйте ещё раз.')


def show_files():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    d = os.listdir(ppk)
    files_exist = False
    for i, file in enumerate(d):
        files_exist = True
        print(i, ':', file)
    if not files_exist:
        print('Файлов пока нет')

def add_new_record():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    name = input('введите имя')
    surname = input('введите фамилию')
    d = {
        'name': name,
        'surname': surname
    }
    json_str = json.dumps(d)
    f_name = d['name'] + '.txt'
    papka = os.listdir(ppk)
    if f_name in papka:
        x = num + 1
        f_name = f_name + x

    full_filename = ppk + '/' + f_name
    with open(full_filename, 'w') as f:
        print(f)
        f.write(json_str)

def view_record(index):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('тут мы будем отображать файл c индексом ', index)
    d = os.listdir(ppk)
    filename = None
    for i, file in enumerate(d):
        if i == int(index):
            filename = file
    if filename:
        print('here we open file', filename)
        with open(ppk + '/' + filename, 'r') as f:
            file_content = f.read()
            saved_dict = json.loads(file_content)
            print('Сохраненный словарь', saved_dict)



try:
    os.mkdir(ppk)
    # os.mkdir(ppk_men)
    # os.mkdir(ppk_women)
except FileExistsError:
    print('Домашняя папка уже содержит папку "Names"')
else:
    print('Будет создана папка "Names" в домашнем каталоге')
finally:
    print('Вы хотите очистить экран перед продолжением?')
    yn = input()
    if yn == 'y' or yn == 'д':
        if os.name == 'nt':
            os.system('cls')
            welcome_menu()
        else:
            os.system('clear')
            welcome_menu()
    else:
        welcome_menu()
