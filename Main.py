from Loader import load_data
from Thief import Thief
from TravellingThiefProblem import TravellingThiefProblem

filename = 'data/trivial_0.ttp'
(variables, cities, distances, items) = load_data(filename)

NUMBER_OF_THIEVES = 10
NUMBER_OF_GENERATIONS = 10
CROSSOVER_PROBABILITY = 0
MUTATION_PROBABILITY = 0
# thief = Thief(cities)
# thief.generate()
# thief2 = Thief(cities)
# thief2.generate()
# thief.eval_fitness(distances, items, variables['w'], variables['v_max'], variables['v_min'])
# thief2.eval_fitness(distances, items, variables['w'], variables['v_max'], variables['v_min'])
# print(thief.f, thief2.f)
# print(thief.g, thief2.g)
# print(thief.G, thief2.G)
# thief.print_cities()
# thief2.print_cities()
# thief.cross(thief2)
# thief.print_cities()
# thief2.print_cities()

ttp = TravellingThiefProblem(NUMBER_OF_THIEVES, NUMBER_OF_GENERATIONS, distances, cities, items, variables['w'], variables['v_max'], variables['v_min'], CROSSOVER_PROBABILITY, MUTATION_PROBABILITY)
ttp.initialize()
ttp.print_generation()
ttp.evaluate()
ttp.print_generation()
ttp.roulette_selection()
ttp.evaluate()
ttp.print_generation()
