def find_vacation_workers(vacation_schedule, query_month):
    workers = [worker for worker, month in vacation_schedule.items() if month == query_month]
    return " ".join(workers)

# Ввод данных
n = int(input("Введите количество сотрудников: "))
vacation_schedule = {}
for _ in range(n):
    worker, day, month = input().split()
    vacation_schedule[worker] = month

query_month = input("Введите месяц для поиска сотрудников в отпуске: ")

# Поиск сотрудников в отпуске в указанном месяце
result = find_vacation_workers(vacation_schedule, query_month)
print(result)
