print("Введите слово:")
word = input()

if len(word) >= 4:
    print(f"Четвертая буква в слове '{word}' - {word[3]}")
else:
    print("НЕТ")


print("Введите слова, начинающиеся на букву 'C':")
while True:
    word = input()
    if word.lower().startswith('c'):
        print(word)
    else:
        break


print("Введите число:")
num = int(input())

if num % 2 == 0:
    print(f"Число {num} - четное")
else:
    print(f"Число {num} - нечетное")


print("Введите строку:")
string = input()

if string == string[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")


print("Введите целое число:")
num = int(input())

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} не является простым числом")
            break
    else:
        print(f"{num} - простое число")
else:
    print(f"{num} не является простым числом")
    input()
