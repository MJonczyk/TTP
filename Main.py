from Loader import load_data
from TravellingThiefProblem import TravellingThiefProblem

filename = 'data/hard_0.ttp'
(variables, cities, distances, items) = load_data(filename)

NUMBER_OF_POPULATIONS = 5
NUMBER_OF_GENERATIONS = 100
NUMBER_OF_THIEVES = 100
CROSSOVER_PROBABILITY = 0.7
MUTATION_PROBABILITY = 0.01
TOURNAMENT_SIZE = 5

header = ('p' + str(NUMBER_OF_THIEVES), 'g' + str(NUMBER_OF_GENERATIONS), 'pc' + str(CROSSOVER_PROBABILITY), 'pm' + str(MUTATION_PROBABILITY))
header = '_'.join(header)
logfile = filename[5:-4]
# logger = Logger(logfile, header)
# logger.create_file()
# pop = Population(NUMBER_OF_THIEVES, distances, cities, variables['w'], variables['v_max'], variables['v_min'], CROSSOVER_PROBABILITY, MUTATION_PROBABILITY, TOURNAMENT_SIZE)
# pop.initialize()
# pop.evaluate()
# for i in range(NUMBER_OF_GENERATIONS):
#     line = []
#     pop.roulette_selection()
#     # pop.tournament_selection()
#     pop.crossover()
#     pop.mutation()
#     pop.evaluate()
#     line.append(i)
#     line.append(pop.get_best())
#     line.append(pop.get_average())
#     line.append(pop.get_worst())
#     logger.write(line)
#     print(str(i) + ";" + pop.to_string())

ttp = TravellingThiefProblem(logfile, header, NUMBER_OF_POPULATIONS, NUMBER_OF_GENERATIONS, NUMBER_OF_THIEVES, distances, cities, variables['w'], variables['v_max'], variables['v_min'], CROSSOVER_PROBABILITY, MUTATION_PROBABILITY, TOURNAMENT_SIZE)
ttp.initialize()
ttp.evaluate()
