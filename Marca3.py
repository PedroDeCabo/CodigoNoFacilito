def Saludar(Nombre):
    print("Hola", Nombre, ",Encantado de conocerte.")
def Despedir(Nombre):
    print("Ahora, vete a tomar por culo:", Nombre, ".")
Nombre = input("Digame su nombre: ")
Saludar(Nombre)
Despedir(Nombre)

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