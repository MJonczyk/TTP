from Loader import load_data
from Logger import Logger
from Population import Population
from TravellingThiefProblem import TravellingThiefProblem

filename = 'data/hard_4.ttp'
(variables, cities, distances, items) = load_data(filename)

NUMBER_OF_POPULATIONS = 5
NUMBER_OF_GENERATIONS = 100
NUMBER_OF_THIEVES = 100
CROSSOVER_PROBABILITY = 0.7
MUTATION_PROBABILITY = 0.5
TOURNAMENT_SIZE = 5

header = ('p' + str(NUMBER_OF_THIEVES), 'g' + str(NUMBER_OF_GENERATIONS), 'pc' + str(CROSSOVER_PROBABILITY), 'pm' + str(MUTATION_PROBABILITY), 'tour' + str(TOURNAMENT_SIZE))
header = '_'.join(header)
logfile = filename[5:-4]

ttp = TravellingThiefProblem(logfile, header, NUMBER_OF_POPULATIONS, NUMBER_OF_GENERATIONS, NUMBER_OF_THIEVES, distances, cities, variables['w'], variables['v_max'], variables['v_min'], CROSSOVER_PROBABILITY, MUTATION_PROBABILITY, TOURNAMENT_SIZE)
ttp.initialize()
ttp.evaluate()

# filename = 'data/hard_4.ttp'
# (variables, cities, distances, items) = load_data(filename)
# logfile = filename[5:-4]
#
# ttp = TravellingThiefProblem(logfile, header, NUMBER_OF_POPULATIONS, NUMBER_OF_GENERATIONS, NUMBER_OF_THIEVES, distances, cities, variables['w'], variables['v_max'], variables['v_min'], CROSSOVER_PROBABILITY, MUTATION_PROBABILITY, TOURNAMENT_SIZE)
# ttp.initialize()
# ttp.evaluate()

# pop = Population(NUMBER_OF_THIEVES, distances, cities, variables['w'], variables['v_max'], variables['v_min'], CROSSOVER_PROBABILITY, MUTATION_PROBABILITY, TOURNAMENT_SIZE)
# logger = Logger(logfile, header)
# pop.initialize()
# pop.evaluate()
# for i in range(NUMBER_OF_GENERATIONS):
#     line = []
#     pop.tournament_selection()
#     pop.crossover()
#     pop.mutation()
#     pop.evaluate()
#     line.append(i)
#     line.append(pop.get_best())
#     line.append(pop.get_average())
#     line.append(pop.get_worst())
#     logger.write(line)
#     print(str(i) + ";" + pop.to_string())

