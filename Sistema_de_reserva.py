Usuario = []
Reserva = []
Mes = ["enero" or 1, "febrero" or 2, "marzo" or 3, "abril" or 4, "mayo" or 5, "junio" or 6, "julio" or 7, "agosto" or 8, "septiembre" or 9, "octubre" or 10, "noviembre" or 11, "diciembre" or 12]
Lugares = ["Paris", "Quito", "Rido de janerio", "Buenos Aires"]

def Lugar():
    print("")
    print("*" * 15, "Destinos", "*" * 15)
    for l in Lugares:
        print(l)
    print("*" * 40)

        
def Menu_reserva():
    while True:
     print("")
     print("-" * 15, "Menu", "-" * 15)
     print("1. Registrar usuario")
     print("2. Realizar reserva")
     print("3. Mostrar reserva")
     print("4. Cancelar reserva")
     print("5. Salir del sistema")
     print("")
     opcion = input("Eliga una opcion: ")
     print("-" * 36)
     print("")
     if opcion == "5":
         print("Cerrando el sistema...")
         print("")
         break
     elif opcion == "1":
         Registrar_usuario()
     elif opcion == "2":
         Realizar_reserva()
     elif opcion == "3":
         Mostrar_reserva()
         
def Registrar_usuario():
    print("¿Ha nombre de quien estara la reservar?")
    Name = input()
    if Name in Usuario:
         print("El nombra ya ha sido registrado antes")
    else:
         Usuario.append(Name)
         print("Nombre registrado")

def Realizar_reserva():
    nombre = input("Escriba su nombre y apellido: ")
    if nombre in Usuario:
        Lugar()
        print("")
        Destino = input("Elija su destino: ")
        if Destino in Lugares:
            print("Destino registrado")
            print("")
            fecha_n = int(input("Ingrese el día: "))
            fecha_m = input("Ingrese el mes: ")
            if fecha_m in Mes and fecha_n < 31 and fecha_n != 0:
             print("Fecha registrada")
             registro = {"nombre": nombre, "destino": Destino, "dia": fecha_n, "mes": fecha_m}
             Reserva.append(registro)
             print("")
             print("Viaje reservado con exito!")
            else:
             print("Fecha no valida") 
        else:
            print("Destino no presente")
    else:
        print("Debe registar su nombre y apellido primero")

def Mostrar_reserva():
    if len(Reserva) == 0:
        print("No hay reservas")
    else:
        print("")
        print("/" * 10, "Reservas" "/" * 10) 
        for reserva in Reserva:
            print(f"Nombre: {reserva['nombre']} - Destino: {reserva['destino']} - Dia: {reserva['dia']} Mes: {reserva['mes']}")
    
Menu_reserva()