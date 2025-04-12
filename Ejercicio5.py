class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor  # Será un objeto de la clase Persona
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar  # Tupla con ciudad y país
        self.fecha_edicion = fecha_edicion

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_isbn(self):
        return self.isbn

    def get_paginas(self):
        return self.paginas

    def get_edicion(self):
        return self.edicion

    def get_editorial(self):
        return self.editorial

    def get_lugar(self):
        return self.lugar

    def get_fecha_edicion(self):
        return self.fecha_edicion

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_paginas(self, paginas):
        self.paginas = paginas

    def set_edicion(self, edicion):
        self.edicion = edicion

    def set_editorial(self, editorial):
        self.editorial = editorial

    def set_lugar(self, lugar):
        self.lugar = lugar

    def set_fecha_edicion(self, fecha_edicion):
        self.fecha_edicion = fecha_edicion

    def leer_informacion(self):
        return f"{self.titulo}, {self.autor.get_nombre()} {self.autor.get_apellido()}, ISBN: {self.isbn}"

    def mostrar_informacion(self):
        ciudad, pais = self.lugar
        return f"""
        Título: {self.titulo} {self.edicion}
        Autor: {self.autor.get_apellido()}, {self.autor.get_nombre()}
        ISBN: {self.isbn}
        {self.editorial}, {ciudad} ({pais})
        {self.fecha_edicion}
        {self.paginas} páginas
        """

# ==== PRUEBAS ====

if __name__ == "__main__":
    autor = Persona("Y. Daniel", "Liang")
    libro = Libro(
        "Introduction to Java Programming",
        autor,
        "0-13-031997-X",
        784,
        "3a. edición",
        "Prentice-Hall",
        ("New Jersey", "USA"),
        "viernes 16 de noviembre de 2001"
    )

    print(libro.leer_informacion())  # Muestra una forma resumida
    print(libro.mostrar_informacion())  # Muestra la información completa con el formato solicitado
