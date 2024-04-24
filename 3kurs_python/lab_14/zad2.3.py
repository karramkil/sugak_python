def find_definition(dictionary, query_word):
    if query_word in dictionary:
        return dictionary[query_word]
    else:
        return "Нет в словаре"

# Ввод данных
n = int(input("Введите количество записей в словаре: "))
dictionary = {}
for _ in range(n):
    word, definition = input().split(" - ")
    dictionary[word] = definition

query_word = input("Введите слово для поиска значения: ")

# Поиск значения по слову в словаре
result = find_definition(dictionary, query_word)
print(result)
