distance = 10
day = 1
total_distance = 0

while day <= 7:
    total_distance += distance
    distance *= 1.1
    day += 1

print(f"Суммарный пробег спортсмена за неделю: {total_distance} км")
