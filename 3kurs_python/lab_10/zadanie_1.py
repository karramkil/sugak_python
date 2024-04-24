print("Введите первое множество чисел через пробел:")
set1 = set(map(int, input().split()))

print("Введите второе множество чисел через пробел:")
set2 = set(map(int, input().split()))

unique_numbers = set1.union(set2)
print("Уникальные числа в обоих множествах:", unique_numbers)

common_numbers = sorted(set1.intersection(set2))
print("Числа, входящие в оба множества в порядке возрастания:", common_numbers)
