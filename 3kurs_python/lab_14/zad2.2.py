def find_specialty_by_group(specialties, query_group):
    for specialty, groups in specialties.items():
        if query_group in groups:
            return specialty
    return ""

# Ввод данных
n = int(input("Введите количество специальностей: "))
specialties = {}
for _ in range(n):
    specialty, groups_str = input().split(" - ")
    groups = groups_str.split(", ")
    specialties[specialty] = groups

query_group = input("Введите номер группы: ")

# Поиск специальности по номеру группы
result = find_specialty_by_group(specialties, query_group)
print(result)
