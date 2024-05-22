import time
class Oficinas:
    def __init__(self, NumeroOficina = 0, LuzLed = False, Nombre = None):
        self.NumeroOficina = NumeroOficina
        self.LuzLed = LuzLed
        self.Nombre = Nombre

Oficina2 = Oficinas(2, True, "Sala de admisiones")

class Empleados:
    def __init__(self, Nombre=None, Fecha=None, Turno=None, Sueldo=0, DiasDeVacaciones=0):
        self.Nombre = Nombre
        self.Fecha = Fecha
        self.turno = Turno
        self.Sueldo = Sueldo
        self.DiasVacaciones = DiasDeVacaciones

Emp0 = Empleados("Juan", "01/01/2020", "Mañana", 1000, 15)
Emp1 = Empleados("Ana", "01/01/2020", "Tarde", 1000, 14)
Emp2 = Empleados("Pedro", "01/01/2020", "Noche", 1000, 7)
Emp3 = Empleados("Maria", "01/01/2020", "Mañana", 1000, 18)

def CalcularVacacionesRestantes(DiasDeVacaciones):  
    VacacionesRestantes = 30 - DiasDeVacaciones
    return VacacionesRestantes

print(CalcularVacacionesRestantes(Emp0.DiasVacaciones))
print(CalcularVacacionesRestantes(Emp1.DiasVacaciones))
print(CalcularVacacionesRestantes(Emp2.DiasVacaciones))
print(CalcularVacacionesRestantes(Emp3.DiasVacaciones))

empleados = [Emp0, Emp1, Emp2, Emp3]

for empleado in empleados:
    print(empleado.Nombre)
    print(empleado.Fecha)
    print(empleado.turno)
    print(empleado.Sueldo)
    print(empleado.DiasVacaciones)
    print(CalcularVacacionesRestantes(empleado.DiasVacaciones))
