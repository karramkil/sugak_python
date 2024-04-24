def sum_positive_below_diag(matrix):
    sum_positive = sum([matrix[i][j] for i in range(len(matrix)) for j in range(i+1) if matrix[i][j] > 0])
    return sum_positive

# Ввод квадратной матрицы
N = int(input("Введите размер квадратной матрицы: "))
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вычисление суммы положительных элементов под главной диагональю
positive_sum_below_diag = sum_positive_below_diag(matrix)

print("Исходная квадратная матрица:")
for row in matrix:
    print(*row)

print("Сумма положительных элементов под главной диагональю и на ней:", positive_sum_below_diag)
