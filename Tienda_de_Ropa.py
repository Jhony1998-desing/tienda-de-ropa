class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_informacion(self):
        return f"{self.nombre} - ${self.precio}"

class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_informacion(self):
        return f"{self.nombre} (Talla: {self.talla}) - ${self.precio}"

class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def mostrar_informacion(self):
        return f"{self.nombre} (Talla: {self.talla}) - ${self.precio}"

class Zapato(Producto):
    def __init__(self, nombre, precio, numero):
        super().__init__(nombre, precio)
        self.numero = numero

    def mostrar_informacion(self):
        return f"{self.nombre} (Número: {self.numero}) - ${self.precio}"

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def comprar_producto(self, producto_nombre):
        for producto in self.productos:
            if producto.nombre == producto_nombre:
                print(f"Has comprado {producto.mostrar_informacion()}")
                self.productos.remove(producto)
                return
        print("Producto no encontrado")

def mostrar_menu():
    print("\nMenú de la Tienda")
    print("1. Ver inventario")
    print("2. Cargar pedido")
    print("3. Comprar producto")
    print("4. Salir")

def cargar_pedido(tienda):
    while True:
        print("\nCargar Pedido:")
        print("1. Camisa")
        print("2. Pantalón")
        print("3. Zapato")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            talla = input("Talla: ")
            tienda.agregar_producto(Camisa(nombre, precio, talla))
            print(f"Producto {nombre} añadido.")
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            talla = input("Talla: ")
            tienda.agregar_producto(Pantalon(nombre, precio, talla))
            print(f"Producto {nombre} añadido.")
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            numero = int(input("Número: "))
            tienda.agregar_producto(Zapato(nombre, precio, numero))
            print(f"Producto {nombre} añadido.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    tienda = Tienda()
    tienda.agregar_producto(Camisa("Camisa azul", 50, "M"))
    tienda.agregar_producto(Pantalon("Pantalón negro", 60, "32"))
    tienda.agregar_producto(Zapato("Zapato deportivo", 80, 42))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nInventario de productos:")
            tienda.mostrar_productos()
        elif opcion == "2":
            cargar_pedido(tienda)
        elif opcion == "3":
            producto_nombre = input("Ingrese el nombre del producto a comprar: ")
            tienda.comprar_producto(producto_nombre)
        elif opcion == "4":
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

