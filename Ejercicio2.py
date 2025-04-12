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

if __name__ == "__main__":
    p1 = Punto(3, 4)
    print("Punto:", p1.impresion())
    print("Eje X:", p1.eje_x())
    print("Eje Y:", p1.eje_y())
    print("Opuesto:", p1.opuesto().impresion())
    print("Distancia al origen:", p1.distancia_origen())
    p1.mover(1, -2)
    print("Punto movido:", p1.impresion())
