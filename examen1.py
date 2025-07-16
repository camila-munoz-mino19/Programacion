productos = {"8475HD": ["HP",15.6,"8GB", "DD", "1T", "Intel Core i5","Nvidia GTX1050"],
             "2175HD": ["Lenovo",14,"4GB", "SSD", "512GB", "Intel core i5","Nvidia GTX1050"],
             "JjfFHD": ["Asus", 14, "16GB","SSD","256GB","Intel core i7","Nvidia RTX2080Ti"],
             "UWU131HD":[ "Dell", 15.6, "8GB","DD", "1T", "AMD Ryzen 3","Nvidia GTX1050"]}


stock = {"8475HD":[387990,10],
         "2175HD":[327990,4],
         "JjfFHD":[424990,1],
         "UWU131HD":[349990,1]}

def menu():
    print("*** MENU PRINCIPAL***")
    print("-----------------------")
    print("1- Stock marca.")
    print("2-Busqueda por precio")
    print("3-Actualizar precio")
    print("4-Salir")

    opcion = input("hola, porfavor ingresa una de las opciones del menú").strip()
    return opcion

#stock de marca
def stock_marca():
    marca = input("Ingrese la marca que deses ver").lower().strip()
    total = 0 
    for clave in productos:
        if productos [clave][0] == marca:
            total += stock[clave][1]
    print("el total para la marca",marca,"es de:",total,"unidades.")

def busqueda_por_precio ():
    try:
        precio_min = int(input("Ingresa un precio minimo para tu busqueda"))
        precio_max = int(input("Ingresa un precio maximo para tu busqueda"))
        encontrados = []
        for clave in stock:
            precio = stock[clave][0]
            cantidad = stock [clave][1]
            if precio_min <= precio <= precio_max and cantidad > 0:
                encontrados.append(clave)
        if len(encontrados) > 0:
            print("los modelos encontrados:")
            for cod in encontrados:
                print("modelo", cod, "marca", productos [cod][0]).sorted() 
            else:
                print("No hay notbooks en ese rango de precios.")
    except ValueError:
        print("Debe ingresar valores enteros!!")

def actualizar_precio(stock):
    while True:
        try:
            opcion = int(input("¿Qué deseas cambiar? 1) Precio 2) Salir: "))
            if opcion == 1:
                modelo = input("Ingresa el modelo: ").upper()
                if modelo in stock:
                    nuevo = int(input("Ingresa el nuevo precio: "))
                    if nuevo >= 0:
                        stock[modelo][0] = nuevo  # Actualiza el precio
                        print("El precio del modelo" ,modelo, "actualizado es:", nuevo)
                    else:
                        print("El precio debe ser mayor a cero.")
                else:
                    print("Modelo no encontrado.")
            elif opcion == 2:
                print("Saliendo del modo de actualización...")
                break 
                print("La opción seleccionada no es válida.")
        except ValueError:
            print("Solo se debe ingresar números enteros.")



opcion = 0

while true:
    print("*** MENU PRINCIPAL***")
    print("-----------------------")
    print("1- Stock marca.")
    print("2-Busqueda por precio")
    print("3-Actualizar precio")
    print("4-Salir")

    try:
        opcion = input("hola, porfavor ingresa una de las opciones del menú").strip()
        if opcion = 1:
            stock_marca()
        elif opcion = 2:
            busqueda_por_precio()
        elif opcion = 3:
            actualizar_precio()
        elif opcion 4:
            print("Hasta luego")
            break
        else:
            print("opcion ingresada no es valida")
    except ValueError:
        print("Debes ingresar solo numero que sale en el menu")       
                