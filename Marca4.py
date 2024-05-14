class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def saludar(self):
        print("Hola, soy un", self.especie, "y me llamo", self.nombre)

    def despedir(self):
        print("Adiós, soy un", self.especie, "y me llamo", self.nombre)


# Ejemplo de uso
leon = Animal("León", "Felino")
leon.saludar()
leon.despedir()
print(leon.nombre)
print(leon.especie)