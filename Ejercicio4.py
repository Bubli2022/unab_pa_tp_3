class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

# ==== PRUEBAS ====

if __name__ == "__main__":
    cancion = Cancion("Bohemian Rhapsody", "Queen")
    
    # Obtener título y autor
    print(f"Título: {cancion.get_titulo()}")
    print(f"Autor: {cancion.get_autor()}")
    
    # Modificar título y autor
    cancion.set_titulo("Imagine")
    cancion.set_autor("John Lennon")
    
    # Obtener los nuevos valores
    print(f"Nuevo Título: {cancion.get_titulo()}")
    print(f"Nuevo Autor: {cancion.get_autor()}")
