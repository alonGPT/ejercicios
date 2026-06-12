boleta =[]
opcion=""

while opcion != 4:
    print("-----MENU-----")
    print("2.Mostrar productos")
    print("1.agregar producto")
    print("3.actualizar un producto.")
    print("4.eliminar un producto")
    print("5.salir")
    opcion =input("escoge una opcion: ")

    if opcion=="1":
        def agregar_producto(nombre, precio):
         producto = {"nombre": nombre, "precio": precio}
         boleta.append(producto)
         print(f"Producto '{nombre}' agregado correctamente.")
        



def calcular_total():
    total =0
    for producto in boleta:
        total=total + producto ["precio"]
    return total    



def mostrar_boleta():
    if len(boleta) == 0:
        print("la boleta esta vacia")
    else:
        print("----BOLETA----")    
        for producto in boleta:
            print (f" {producto['nombre']} -   ${producto['precio']}")
        print(f"total:  ${calcular_total()}")
        print("--------------------\n")



def actualizar_precio(nombre, nuevo_precio):
    for producto in boleta:
        if producto["nombre"] == nombre:
            producto["precio"] = nuevo_precio
            print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
            return
    print(f"Producto '{nombre}' no encontrado.")

actualizar_precio("Leche", 1350)



def eliminar_producto(nombre):
    for producto in boleta:
        if producto["nombre"] == nombre:
            boleta.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

eliminar_producto("Pan")



agregar_producto("galleta", 1500)
agregar_producto("bebida", 1700)
agregar_producto("leche", 1200)
agregar_producto("pan", 950)
print(boleta)


actualizar_precio ("galleta", 990)

eliminar_producto("pan")

mostrar_boleta()
