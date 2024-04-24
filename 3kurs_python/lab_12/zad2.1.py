def sum_columns(matrix):
    sums = [sum(col) for col in zip(*matrix)]
    return sums

# Ввод матрицы
M = int(input("Введите количество строк матрицы: "))
N = int(input("Введите количество столбцов матрицы: "))
matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вычисление суммы элементов каждого столбца
column_sums = sum_columns(matrix)

print("Исходная матрица:")
for row in matrix:
    print(*row)

print("Суммы элементов каждого столбца:", column_sums)
