import random
import string
from datetime import datetime, timedelta

def generate_passwords(N, K):
    пароли = set()
    while len(пароли) < N:
        пароль = ''.join(random.choices(string.ascii_letters + string.digits, k=K))
        пароли.add(пароль)
    return пароли

def generate_exam_schedule(num_exams, дисциплины):
    дни = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    времена = [str(i) + ':00' for i in range(9, 15) if i != 12]
    
    for номер_экзамена in range(1, num_exams + 1):
        дисциплина = random.choice(дисциплины)
        день = random.choice(дни)
        время = random.choice(времена)
        номер_билета = random.randint(1, 20)
        print(f"Экзамен по '{дисциплина}' состоится в {день} в {время}. Ваш счастливый номер билета: {номер_билета}.")

def дней_до_экзамена(K):
    текущая_дата = datetime.now()
    дата_экзамена = текущая_дата + timedelta(days=K)
    return дата_экзамена.strftime("%B %d")

def счастливые_даты_экзаменов(начальная_дата, n):
    текущая_дата = datetime.strptime(начальная_дата, "%Y/%m/%d")
    счастливые_даты = []
    
    while len(счастливые_даты) < 3:
        текущая_дата += timedelta(days=n)
        if текущая_дата.weekday() != 0 and текущая_дата.day % 4 != 0:
            счастливые_даты.append(текущая_дата.strftime("%d %B, %A"))
    
    return счастливые_даты

# Задание 1
N = 5
K = 8
пароли = generate_passwords(N, K)
print("Сгенерированные пароли:")
for пароль in пароли:
    print(пароль)

# Задание 2
num_exams = 4
дисциплины = "Математика, Физика, Химия, История".split(", ")
generate_exam_schedule(num_exams, дисциплины)

# Задание 3
K = 10
дата_экзамена = дней_до_экзамена(K)
print(f"Экзамен будет {дата_экзамена}.")

# Задание 4
начальная_дата = "2022/11/01"
n = 7
счастливые_даты = счастливые_даты_экзаменов(начальная_дата, n)
print("Счастливые даты экзаменов:")
for дата in счастливые_даты:
    print(дата)
