# Clases y POO

class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")

class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda

# Implementación del Sistema

def menu():
    inventario = Inventario()
    productos_disponibles = [
        RopaHombre("Camisa de Hombre", 25.00, 50, "M"),
        RopaHombre("Pantalón de Hombre", 30.00, 30, "L"),
        RopaHombre("Chaqueta de Hombre", 55.00, 20, "XL"),
        RopaMujer("Falda de Mujer", 28.00, 15, "S"),
        RopaMujer("Blusa de Mujer", 22.00, 40, "M"),
        RopaMujer("Vestido de Mujer", 45.00, 10, "L"),
        RopaHombre("Zapatos de Hombre", 60.00, 25, "42"),
        RopaMujer("Zapatos de Mujer", 50.00, 20, "38"),
    ]

    while True:
        print("\n1: Ver productos disponibles")
        print("2: Agregar producto al inventario")
        print("3: Ver inventario")
        print("4: Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            for idx, producto in enumerate(productos_disponibles, 1):
                print(f"{idx}. {producto}")
        elif opcion == '2':
            num_producto = int(input("Selecciona el número del producto que deseas agregar: ")) - 1
            if 0 <= num_producto < len(productos_disponibles):
                inventario.agregar_prenda(productos_disponibles[num_producto])
                print(f"Producto {productos_disponibles[num_producto].nombre} añadido al inventario.")
            else:
                print("Producto no válido.")
        elif opcion == '3':
            inventario.mostrar_inventario()
        elif opcion == '4':
            print("Gracias por usar el sistema de compra de ropa. ¡Hasta luego!")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
