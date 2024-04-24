for hours in range(3, 25, 3):
    amoeba = 2 ** (hours // 3)
    print(f"Через {hours} часов будет {amoeba} амёб")
    

    
n = 15
numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(n)]
sum_numbers = sum(numbers)
prod_numbers = 1
for num in numbers:
    prod_numbers *= num
print("Сумма чисел:", sum_numbers)
print("Произведение чисел:", prod_numbers)


X = 10
total_distance = X
for day in range(2, 8):
    X *= 1.1
    total_distance += X
print("Суммарный путь за неделю:", total_distance)


A = int(input("Введите размер стипендии: "))
B = int(input("Введите расходы на проживание: "))
total_money_needed = 0
for month in range(1, 11):
    total_money_needed += B
    B *= 1.03
total_money_needed += A * 10
print("Необходимо попросить у родителей:", total_money_needed)


U = 40
total_pages = U
for day in range(2, 11):
    U *= 1.05
    total_pages += U
print("В книге страниц:", round(total_pages))


k = 3
total_sum = 0
for num in range(1000, 10000):
    if num % k == 0:
        total_sum += num
print("Сумма всех 4-значных чисел, кратных", k, ":", total_sum)


total_sum_cubes = sum([num**3 for num in range(7, 38, 2)])
print("Сумма кубов нечетных чисел от 7 до 37:", total_sum_cubes)


n = 30
total_sum_squares_even = sum([num**2 for num in range(2, n*2+1, 2)])
print("Сумма квадратов первых", n, "-четных чисел натурального ряда:", total_sum_squares_even)


n = 40
total_sum_squares_odd = sum([num**2 for num in range(1, n*2, 2)])
print("Сумма квадратов первых", n, "-нечетных чисел натурального ряда:", total_sum_squares_odd)


total_sum_cubes_even = sum([num**3 for num in range(6, 37, 2)])
print("Сумма кубов четных чисел от 6 до 36:", total_sum_cubes_even)
input()
