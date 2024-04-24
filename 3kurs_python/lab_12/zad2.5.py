def sum_positive_above_extra_diag(matrix):
    N = len(matrix)
    sum_positive = sum([matrix[i][j] for i in range(N) for j in range(N) if i+j < N-1 and matrix[i][j] > 0])
    return sum_positive

# Ввод квадратной матрицы
N = int(input("Введите размер квадратной матрицы: "))
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вычисление суммы положительных элементов над дополнительной диагональю
positive_sum_above_extra_diag = sum_positive_above_extra_diag(matrix)

print("Исходная квадратная матрица:")
for row in matrix:
    print(*row)

print("Сумма положительных элементов над дополнительной диагональю:", positive_sum_above_extra_diag)
