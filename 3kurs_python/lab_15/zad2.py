# Задание 1
def S(r):
    return 3.14159 * r**2

def l(r):
    return 2 * 3.14159 * r

def krug():
    radius = float(input("Введите радиус окружности: "))
    area = S(radius)
    circumference = l(radius)
    print("Площадь круга:", area)
    print("Длина окружности:", circumference)

krug()

# Задание 2
def filter_even_numbers_above_10(numbers):
    return [num for num in numbers if num % 2 == 0 and num > 10]

def count_spaces(string):
    space_count = string.count(' ')
    if space_count % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")

def print_average_of_list(numbers):
    if not numbers:
        print(0)
    else:
        avg = sum(numbers) / len(numbers)
        print(avg)

def print_sum_and_product_of_list(numbers):
    if not numbers:
        print(0)
    else:
        total_sum = sum(numbers)
        total_product = 1
        for num in numbers:
            total_product *= num
        print("Сумма элементов:", total_sum)
        print("Произведение элементов:", total_product)

def check_triangle_sides(sides):
    a, b, c = sides
    if a + b > c and a + c > b and b + c > a:
        print("Это треугольник")
    else:
        print("Это не треугольник")

# Задание 3
def process_lists(list1, a, b, c):
    filtered_elements = [num for num in list1 if num > a and num < b and num % c == 0]
    sum_of_others = sum([num for num in list1 if num not in filtered_elements])
    return filtered_elements, sum_of_others

# Пример использования функций
list1 = [5, 15, 20, 25, 30]
a, b, c = 10, 25, 5
filtered_elements, sum_of_others = process_lists(list1, a, b, c)
print("Элементы, удовлетворяющие условиям:", filtered_elements)
print("Сумма остальных элементов:", sum_of_others)
