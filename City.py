class City:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.index)
