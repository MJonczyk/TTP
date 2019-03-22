from Population import Population
from Logger import Logger


class TravellingThiefProblem:
    def __init__(self, logfile, header, number_of_populations, number_of_generations, number_of_thieves, distances, cities, w, v_max, v_min, p_c, p_m, tournament_size=0):
        self.number_of_populations = number_of_populations
        self.number_of_generations = number_of_generations
        self.populations = []
        self.tournament_size = tournament_size
        self.logger = Logger(logfile, header)
        for i in range(number_of_populations):
            self.populations.append(Population(number_of_thieves, distances, cities, w, v_max, v_min, p_c, p_m, tournament_size))

    def initialize(self):
        self.logger.create_file()

    def selection(self):
        if self.tournament_size == 0:
            for i in range(self.number_of_populations):
                self.populations[i].roulette_selection()
        else:
            for i in range(self.number_of_populations):
                self.populations[i].tournament_selection()

    def get_best(self):
        sum = 0
        for i in range(self.number_of_populations):
            sum += self.populations[i].get_best()
        return sum / self.number_of_populations

    def get_average(self):
        sum = 0
        for i in range(self.number_of_populations):
            sum += self.populations[i].get_average()
        return sum / self.number_of_populations

    def get_worst(self):
        sum = 0
        for i in range(self.number_of_populations):
            sum += self.populations[i].get_worst()
        return sum / self.number_of_populations

    def evaluate(self):
        for i in range(self.number_of_populations):
            self.populations[i].initialize()
        for i in range(self.number_of_populations):
            self.populations[i].evaluate()
        for i in range(self.number_of_generations):
            line = []
            self.selection()
            for j in range(self.number_of_populations):
                self.populations[j].crossover()
            for j in range(self.number_of_populations):
                self.populations[j].mutation()
            for j in range(self.number_of_populations):
                self.populations[j].evaluate()
            line.append(i)
            line.append(self.get_best())
            line.append(self.get_average())
            line.append(self.get_worst())
            self.logger.write(line)
            print(str(i) + ";" + self.to_string())

    def to_string(self):
        return str(self.get_best()) + ";" + str(self.get_average()) + ";" + str(self.get_worst())