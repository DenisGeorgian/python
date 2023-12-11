class Fractie:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self, x, y):
        return f"{self.x}/{self.y}"

    def __add__(self, other):
        x_nou = self.x * other.y + other.x * self.y
        y_nou = other.x * other.y
        return Fractie(x_nou, y_nou)

    def __sub__(self, other):
        x_nou = self.x * other.y - other.x * self.y
        y_nou = other.x * other.y

    def inverse(self):
        return Fractie(self.y, self.x)




