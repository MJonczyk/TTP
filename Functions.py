

# greedy algorithm
def steal_item(items, city_index, w, w_c):
    ratio = 0
    stolen_item_index = -1
    for j in range(len(items)):
        if items[j].city_index == city_index:
            if items[j].profit_weight_ratio > ratio and w_c + items[j].weight < w:
                stolen_item_index = j
                ratio = items[j].profit_weight_ratio

    return stolen_item_index