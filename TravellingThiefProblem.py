import random
from Thief import Thief


class TravellingThiefProblem:
    def __init__(self, number_of_thieves, number_of_generations, distances, cities, items, w, v_max, v_min, p_c, p_m):
        self.number_of_thieves = number_of_thieves
        self.number_of_generations = number_of_generations
        self.thieves = []
        self.distances = distances
        self.cities = cities
        self.items = items
        self.w = w
        self.v_max = v_max
        self.v_min = v_min
        self.p_c = p_c
        self.p_m = p_m

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
                self.thieves[i].cross(self.thieves[ind])

    def mutation(self):
        for i in range(self.number_of_thieves):
            if random.random() < self.p_m:
                self.thieves[i].mutate()

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

    def tournament_selection(self):
        """"""

    def print_generation(self):
        for i in range(self.number_of_thieves):
            self.thieves[i].print()
