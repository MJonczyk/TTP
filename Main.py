from Loader import load_data
from Thief import Thief
from Logger import Logger
from Population import Population
import os

filename = 'data/trivial_0.ttp'
(variables, cities, distances, items) = load_data(filename)

NUMBER_OF_THIEVES = 100
NUMBER_OF_GENERATIONS = 100
CROSSOVER_PROBABILITY = 0.7
MUTATION_PROBABILITY = 0.1

logger = Logger('trivial_0')
logger.create_file()

pop = Population(NUMBER_OF_THIEVES, distances, cities, items, variables['w'], variables['v_max'], variables['v_min'], CROSSOVER_PROBABILITY, MUTATION_PROBABILITY, 5)
pop.initialize()
pop.evaluate()
for i in range(NUMBER_OF_GENERATIONS):
    line = []
    pop.tournament_selection()
    pop.crossover()
    pop.mutation()
    pop.evaluate()
    line.append(i)
    line.append(pop.get_best())
    line.append(pop.get_average())
    line.append(pop.get_worst())
    logger.write(line)
    print(str(i) + ";" + pop.to_string())
