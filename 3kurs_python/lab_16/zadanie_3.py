def is_three_digit_and_divisible_by_8(num):
    return 100 <= num < 1000 and num % 8 == 0

def is_negative(num):
    return num < 0


def is_even(num):
    return num % 2 == 0

def divisible_by_17(num):
    return num % 17 == 0

def is_three_digit_even_and_divisible_by_6(num):
    return 100 <= num < 1000 and num % 2 == 0 and num % 6 == 0

numbers = list(map(int, input("Введите числа через пробел: ").split()))

sum_cubed_3_digit_divisible_by_8 = sum([num**3 for num in numbers if is_three_digit_and_divisible_by_8(num)])
sum_cubed_negative = sum([num**3 for num in numbers if is_negative(num)])
even_numbers = [num for num in numbers if is_even(num)]
divisible_by_17_numbers = [num for num in numbers if divisible_by_17(num)]
three_digit_even_divisible_by_6 = [num for num in numbers if is_three_digit_even_and_divisible_by_6(num)]

print("Сумма кубов всех трехзначных чисел, делящихся на 8:", sum_cubed_3_digit_divisible_by_8)
print("Сумма кубов отрицательных чисел:", sum_cubed_negative)
print("Четные числа:", even_numbers)
print("Числа, делимые на 17:", divisible_by_17_numbers)
print("Трехзначные четные числа, делящиеся на 6:", three_digit_even_divisible_by_6)
input()
