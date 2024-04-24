input_string = input("Введите строку из нескольких слов: ")
output_string = "-".join([word.upper() for word in input_string.split()])
print("Результат:", output_string)


input_string = input("Введите строку: ").lower()
max_count = max([input_string.count(char) for char in set(input_string)])
print("Максимальное количество повторений для одной буквы:", max_count)


numbers = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
start, end = map(int, input("Введите два целых числа X и Y: ").split())
sum_numbers = sum(numbers[start:end+1])
print("Сумма чисел от номера X до номера Y:", sum_numbers)


numbers = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
start, end = map(int, input("Введите два целых числа X и Y: ").split())

product = 1
for num in numbers[start:end+1]:
    product *= num
print("Произведение чисел от номера X до номера Y:", product)



numbers = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
start, end = map(int, input("Введите два целых числа X и Y: ").split())
sum_of_squares = sum([num**2 for num in numbers[start:end+1]])
print("Сумма квадратов чисел от номера X до номера Y:", sum_of_squares)
