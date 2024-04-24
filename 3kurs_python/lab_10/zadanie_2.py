print("Введите непустую последовательность символов:")
sequence = input()
digits_set = {char for char in sequence if char.isdigit()}
print("Множество цифр от '0' до '9':", digits_set)

print("Введите непустую последовательность символов:")
sequence = input()

digits_set = {char for char in sequence if char.isdigit()}
print("Множество цифр от '0' до '9':", digits_set)

print("Введите непустую последовательность символов:")
sequence = input()

digits_set = {char for char in sequence if char.isdigit()}
print("Множество цифр от '0' до '9':", digits_set)

print("Введите непустую последовательность символов:")
sequence = input()

digits_operators_set = {char for char in sequence if (char.isdigit() and int(char) >= 5) or char in "+-*/"}
print("Множество цифр от '5' до '9' и знаков арифметических операций:", digits_operators_set)

print("Введите непустую последовательность символов:")
sequence = input()

operators_punctuation_set = {char for char in sequence if char in "+-*/.,;:!?()[]{}"}
print("Множество знаков арифметических операций и знаков препинания:", operators_punctuation_set)

print("Введите непустую последовательность символов:")
sequence = input()
punctuation_relations_set = {char for char in sequence if char in "<>=.,;:!?()[]{}"}
print("Множество знаков препинания и операций отношения:", punctuation_relations_set)

input()
