import random
from Functions import steal_item


class Thief:
    def __init__(self, cities):
        self.cities = list.copy(cities)
        self.distances = []
        self.f = 0
        self.g = 0
        self.G = 0
        self.fitness = 0
        self.a_wheel = 0
        self.b_wheel = 0

    def generate(self):
        random.shuffle(self.cities)

    # f(x, y), g(y), G(x, y)
    def eval_fitness(self, distances, items, w, v_max, v_min):
        w_c = 0
        self.f = 0
        self.g = 0
        self.G = 0
        self.fitness = 0

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
    def swap_mutate(self):
        i = random.randrange(0, len(self.cities))
        j = random.randrange(0, len(self.cities))

        while(j == i):
            j = random.randrange(0, len(self.cities))

        first_city = self.cities[i]
        self.cities[i] = self.cities[j]
        self.cities[j] = first_city

    # reverse
    def reverse_mutate(self):
        i = random.randrange(0, len(self.cities) - 1)
        j = random.randrange(0, len(self.cities))

        while (j <= i):
            j = random.randrange(0, len(self.cities))

        if i != 0:
            self.cities = self.cities[:i] + self.cities[j:i-1:-1] + self.cities[j+1:]
        else:
            self.cities = self.cities[:i] + self.cities[j::-1] + self.cities[j+1:]

    # PMX
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
            print("i: " + str(i))
            for j in range(b - a):
                if self.cities[i].index == second_alleles[j].index:
                    self.cities[i] = first_alleles[k]
                    k += 1
                if second_thief.cities[i].index == first_alleles[j].index:
                    second_thief.cities[i] = second_alleles[l]
                    l += 1

        for i in range(b, len(self.cities)):
            print("i: " + str())
            for j in range(b - a):
                if self.cities[i].index == second_alleles[j].index:
                    self.cities[i] = first_alleles[k]
                    k += 1
                if second_thief.cities[i].index == first_alleles[j].index:
                    second_thief.cities[i] = second_alleles[l]
                    l += 1

    # OX
    def cross2(self, second_thief):
        size = len(self.cities)
        a = random.randrange(0, size - 1)
        b = random.randrange(0, size)
        k = 0
        l = 0

        while (b <= a):
            b = random.randrange(0, size)

        if a == 0:
            k = b
            l = b

        first_alleles = [x.index for x in self.cities[a:b]]
        second_alleles = [x.index for x in second_thief.cities[a:b]]

        new_thief1 = [0] * size
        new_thief2 = [0] * size

        for i in range(a, b):
            new_thief1[i] = second_thief.cities[i].index
            new_thief2[i] = self.cities[i].index

        for i in range(size):
            if second_thief.cities[i].index not in first_alleles:
                new_thief2[k] = second_thief.cities[i].index
                k += 1
                if k == a:
                    k = b
            if self.cities[i].index not in second_alleles:
                new_thief1[l] = self.cities[i].index
                l += 1
                if l == a:
                    l = b

        for i in range(size):
            self.cities[i] = second_thief.get_city(new_thief1[i])
        for i in range(size):
            second_thief.cities[i] = self.get_city(new_thief2[i])

    def copy(self):
        thief = Thief(list.copy(self.cities))
        thief.g = self.g
        thief.f = self.f
        thief.G = self.G

        return thief

    def print_cities(self):
        s = ""
        for c in self.cities:
            s += str(c.index)
            s += ", "
        print(s)

    def print(self):
        s = ""
        for c in self.cities:
            s += str(c.index)
            s += ", "
        s += str(self.G)
        print(s)

    def get_city(self, index):
        for i in range(len(self.cities)):
            if self.cities[i].index == index:
                return self.cities[i]
