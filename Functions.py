

# greedy algorithm
def steal_item(city, w, w_c):
    i = 0
    while i < len(city.items):
        if city.items[i].weight + w_c < w:
            return i
        i += 1
    return -1
