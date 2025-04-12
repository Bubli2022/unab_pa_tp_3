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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy


class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia):
        self._punto_a.mover(distancia, 0)
        self._punto_b.mover(distancia, 0)

    def mueve_izquierda(self, distancia):
        self._punto_a.mover(-distancia, 0)
        self._punto_b.mover(-distancia, 0)

    def mueve_arriba(self, distancia):
        self._punto_a.mover(0, distancia)
        self._punto_b.mover(0, distancia)

    def mueve_abajo(self, distancia):
        self._punto_a.mover(0, -distancia)
        self._punto_b.mover(0, -distancia)

    def impresion(self):
        return f"Línea: A{self._punto_a.impresion()} - B{self._punto_b.impresion()}"

# ==== PRUEBAS ====

if __name__ == "__main__":
    p1 = Punto(1, 2)
    p2 = Punto(3, 4)
    linea = Linea(p1, p2)
    print(linea.impresion())

    linea.mueve_derecha(2)
    print("Después de mover a la derecha:", linea.impresion())

    linea.mueve_arriba(3)
    print("Después de mover arriba:", linea.impresion())

    linea.mueve_izquierda(1)
    print("Después de mover a la izquierda:", linea.impresion())

    linea.mueve_abajo(2)
    print("Después de mover abajo:", linea.impresion())
