def find_students_by_specialty(students, query_specialty):
    student_names = [student[0] for student in students if student[1] == query_specialty]
    if student_names:
        return ", ".join(student_names)
    else:
        return "Проверьте запрос"

# Ввод данных
n = int(input("Введите количество студентов: "))
students = [input().split() for _ in range(n)]
query_specialty = input("Введите название специальности: ")

# Поиск студентов по специальности
result = find_students_by_specialty(students, query_specialty)
print(result)
