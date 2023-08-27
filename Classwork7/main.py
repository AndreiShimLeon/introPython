# # Задача 49.
# Создать телефонный справочник:
# 1. Программа должна выводить данные;
# 2. Программа должна сохранять данные в текстовом файле;
# 3. Пользователь может ввести одну из характеристик
# для поиска определенной записи (например, имя или фамилию)
# 4. Использование функций. Программа не должны быть линейной.


# Homework: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

def correct_data(phonebook):
    flag = True
    while flag:
        search_key = input('Введите имя/фамилию для поиска. Для выхода введите "выход": ')
        if search_key.lower() == 'выход':
            flag = False
        else:
            results = search_contacts(phonebook, search_key)
            if len(results) > 1:
                print('Было найдено более 1 записи, повторите поиск')
            else:
                print(f'{results[0][1]["last_name"]},{results[0][1]["first_name"]},{results[0][1]["middle_name"]},{results[0][1]["phone_number"]}')
                confirmation = input(f'Найденная запись требует корректировки? Y/N: ').lower()
                if confirmation == 'y':
                    new_l_name = input('Введите новую фамилию: ')
                    new_f_name = input('Введите новое имя: ')
                    new_m_name = input('Введите новое отчество: ')
                    new_number = input('Введите новый номер: ')
                    new_contact = {
                        'last_name': new_l_name,
                        'first_name': new_f_name,
                        'middle_name': new_m_name,
                        'phone_number': new_number
                    }
                    phonebook[results[0][0]] = new_contact
                    print('Запись скорректирована')

def delete_data(phonebook):
    flag = True
    while flag:
        search_key = input('Введите имя/фамилию для поиска. Для выхода введите "выход": ')
        if search_key.lower() == 'выход':
            flag = False
        else:
            results = search_contacts(phonebook, search_key)
            if len(results) > 1:
                print('Было найдено более 1 записи, повторите поиск')
            else:
                print(
                    f'{results[0][1]["last_name"]},{results[0][1]["first_name"]},{results[0][1]["middle_name"]},{results[0][1]["phone_number"]}')
                confirmation = input(f'Вы хотите удалить запись? Y/N: ').lower()
                if confirmation == 'y':
                    phonebook.pop(results[0][0])
                    print('Запись удалена')
def load_file(filename):
    phonebook=[]
    try:
        with open(filename, 'r') as file:
            for contact in file:
                last_name, first_name, middle_name, phone_number = contact.split(',')
                phonebook.append({
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'phone_number': phone_number.replace('\n', '')
                })
            print('Данные загружены')
    except FileNotFoundError:
        print('Файл не найден')
    print("=" * 100)
    return phonebook
def search_contacts(phonebook, search_key):
    results = []
    for index, contact in enumerate(phonebook):
        if search_key.lower() in contact['last_name'].lower()  or search_key.lower() in contact['first_name'].lower():
            results.append([index,contact])
    if len(results) == 0:
        print(f'Запись не найдена') 
    else:
        print(f'Найдено {len(results)} записей: ')
    print("=" * 100)
    return results
def views_contacts(phonebook):
    for index,contact in enumerate(phonebook, start=1):
        print(f'({index}) {contact["last_name"]}, {contact["first_name"]}, {contact["middle_name"]}, {contact["phone_number"]}')
    print("="*100)

def safe_to_file(filename, phonebook):
    with open(filename, 'w') as file:
        for contact in phonebook:
            file.write(f'{contact["last_name"]},{contact["first_name"]},{contact["middle_name"]},{contact["phone_number"]}')
    print('Данные сохранены в файле.')
    print("="*100)

def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    contact = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    phonebook.append(contact)
    print('Контакт добавлен.')
    print("="*100)

def main ():
    phonebook = []
    filename = 'contacts.txt'
    flag = True
    while flag:
        print("1. Добавить контакт")
        print("2. Сохранить файл")
        print("3. Вывести все контакты")
        print("4. Поиск по имени/фамилии")
        print("5. Загрузить из файла")
        print("6. Скорректировать данные")
        print("7. Удалить данные")
        print("8. Выйти")
        print("=" * 100)
        choice = input('Выберите действие: ')
        if choice == "1":
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            middle_name = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)
        elif choice == "2":
            safe_to_file(filename, phonebook)
        elif choice == "3":
            views_contacts(phonebook)
        elif choice == "4":
            search_key = input('Введите имя/фамилию для поиска: ')
            results = search_contacts(phonebook, search_key)
            for contact in results:
                print(f'{contact[1]["last_name"]},{contact[1]["first_name"]},{contact[1]["middle_name"]},{contact[1]["phone_number"]}')
        elif choice == '5':
            phonebook = load_file(filename)
        elif choice == '6':
            correct_data(phonebook)
        elif choice == '7':
            delete_data(phonebook)
        elif choice == "8":
            flag = False
        else:
            print("Некорректный выбор. Повторите ввод.")
            print("=" * 100)

if __name__ == '__main__':
    main()