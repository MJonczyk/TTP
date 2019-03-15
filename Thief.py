import numpy as np
import random
from Functions import steal_item


class Thief:
    def __init__(self, cities):
        self.cities = list.copy(cities)
        self.distances = []
        self.f = 0
        self.g = 0
        self.G = 0

    def generate(self):
        random.shuffle(self.cities)

    # f(x, y), g(y), G(x, y)
    def route_distance(self, distances, items, w, v_max, v_min):
        w_c = 0

        for i in range(len(self.cities)):
            stolen_item_index = steal_item(items, self.cities[i].index, w, w_c)

            if stolen_item_index != -1:
                w_c += items[stolen_item_index].weight
                self.g += items[stolen_item_index].profit
            v_c = v_max - w_c * (v_max - v_min) / w

            if i + 1 < len(self.cities):
                t = distances[self.cities[i].index-1][self.cities[i + 1].index-1] / v_c
            else:
                t = distances[self.cities[i].index-1][self.cities[1].index-1] / v_c
            self.f += t
        self.G = self.g - self.f

    # swap
    def mutate(self):
        i = random.randrange(0, len(self.cities))
        j = random.randrange(0, len(self.cities))

        while(j == i):
            j = random.randrange(0, len(self.cities))

        first_city = self.cities[i]
        self.cities[i] = self.cities[j]
        self.cities[j] = first_city

    def cross(self, second_thief):
        a = random.randrange(0, len(self.cities) - 1)
        b = random.randrange(0, len(self.cities))

        while (b <= a):
            b = random.randrange(0, len(self.cities))

        first_alleles = self.cities[a:b]
        second_alleles = second_thief.cities[a:b]
        print(a, b)
        print(first_alleles[0], first_alleles[b-a-1], second_alleles[0], second_alleles[b-a-1])
        for i in range(a, b):
            temp = self.cities[i]
            self.cities[i] = second_thief.cities[i]
            second_thief.cities[i] = temp

        k = 0
        l = 0
        for i in range(0, a):
            for j in range(b - a):
                if self.cities[i].index == second_alleles[j].index:
                    self.cities[i] = first_alleles[k]
                    k += 1
                if second_thief.cities[i].index == first_alleles[j].index:
                    second_thief.cities[i] = second_alleles[l]
                    l += 1

        for i in range(b, len(self.cities)):
            for j in range(b - a):
                if self.cities[i].index == second_alleles[j].index:
                    self.cities[i] = first_alleles[k]
                    k += 1
                if second_thief.cities[i].index == first_alleles[j].index:
                    second_thief.cities[i] = second_alleles[l]
                    l += 1


    def print_cities(self):
        s = ""
        for c in self.cities:
            s += str(c.index)
            s += ", "
        print(s)
