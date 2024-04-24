def find_phone_number(phone_book, query_name):
    if query_name in phone_book:
        return phone_book[query_name]
    else:
        return "Нет в телефонной книге"

# Ввод данных
n = int(input("Введите количество номеров телефонов: "))
phone_book = {}
for _ in range(n):
    phone, name = input().split()
    phone_book[name] = phone

query = input("Введите имя для поиска номера телефона: ")

# Поиск номера телефона по имени
result = find_phone_number(phone_book, query)
print(result)
