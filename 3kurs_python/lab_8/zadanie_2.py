user_input = input("Введите строку, заканчивающуюся точкой: ")
if user_input.endswith('.'):
    user_input = user_input[:-1]
words = user_input.split()
word_count = len(words)
print(f"Количество слов в строке: {word_count}")
input()
