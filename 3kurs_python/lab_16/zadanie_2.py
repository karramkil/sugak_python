import math

n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

C = factorial(n) / (factorial(m) * factorial(n - m))
print("Значение выражения C =", C)
