import fill_module

N = int(input("Сколько элементов списка следует заполнить? "))
K = int(input("Введите значение для заполнения: "))

A = []
A = fill_module.fill_elements(A, N, K)

print("Список A после заполнения:", A)