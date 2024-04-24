import math

a = -0.5
b = 2

t = float(input("Введите значение t (от 1 до 2): "))

if t >= 1 and t <= 2:
    y = (a * t ** 2 * math.log(t)) / (math.exp(a * t) * math.cos(b * t))
    print(f"Значение функции y при t={t}: {y}")
else:
    print("Ошибка: значение t должно быть в диапазоне от 1 до 2")
