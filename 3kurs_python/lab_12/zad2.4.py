def sum_negative_above_diag(matrix):
    sum_negative = sum([matrix[i][j] for i in range(len(matrix)) for j in range(i) if matrix[i][j] < 0])
    return sum_negative

# Ввод квадратной матрицы
N = int(input("Введите размер квадратной матрицы: "))
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вычисление суммы отрицательных элементов над главной диагональю
negative_sum_above_diag = sum_negative_above_diag(matrix)

print("Исходная квадратная матрица:")
for row in matrix:
    print(*row)

print("Сумма отрицательных элементов над главной диагональю:", negative_sum_above_diag)
