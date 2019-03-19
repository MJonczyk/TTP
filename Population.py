import random
from Thief import Thief


class Population:
    def __init__(self, number_of_thieves, distances, cities, items, w, v_max, v_min, p_c, p_m, tournament_size=0):
        self.number_of_thieves = number_of_thieves
        self.thieves = []
        self.distances = distances
        self.cities = cities
        self.items = items
        self.w = w
        self.v_max = v_max
        self.v_min = v_min
        self.p_c = p_c
        self.p_m = p_m
        self.tournament_size = tournament_size

    def initialize(self):
        for i in range(self.number_of_thieves):
            self.thieves.append(Thief(self.cities))
            self.thieves[i].generate()

    def evaluate(self):
        for i in range(self.number_of_thieves):
            self.thieves[i].eval_fitness(self.distances, self.items, self.w, self.v_max, self.v_min)

    def crossover(self):
        for i in range(self.number_of_thieves):
            if random.random() < self.p_c:
                ind = random.randrange(0, self.number_of_thieves)
                while ind == i:
                    ind = random.randrange(0, self.number_of_thieves)
                self.thieves[i].cross2(self.thieves[ind])

    def mutation(self):
        for i in range(self.number_of_thieves):
            if random.random() < self.p_m:
                self.thieves[i].reverse_mutate()

    def roulette_selection(self):
        sum_of_fitness = 0
        sum_of_probability = 0
        for i in range(self.number_of_thieves):
            sum_of_fitness -= self.thieves[i].G

        for i in range(self.number_of_thieves):
            probability = -self.thieves[i].G / sum_of_fitness
            self.thieves[i].a_wheel = sum_of_probability
            sum_of_probability += probability
            self.thieves[i].b_wheel = sum_of_probability

        next_generation = []
        while len(next_generation) < len(self.thieves):
            ind = random.random()
            for i in range(len(self.thieves)):
                if self.thieves[i].b_wheel > ind > self.thieves[i].a_wheel:
                    next_generation.append(self.thieves[i].copy())

        self.thieves = next_generation

    def roulette_selection2(self):
        worst_G = -(sorted(self.thieves, key=lambda x: x.G)[0]) + 1
        sum_of_fitness = 0
        sum_of_probability = 0
        for i in range(self.number_of_thieves):
            sum_of_fitness -= self.thieves[i].G

        for i in range(self.number_of_thieves):
            probability = -self.thieves[i].G / sum_of_fitness
            self.thieves[i].a_wheel = sum_of_probability
            sum_of_probability += probability
            self.thieves[i].b_wheel = sum_of_probability

        next_generation = []
        while len(next_generation) < len(self.thieves):
            ind = random.random()
            for i in range(len(self.thieves)):
                if self.thieves[i].b_wheel > ind > self.thieves[i].a_wheel:
                    next_generation.append(self.thieves[i].copy())

        self.thieves = next_generation

    def tournament_selection(self):
        new_thieves = []
        for i in range(self.number_of_thieves):
            competitors = []
            for j in range(self.tournament_size):
                ind = random.randrange(0, self.number_of_thieves)
                competitors.append(self.thieves[ind])
            competitors.sort(key=lambda x: x.G, reverse=True)
            new_thieves.append(competitors[0].copy())
        self.thieves = new_thieves

    def print_generation(self):
        for i in range(self.number_of_thieves):
            self.thieves[i].print()

    def to_string(self):
        worst = min([x.G for x in self.thieves])
        best = max([x.G for x in self.thieves])
        average = sum([x.G for x in self.thieves]) / self.number_of_thieves
        return str(best) + ";" + str(average) + ";" + str(worst)

    def get_best(self):
        return max([x.G for x in self.thieves])

    def get_average(self):
        return sum([x.G for x in self.thieves]) / self.number_of_thieves

    def get_worst(self):
        return min([x.G for x in self.thieves])