sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480)
}

distances = {}

cities = list(sites.keys())

for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        city1 = cities[i]
        city2 = cities[j]
        
        x1, y1 = sites[city1]
        x2, y2 = sites[city2]
        
        distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
        
        distances[(city1, city2)] = distance

print(distances)

