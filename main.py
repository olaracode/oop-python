"""
Programacion Orientada a Objetos:
Objeto: Es como una plantilla para crear cosas.
Estructuras de datos.
"""

# Para crear un objeto se usa class
# Para nombrar un objeto NombreObjeto(CamelCase)
# Debe poder sumar
# Debe poder restar
# Debe poder multiplicar
# Debe poder dividir
class Calculadora:
    # Algun tipo de estado, un valor que mantenga y modifique
    # Una funcion dentro de un objeto se le llama "metodo"
    def suma(self, a, b):
        return a + b
    
    # (self) -> Self es la instancia actual del objeto
    def resta(self, a, b):
        return a - b
    # pass: pass se utiliza para decirle a python que no de error por un bloque vacio

# Una instancia de mi calculadora
calculadora_simple = Calculadora()
suma_2_2 = Calculadora().suma(2,2) # Sin instanciar
suma_1_2 = calculadora_simple.suma(1,2) # instanciada

# Si tienes un objeto, nada mas el objeto mismo puede modificarse
class Persona:
    # metodo nativo de los objetos
    # inicializacion -> Creacion / Instanciacions
    def __init__(self, name, apellido, edad, nro_documento):
        # valores directamente al objeto
        self.name = name
        self.apellido = apellido
        self.edad = edad
        self.nro_documento = nro_documento

    # Metodos
    def saludar(self):
        print(f"Hola me llamo {self.name} {self.apellido}")
    
    def dar_su_edad(self):
        print(f"Tengo {self.edad} anios")


    def set_data(self, name="", apellido=""):
        if name != "":
            self.name = name
        if apellido != "":
            self.apellido = apellido

    # serialize
    def serialize(self):
        return {
            "name": self.name,
            "apellido": self.apellido,
            "edad": self.edad,
            "documento_identidad": self.nro_documento
        }
    
    # representacion
    # Sirve para sobreescribir
    # como se ve el objeto cuando lo imprimes directamente
    def __repr__(self):
        # "{"name": self.name}"
        return f"ID:{self.nro_documento}"

alexis = Persona("Alexis", "Penia", 24, 11111111)
alexis.saludar()
alexis.dar_su_edad()

jose = Persona("Jose", "Morrone", 25, 222222222)
jose.saludar()
jose.dar_su_edad()

angie = Persona("Angie", "Vanega", 20, 33333333)
angie.saludar()
angie.dar_su_edad()

# Permite modificar los valores desde afuera
angie.set_data(apellido="algo")
angie.set_data(name="angie")
angie.set_data(name="angie", apellido="vanega")
print(angie.apellido)