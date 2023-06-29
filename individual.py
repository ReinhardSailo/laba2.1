def calculate_population_density(population, area):
    density = population / area
    return density

population = int(input("Введите количество жителей в государстве: "))
area = float(input("Введите площадь территории государства: "))

population_density = calculate_population_density(population, area)

print("Плотность населения в государстве составляет:", population_density, "чел/км²")
