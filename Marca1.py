print("Hola mundo")
def sumar(a, b):    
    return a + b
def potencias(a, b):
    return a ** b
print(sumar(2, 2))
print(potencias(2, 2))
class Ejemplo:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, {self.nombre}!")

ejemplo = Ejemplo("Juan")
ejemplo.saludar()