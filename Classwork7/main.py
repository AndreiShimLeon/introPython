# # Задача 49.
# Создать телефонный справочник:
# 1. Программа должна выводить данные;
# 2. Программа должна сохранять данные в текстовом файле;
# 3. Пользователь может ввести одну из характеристик
# для поиска определенной записи (например, имя или фамилию)
# 4. Использование функций. Программа не должны быть линейной.

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
                    'phone_number': phone_number
                })
            print('Данные загружены')
    except FileNotFoundError:
        print('Файл не найден')
    print("=" * 100)
    return phonebook
def search_contacts(phonebook, search_key):
    results = []
    for contact in phonebook:
        if search_key.lower() in contact['last_name'].lower()  or search_key.lower() in contact['first_name'].lower():
            results.append(contact)
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
        print("6. Выйти")
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
            views_contacts(results)
        elif choice == '5':
            phonebook = load_file(filename)
        elif choice == "6":
            flag = False
        else:
            print("Некорректный выбор. Повторите ввод.")
            print("=" * 100)

if __name__ == '__main__':
    main()