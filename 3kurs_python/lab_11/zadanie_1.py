n = int(input("Введите количество оценок: "))
grades = []
for _ in range(n):
    grade = float(input("Введите оценку: "))
    grades.append(grade)
print("Введенные оценки:", grades)
average_grade = sum(grades) / n
print("Средняя оценка за урок:", average_grade)
