import os

os.system("cls")

#Guardar tipo-patente-marca-precio-multas(monto y fecha)-fecha de registro del vehiculo-nombre del dueño
#marca debe tener entre 2 a 15 caracteres y precio mayor o igual a 5 millones


#opcion 1 - Grabar/Agregar
def agregar_auto():
    #insertar patente(xx-xx-11)
    while True:
        patente = input("Ingrese Patente Del Vehiculo con el siguiente formato[XX-XX-11]: ")
        if len(patente.lower()) == 8:
            print("Patente Con Formato Valido")
            break
        print("Patente Invalida, Ingresela Con El Formato Correcto[XX-XX-11]")

    #insertar nombre del dueño
    nombre = input("Ingrese Su Nombre y Apellido: ")
    
    #insertar tipo(si es Auto Comun-Camion-Camioneta-Moto)
    while True:
        tipo = input("Ingrese tipo Vehiculo[Auto-Camioneta-Camion-Moto]: ")
        if tipo.lower() in ['auto','camioneta','camion','moto']:
            break
        print("Tipo Ingresado Invalido, Ingresar uno De los mostrados en pantalla...")
    #insertar marca
    while True:
        marca = input("Ingrese Marca Del Vehiculo: ")
        if len(marca) >= 2 and len(marca) <= 15:
            print("Marca Valida")
            break
        print("Marca Invalida, Solo permitido de 2 a 15 caracteres...")

    #insertar precio
    while True:
        precio = int(input("Ingrese El Precio Del Vehiculo[Debe ser Mayor o igual a 5000000]: "))
        if precio >= 5000000:
            print("Precio Valido...")
            break
        print("Precio Invalido, Debe Ser una cifra superior a 5 millones y sin puntos ni coma...")

    #insertar multas #if para preguntar si posee multas o no
    p_multas = input("¿El Vehiculo Posee Multas(Si/No): ")
    if p_multas.lower() == "si":
        while True:
            monto_m = int(input("Ingrese Monto De La Multa[sin puntos ni coma]: "))
            if monto_m >= 1:
                print("Monto Valido")
            print("Monto Invalido, Por favor Ingrese Un Valor De Acuerdo Al Formato Mostrado...")
            fecha_m = input("Ingresar Fecha De La Multa[Formato EJ: 10-01-2023]: ")
            if len(fecha_m) == 10:
                print("Fecha Con Formato Valido...")
                break
            print("Fecha Con Formato Invalido, Favor De Ingresarla Con El Formato mostrado")
    #insertar fecha de registro del auto
    while True:
        fecha_registro = input("Ingresar Fecha Del Vehiculo[Formato EJ: 10-01-2023]: ")
        if len(fecha_registro) == 10:
            print("Fecha Con Formato Valido...")
            break
        print("Fecha Con Formato Invalido, Favor De Ingresarla Con El Formato mostrado")
    #Agregar a la lista
    registro = [patente, nombre, marca, precio, monto_m, fecha_m, fecha_registro]
    autos.append(registro)
    return autos


#opcion 2 buscar
def buscar_por_patente():
    patente_buscar = input("ingrese La Patente Que Desea Buscar[Formato XX-XX-11]:")
    for au in autos:
        if au[0] == patente_buscar:
            return au
    return None

autos = [
        []
        ]

while True:
    print("Menu Auto Seguro")
    print("1.-Grabar/Agregar Un Vehiculo")
    print("2.-Buscar por patente")
    print("3.-Imprimir Certificado")
    print("4.-Salir")

    try:
        op = int(input("ingresar una opcion del 1 al 4:"))
    except:
        print("Opcion Invalida, ingresar solo numero entre 1 y 4")
        op = 0
    if op == 1:
        print("Selecciono Grabar/Agregar Un Vehiculo...")
        lista_agregar =agregar_auto()
        print(lista_agregar)
    if op == 2:
        print("Selecciono Buscar por patente...")
        auto_encontrado = None

        while auto_encontrado is None:
            auto_encontrado = buscar_por_patente()
            if auto_encontrado is None:
                print("La Patente Ingresada no existe...")
        patente = auto_encontrado[0]
        nombre = auto_encontrado[1]
        marca = auto_encontrado[2]
        precio = auto_encontrado[3]
        fecha_registro = auto_encontrado[6]
    print("Informacion")
    print("Patente: ", patente)
    print("Nombre: ", nombre)
    print("Marca: ", marca)
    print("Precio Vehiculo: ",precio)
    print("Fecha Registro: ", fecha_registro)

    if op == 3:
        print("Selecciono Imprimir Certificados...")
    if op == 4:
        print("Gracias Por Usar Nuestros Servicios")
        break
    input("Presione Cualquier Tecla Para Continuar/Salir...")