
A = [int(input(f"Введите {i + 1}-й элемент списка A: ")) for i in range(20)]
negative_count = len([num for num in A if num < 0])
print("Количество отрицательных элементов списка A:", negative_count)


B = [int(input(f"Введите {i + 1}-й элемент списка B: ")) for i in range(15)]
positive_sum = sum([num for num in B if num > 0])
print("Сумма положительных элементов списка B:", positive_sum)

C = [int(input(f"Введите {i + 1}-й элемент списка C: ")) for i in range(25)]

average = sum(C) / len(C)
print("Среднее арифметическое всех элементов списка C:", average)


D = [int(input(f"Введите {i + 1}-й элемент списка D: ")) for i in range(12)]

product = 1
for num in D:
    product *= num
print("Произведение всех элементов списка D:", product)

from collections import Counter

E = [int(input(f"Введите {i + 1}-й элемент списка E: ")) for i in range(18)]

counter = Counter(E)
most_common_element = counter.most_common(1)[0][0]
print("Самый часто встречающийся элемент списка E:", most_common_element)
input()

