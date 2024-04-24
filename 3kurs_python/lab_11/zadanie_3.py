numbers = [int(input(f"Введите {i + 1}-е число: ")) for i in range(20)]
max_number = max(numbers)
max_index = numbers.index(max_number)
numbers[0], numbers[max_index] = numbers[max_index], numbers[0]
print("Список после замены наибольшего элемента с первым:", numbers)

numbers = [int(input(f"Введите {i + 1}-е число: ")) for i in range(10)]
min_number = min(numbers)
min_index = numbers.index(min_number)
numbers[min_index] *= 2
print("Список после увеличения наименьшего элемента в два раза:", numbers)

numbers = [int(input(f"Введите {i + 1}-е число: ")) for i in range(15)]
sum_of_squares = sum([num**2 for num in numbers])
print("Сумма квадратов всех элементов списка:", sum_of_squares)

import math
numbers = [int(input(f"Введите {i + 1}-е число: ")) for i in range(12)]
positive_numbers = [num for num in numbers if num > 0]
geometric_mean = math.prod(positive_numbers) ** (1 / len(positive_numbers))
print("Среднее геометрическое всех положительных элементов:", geometric_mean)

numbers = [int(input(f"Введите {i + 1}-е число: ")) for i in range(18)]
max_value = max(numbers)
min_value = min(numbers)
difference = max_value - min_value
print("Разность между максимальным и минимальным значениями:", difference)
