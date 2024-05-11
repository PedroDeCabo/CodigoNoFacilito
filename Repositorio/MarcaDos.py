class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Velocidad: {self.velocidad} km/h")

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Acelerar el coche
mi_coche.acelerar(20)

# Mostrar la información del coche
mi_coche.mostrar_informacion()

# Frenar el coche
mi_coche.frenar(10)

# Mostrar la información actualizada del coche
mi_coche.mostrar_informacion()