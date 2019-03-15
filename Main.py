from Loader import load_data
from Thief import Thief

filename = 'data/trivial_0.ttp'
(variables, cities, distances, items) = load_data(filename)

thief = Thief(cities)
thief.generate()
thief2 = Thief(cities)
thief2.generate()
thief.route_distance(distances, items, variables['w'], variables['v_max'], variables['v_min'])
thief2.route_distance(distances, items, variables['w'], variables['v_max'], variables['v_min'])
print(thief.f, thief2.f)
print(thief.g, thief2.g)
print(thief.G, thief2.G)
thief.print_cities()
thief2.print_cities()
thief.cross(thief2)
thief.print_cities()
thief2.print_cities()

