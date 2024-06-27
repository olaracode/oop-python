"""
Tienda de departamentos
"""
# Tienda


# Producto: marca / precio / cantidad
# Tecnologicos: ram / procesador / tamano pantalla
# Ropa: talla(e) / material
# Hogar:  ancho / alto / peso

class Producto:
    def __init__(self, marca, precio, cantidad):
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad
    
    def get_price(self):
        return self.precio
    
    def get_total_price(self):
        return self.precio * self.cantidad
    
    def restar_cantidad(self, cantidad_a_restar):
        self.cantidad -= cantidad_a_restar
    
    def get_datos(self):
        return {
            "marca": self.marca,
            "precio": self.precio,
            "cantidad": self.cantidad
        }
    
    def __repr__(self):
        return f"Producto: {self.marca} ${self.precio}"


class ProductoTecnologico(Producto):
    def __init__(self, marca, precio, cantidad, ram, procesador, pantalla):
        super().__init__(marca, precio, cantidad)
        self.ram = ram
        self.procesador = procesador
        self.pantalla = pantalla

class ProductoRopa(Producto):
    def __init__(self, marca, precio, cantidad, talla, material):
        super().__init__(marca, precio, cantidad)
        self.talla = talla
        self.material = material

class ProductoHogar(Producto):
    def __init__(self, marca, precio, cantidad, ancho, alto, peso):
        super().__init__(marca, precio, cantidad)
        self.ancho = ancho
        self.alto = alto
        self.peso = peso

telefono = ProductoTecnologico("Samsung", 300, 10, 3, 4, 8.6)
producto_hogar = ProductoHogar("Colchon", 500, 100, 100, 10, 20)
converse = ProductoRopa("Converse", 200, 10, 40, "Tela")

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
        self.ganancias = 0
    
    def agregar_producto(self):
        print("Agregue un produto a la tienda -------------------")
        product_type = int(input("1. Hogar, 2. Tecnologico, 3. Ropa: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))

        if product_type == 1:
            ancho = int(input("Introducir ancho: "))
            alto = int(input("Introducir alto: "))
            peso = int(input("Introducir peso: "))
            self.agregar_a_inventario(ProductoHogar(nombre, precio, cantidad, ancho, alto, peso))
        elif product_type == 2:
            ram = input("Introducir ram: ")
            procesador = input("Introducir procesador: ")
            pantalla = input("Introducir pantalla")
            self.agregar_a_inventario(ProductoTecnologico(nombre, precio, cantidad, ram, procesador, pantalla))
        elif product_type == 3:
            talla = input("Introducir talla: ")
            material = input("Introducir material: ")
            self.agregar_a_inventario(ProductoRopa(nombre, precio, cantidad, talla, material))
        else:
            print("Tipo no valido :(")
        print("-" * 20, "Producto agregado")
        continuar = input("Agregar otro producto? Y/N")
        if continuar == "y":
            self.agregar_producto()
        
    def agregar_a_inventario(self, producto):
        self.inventario.append(producto)
    
    def calcular_precio_inventario(self):
        total = 0
        for product in self.inventario:
            total += product.get_total_price()
        return total
    

four_geeks = Tienda("4geeks")
four_geeks.agregar_producto()
print(four_geeks.inventario)
