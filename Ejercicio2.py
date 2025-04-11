class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f"({self.x}, {self.y})"

    def opuesto(self):
        return Punto(-self.x, -self.y)

    def distancia_al_origen(self):
        """Devuelve la distancia del punto al origen (0,0)"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def mover(self, dx, dy):
        """Mueve el punto en el plano una cantidad dx en X y dy en Y"""
        self.x += dx
        self.y += dy
