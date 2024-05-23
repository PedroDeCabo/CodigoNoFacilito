class TemperatureConverter:
    @staticmethod
    def CelsiusToFahrenheit(tempCelsius):
        celsius = float(tempCelsius)
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit

    @staticmethod
    def FahrenheitToCelsius(tempFahrenheit):
        fahrenheit = float(tempFahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    @staticmethod
    def ConvertidorMedidas(MedidasCentimetros):
        Centimetros = float(MedidasCentimetros)
        Pulgadas = Centimetros / 2.54
        return Pulgadas

    @staticmethod
    def ConvertidorPulgadas(MedidasPulgadas):
        Pulgadas = float(MedidasPulgadas)
        Centimetros = Pulgadas * 2.54
        return Centimetros


while True:
    selection = input("Enter C)elsius to Fahrenheit or F)arenheit to Celsius or Enter E)centimetros to pulgadas or P)ulgadas to centimetros or Q)uit:")
    farenheit, celsius = 0, 0
    Centimetros, Pulgadas = 0, 0

    if selection.lower() == "c":
        tempCelsius = input("Please enter the Celsius temperature: ")
        farenheit = TemperatureConverter.CelsiusToFahrenheit(tempCelsius)
        print(f"Temperature in Fahrenheit: {farenheit:.2f}")

    elif selection.lower() == "f":
        tempFahrenheit = input("Please enter the Fahrenheit temperature: ")
        celsius = TemperatureConverter.FahrenheitToCelsius(tempFahrenheit)
        print(f"Temperature in Celsius: {celsius:.2f}")

    elif selection.lower() == "e":
        MedidasCentimetros = input("Por favor introduce la medida en centimetros: ")
        Centimetros = TemperatureConverter.ConvertidorMedidas(MedidasCentimetros)
        print(f"La medida en pulgadas es: {Centimetros:.2f}")

    elif selection.lower() == "p":
        MedidasPulgadas = input("Por favor introduce la medida en pulgadas: ")
        Pulgadas = TemperatureConverter.ConvertidorPulgadas(MedidasPulgadas)
        print(f"La medida en centimetros es: {Pulgadas:.2f}")

    elif selection.lower() == "q":
        break

    else:
        print("Please try again.")
