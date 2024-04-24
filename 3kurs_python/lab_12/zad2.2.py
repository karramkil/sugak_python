def sum_rows(matrix):
    row_sums = [sum(row) for row in matrix]
    return row_sums

# Ввод матрицы
M = int(input("Введите количество строк матрицы: "))
N = int(input("Введите количество столбцов матрицы: "))
matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вычисление суммы элементов каждой строки
row_sums = sum_rows(matrix)

print("Исходная матрица:")
for row in matrix:
    print(*row)

print("Суммы элементов каждой строки:", row_sums)
