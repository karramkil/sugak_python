num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} делится на {num2}")
else:
    print(f"{num1} не делится на {num2}")
