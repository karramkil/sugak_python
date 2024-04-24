def print_matrix_snake(matrix):
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            print(*row)
        else:
            print(*row[::-1])

# Пример матрицы 3x4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Исходная матрица:")
for row in matrix:
    print(*row)

print("\nВывод элементов в змейке:")
print_matrix_snake(matrix)
