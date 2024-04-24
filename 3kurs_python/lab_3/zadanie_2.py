a, b, c = float(input("Введите число a: ")), float(input("Введите число b: ")), float(input("Введите число c: "))
a = a ** 2 if a >= 0 else a ** 4
b = b ** 2 if b >= 0 else b ** 4
c = c ** 2 if c >= 0 else c ** 4
print("a =", a)
print("b =", b)
print("c =", c)


a, b = float(input("Введите число a: ")), float(input("Введите число b: "))
if abs(a) > b:
    a = a / 5
print("a =", a)
print("b =", b)


x, y = float(input("Введите число x: ")), float(input("Введите число y: "))
if x < y:
    x, y = (x + y) / 2, 2 * x * y
else:
    x, y = 2 * x * y, (x + y) / 2
print("x =", x)
print("y =", y)


m, n = int(input("Введите число m: ")), int(input("Введите число n: "))
if m != n:
    m, n = max(m, n), max(m, n)
else:
    m, n = 0, 0
print("m =", m)
print("n =", n)

a, b, c = float(input("Введите число a: ")), float(input("Введите число b: ")), float(input("Введите число c: "))
negative_count = 0
if a < 0:
    negative_count += 1
if b < 0:
    negative_count += 1
if c < 0:
    negative_count += 1
print("Количество отрицательных чисел:", negative_count)


a, b, c = float(input("Введите число a: ")), float(input("Введите число b: ")), float(input("Введите число c: "))
positive_count = 0
if a > 0:
    positive_count += 1
if b > 0:
    positive_count += 1
if c > 0:
    positive_count += 1
print("Количество положительных чисел:", positive_count)


a, b, c = float(input("Введите число a: ")), float(input("Введите число b: ")), float(input("Введите число c: "))
two_digit_count = 0
if 10 <= a < 100:
    two_digit_count += 1
if 10 <= b < 100:
    two_digit_count += 1
if 10 <= c < 100:
    two_digit_count += 1
print("Количество двухзначных чисел:", two_digit_count)


temperature = float(input("Введите температуру в комнате: "))
if temperature > 60:
    print("Пожароопасная ситуация")


m, n = float(input("Введите массу первого пакета: ")), float(input("Введите массу второго пакета: "))
if m > n:
    print("Первый пакет тяжелее")
elif m < n:
    print("Второй пакет тяжелее")
else:
    print("Пакеты имеют одинаковую массу")

m, n = float(input("Введите массу первого пакета: ")), float(input("Введите массу второго пакета: "))
if m > n:
    print("Масса более тяжелого пакета:", m)
else:
    print("Масса более тяжелого пакета:", n)
