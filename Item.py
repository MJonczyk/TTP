class Item:
    def __init__(self, index, profit, weight, city_index):
        self.index = index
        self.profit = profit
        self.weight = weight
        self.city_index = city_index
        self.profit_weight_ratio = self.profit / self.weight