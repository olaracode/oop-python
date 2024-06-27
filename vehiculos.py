"""
Vehiculos Motorizados:
---- Modelo
---- Marca
---- Motor

- Herencia
Autos/Carros -> VehiculoMotorizado, cantidad_personas
Lanchas/Botes -> VehiculoMotorizado, pies_largo, pies_ancho 
Motos -> VehiculoMotorizado, tipo()
"""

class Vehiculo:
    def __init__(self, modelo, marca, motor):
        self.model = modelo
        self.marca = marca
        self.motor = motor

    def arrancar(self):
        print("Ruidos de motor")
    
    def retroceder(self):
        print("Ruidos de motor retrocediendo")

# class NombreObjetoHijo(NombreObjetoPadre): heredas
class Auto(Vehiculo):
    def __init__(self, modelo, marca, motor, cantidad_personas):
        # super().__init__()
        super().__init__(modelo, marca, motor)
        self.cantidad_personas = cantidad_personas

class Lancha(Vehiculo):
    def __init__(self, modelo, marca, motor, pies_largo, pies_ancho):
        super().__init__(modelo, marca, motor)
        self.pies_largo = pies_largo
        self.pies_ancho = pies_ancho
    
    def soltar_anclas(self):
        print("Suenan anclas")

corola = Auto("Corolla", "Toyota", "2l", 5)

lancha_miscelanea = Lancha("Yamaha", "Lancha", "Yamaha1", 10, 5)