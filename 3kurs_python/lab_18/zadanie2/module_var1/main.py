import filter_module

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5

B = filter_module.filter_elements(A, K)

print("Список A:", A)
print("Значение K:", K)
print("Список B после фильтрации:", B)