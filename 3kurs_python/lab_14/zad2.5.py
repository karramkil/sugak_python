def find_country_by_city(geography_dict, query_city):
    for country, cities in geography_dict.items():
        if query_city in cities:
            return country
    return ""

# Ввод данных
n = int(input("Введите количество стран: "))
geography_dict = {}
for _ in range(n):
    country, *cities = input().split()
    geography_dict[country] = cities

query_city = input("Введите название города: ")

# Поиск страны по названию города
result = find_country_by_city(geography_dict, query_city)
print(result)
