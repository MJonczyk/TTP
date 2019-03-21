class City:
    def __init__(self, index, x, y, items):
        self.index = index
        self.x = x
        self.y = y
        self.items = items

    def __str__(self):
        return str(self.index)
