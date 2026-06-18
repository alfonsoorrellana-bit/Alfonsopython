# uso y eplicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# print(alumno)
# print(alumno["carrera"])
# # print(alumno)
# # print(alumno["carrera"])

# for key ,value in alumno.items():
#     print(f"{key}= {value} ")
# print("---Cambios de datos---")
# # for dato ,valor in alumno.items():
# #     print(dato, valor )
# alumno["email"]="shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key ,value in alumno.items():
#     print(f"{key}= {value} ")

# productos={
#     1:{"nombre": "Control Inalambrico",
#        "categoria": "Electronica",
#        "precio": 45000},
#     2:{"nombre": "Pilas Recargables",
#        "categoria": "Insumos",
#        "precio": 5000},
#     3:{"nombre": "Pasta Termica",
#        "categoria": "Computacion",
#        "precio": 7000},
# }

# print(productos[1]["nombre"])

# '''
# Crear un diccionario de trabajadores 
# '''

# ##CRUD DE VEGETALES

# vegetales={
#    1:"Maracuyá",2:"Pera",3:"Cebolla",7:"Papa"
# }

# print(list(vegetales.keys())[-1])


# def agregarVegetales():
#    print("-"*20)
#    agregar=input("Ingrese un vegetal: ")
#    nuevoKey=list(vegetales.keys())[-1]
#    vegetales[nuevoKey+1]=agregar
# def mostrarVegetales():
#    print("-"*40)
#    for num, nombre in vegetales.items():
#          print(f"{num}.- {nombre} ")
# def eliminarVegetal():
#    mostrarVegetales()
#    borrar=int(input("Cual vegetal borrará?: "))
#    del vegetales[borrar]
# def actualizarVegetal():
#    mostrarVegetales()
#    act=int(input("Cual vegetal actualizará?: "))
#    vegetales[act]=input("Ingrese nuevo nombre: ")

# def vegetalesMenu():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarVegetales()
#                case 2:
#                   eliminarVegetal()
#                case 3:
#                   actualizarVegetal()
#                case 4:
#                   mostrarVegetales()
#                case 5:
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)

# # vegetalesMenu()

# ##Diccionario con diccionarios
# productosDicc={
#    1:{"nombre": "Maracuyá", "precio": 3000},
#    2:{"nombre": "Pera", "precio": 1500},
#    3:{"nombre": "Cebolla", "precio": 1200}
# }
# carrito=[]
# productosDicc[4]={"nombre": "Piña", "precio": 3500}
# def agregarProducto():
#    print("Cual es el nombre del producto?")
#    nombre = input()
#    print("cual es el precio?")
#    precio = int(input())
#    nuevoKey=list(productosDicc.keys())
#    nuevoKey.sort()
#    productosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "precio": precio}
# def MostrarProducto():
#    for key, producto in productosDicc.items():
#       print(f"{key} .{producto}")
# def eliminarProducto():
#    MostrarProducto()
#    borrar=int(input("Cual Producto borrará?: "))
#    del productosDicc[borrar]
# def actualizarProducto():
#    MostrarProducto()
#    num=int(input("Que producto desea actualizar?: "))
#    if num in productosDicc.keys():
#       nombre=input("Cual es el nombre nuevo?: ")
#       precio=int(input("Cual es el precio nuevo?: "))
#       productosDicc[num]={"nombre": nombre, "precio": precio}
#    else:
#       print("Producto no encontrado")

# def comprar():
#    while True:
#       MostrarProducto()
#       try:
#          con=int (input("que producto desea comprar?: "))
#          if con==0:
#             break
#          if con in productosDicc.keys():
#             carrito.append(productosDicc[con])
#       except Exception as e:
#            print("Error:",e)

# def crearboleta():
#    total=0
#    print("-"*30 "0", "-"*30)
#    print("bienvenido a minimarket")
#    for prod in carrito:
#       print(f"{prod['nombre']}__${prod['precio']}")
#       total+=prod["precio"]
#    print("-"*30 "0", "-"*30)
#    print(f"el total neto es {total} y el iva es {total*0.19} y el total a pagar es {round(total*1.19)}")
#    print("gracias por venir a minimarket ")
#    print("-"*30 "0", "-"*30)
         
# # print(productosDicc[2]["precio"])  # precio de la pera
# # print(productosDicc[3]["nombre"])  # nombre de la cebolla

# # for num, veg in productosDicc.items():
# #     print(f"{num}.- {veg}")

# ##Lista con diccionarios
# productosList=[
#    {"nombre": "Maracuyá", "precio": 3000}, #0
#    {"nombre": "Pera", "precio": 1500},     #1  
#    {"nombre": "Cebolla", "precio": 1200}   #2
# ]

# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #nombre de la naracuya


# carrito={}
# def vegetalesMenuDiccionario():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Comprar")
#          print("6.- Crear Boleta y salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarProducto()
#                case 2:
#                   eliminarProducto()
#                case 3:
#                   actualizarProducto()
#                case 4:
#                   MostrarProducto()
#                case 5:
#                     print("comprar")
#                     comprar()
#                     carritototal=0
#                case 6:
#                   crearboleta()
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:                 
#          print("Error:",e)
# vegetalesMenuDiccionario()

#Cambiar la funcion actualizar para que solo 
# actualice una solo key 
# Ademas, crear un CRUD pero con la lista 
# de diccionarios

agregarpacientes=()
mostarpacientes=()
pacientes=()

def validtemp(t):
    if t>39:
        return True
    else:
        return False
pacientes.append({"nombre": "alan brito", "prevision": "isapre", "temperatura": 39.5, "grave": True})
def agregarusuario():
   nombre=input("ingrese el nombre del paciente nuevo: ")
   while nombre=="" or len(nombre)<9:
      print("nombre no puede ser vacion  ni tener menos de 8 caracter. ")
      nombre=input("ingrese el nombre del paciente nuevo: ")
   prevision=input("ingrese la prevision del paciente nuevo (fonasa, isapre, fodesa): ")
   while prevision.lower() not in 
   temperatura=float(input("ingrese la temperatura del paciente nuevo: "))
   pacientes.append({"nombre": nombre, "prevision": prevision, "temperatura": temperatura, "grave": validtemp(temperatura)})
   print(pacientes)

   while True:
      try:
         print("1.- agregar pacientes ")
         print("2.- quitar pacientes ")
         print("3.- tomar temperatura ")
         print("4.- cobrar a pacientes ")
         print("5.- mostrar pacientes ")
         print("9.- salir")
         op=int(input("Seleccione una opcion: "))
         match op:
            case 1:
               agregarpacientes()
            case 2:
               mostarpacientes()
               eliminar=int(input("que pacientes desea eliminar?: "))
               pacientes.pop(eliminar-1)
            case 3:
                 print("")
            case 4:
                 msotrarpacientes()
                 cobrar=int(input("a quien la va a cobrar?: "))
                 if pacientes[cobrar-1]["prevision"]

               
         
         
         
         

      except Exception as e:
         print("Error:", e)
   




pacientes.append({"nombre": "Alan Brito", "prevision": "Isapre", 
   "temperatura":39.6, "grave": True})



def validarEstado(tempe):
   if tempe>39:
       return True 
   else:
       return False
def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in pacientes:
            print(f"{c} .- {p}")
            c+=1
def agregarPaciente():
    nombre=input("Ingrese nombre: ")
    prevision=input("Ingrese prevision: ")
    temp=float(input("Ingrese temp: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
                "temperatura":temp, "grave": validarEstado(temp)})
    print("Paciente agregado al listado")
def eliminarPaciente():
    mostrarPacientes()
    paci=int(input("Que paciente se vá?: "))
    pacientes.pop(paci-1)
    print("Paciente eliminado.")
def tomarTemp():
    mostrarPacientes()
    paciente=int(input ("A que paciente le tomamos temperatura?: "))
    tomarTemp=float(input("ingrese su temperatura: "))
    pacientes[paciente-1]["temperatura"]=tomarTemp
    pacientes[paciente-1]["grave"]=validarEstado(tomarTemp)
def cobrarAtencion():
    mostrarPacientes()
    pa=int(input("¿que paciente va a pagar?: "))
    if -1<cobrar<len(pacientes):
        print("paciente no enontrado")


      
    if pacientes[pa-1]["prevision"].lower()=="fonasa":
        pagar=25000*0.46
    elif pacientes[pa-1]["prevision"].lower()=="isapre":
        pagar=25000*0.73
    elif pacientes[pa-1]["prevision"].lower()=="fodesa":
        pagar=25000*0.875
    else:
        print("prevision incorrecta")
    print("Su total a pagar es: ", pagar)
while True:
    try:
        print("1.- Ingresar paciente")
        print("2.- Quitar paciente")
        print("3.- Tomar Temperatura")
        print("4.- Cobra atencion")
        print("5.- Mostrar Pacientes")
        print("9.- Salir")
        op=int(input("Ingrese una opcion: "))
        match op:
            case 1:
                agregarPaciente()
            case 2:
                eliminarPaciente()
            case 3:
                tomarTemp()
            case 4:
                cobrarAtencion()
            case 5:
                mostrarPacientes()
            case 9:
                print("Saliendo")
                break
            case _:
                print("Opción inválida")
    except Exception as e:
        print("Error:" , e)