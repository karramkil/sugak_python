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

# Пример использования функций
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
filtered_numbers = filter_even_numbers_above_10(numbers)
print("Четные числа больше 10:", filtered_numbers)

string_input = input("Введите строку: ")
count_spaces(string_input)

list_for_avg = list(map(int, input("Введите список целых чисел через пробел: ").split()))
print_average_of_list(list_for_avg)

list_for_sum_prod = list(map(float, input("Введите список вещественных чисел через пробел: ").split()))
print_sum_and_product_of_list(list_for_sum_prod)

triangle_sides = list(map(int, input("Введите три числа (длины отрезков) через пробел: ").split()))
check_triangle_sides(triangle_sides)
