import numpy as np
from City import City
from Item import Item
import math


def load_data(filename):
    data = []
    variables = {}

    with open(filename) as f:
        for line in f:
            x = line.split()
            l = ' '.join(x)
            data.append(l)

    variables['PROBLEM_NAME'] = data[0].split()[2]
    variables['KNAPSACK_DATA_TYPE'] = data[1].split()[3]
    variables['dim'] = int(data[2].split()[1])
    variables['number_of_items'] = int(data[3].split()[3])
    variables['w'] = int(data[4].split()[3])
    variables['v_min'] = float(data[5].split()[2])
    variables['v_max'] = float(data[6].split()[2])
    variables['EDGE_WEIGHT_TYPE'] = data[8].split()[1]

    dim = variables['dim']
    number_of_items = variables['number_of_items']

    cities = data[10:(10 + dim)]
    cities = load_cities(cities)
    items = data[(10 + dim + 1):(10 + dim + 1 + number_of_items)]
    items = load_items(items)

    distances = np.empty([dim, dim])
    for i in range(dim):
        for j in range(dim):
            distances[i][j] = int(math.ceil(math.sqrt((cities[i].x - cities[j].x) ** 2 + (cities[i].y - cities[j].y) ** 2)))

    distances.astype(int)

    return (variables, cities, distances, items)


def load_cities(cities):
    cities = [c.split() for c in cities]
    cities = np.array(cities)
    cities = cities.astype(float)
    cities = [City(int(c[0]), c[1], c[2]) for c in cities]
    return cities


def load_items(items):
    items = [i.split() for i in items]
    items = [Item(int(i[0]), float(i[1]), float(i[2]), int(i[3])) for i in items]
    return items


if __name__ == "__main__":
    (variables, cities, distances, items) = load_data('data/trivial_0.ttp')
    print(variables)
    for c in cities:
        print(c.index)
    print(cities)
    print(distances)
    for i in items:
        print(i.city_index)