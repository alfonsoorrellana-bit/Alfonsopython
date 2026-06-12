jugadores={
   1:{"nombre": "cristano ronaldo ", "nacido": 1985, "pais": "Portugal"},
   2:{"nombre": "lionel andres messi", "nacido": 1987, "pais": "Argentina"},
   3:{"nombre": "neymar junior", "nacido": 1992, "pais": "Brasil"}
}

carrito=[]
def jugadores():
   print("Cual es el nombre del jugador?")
   nombre = input()
   print("cual es el nacimiento?")
   nacido = int(input())
   nuevoKey=list(jugadores.keys())
   nuevoKey.sort()
   jugadores[nuevoKey[-1]+1]= {"nombre": nombre, "nacido": nacido}
def Mostrarjugadores():
   for key, producto in jugadores.items():
      print(f"{key} .{producto}")
def eliminarProducto():
   Mostrarjugadores()
   borrar=int(input("Cual  Producto borrará?: "))
   del jugadores[borrar]
def actualizarProducto():
   Mostrarjugadores()
   num=int(input("Que jugador desea actualizar?: "))
   if num in jugadores.keys():
      nombre=input("Cual es el nombre nuevo?: ")
      precio=int(input("Cual es el precio nuevo?: "))
      productosDicc[num]={"nombre": nombre, "precio": precio}
   else:
      print("Producto no encontrado")

def comprar():
   while True:
      Mostrarjugadores()
      try:
         con=int (input("que jugador desea comprar?: "))
         if con==0:
            break
         if con in jugadores.keys():
            carrito.append(jugadores[con])
      except Exception as e:
           print("Error:",e)

def crearboleta():
   total=0
   print("-"*30 "0", "-"*30)
   print("bienvenido a los nacimientos de los jugadores ")
   for prod in carrito:
      print(f"{prod['nombre']}__${prod['precio']}")
      total+=prod["precio"]
   print("-"*30 "0", "-"*30)
   print("gracias por venir a los nacimientos de los jugadores ")
   print("-"*30 "0", "-"*30)
         
# print(productosDicc[2]["precio"])  # precio de la pera
# print(productosDicc[3]["nombre"])  # nombre de la cebolla

# for num, veg in productosDicc.items():
#     print(f"{num}.- {veg}")

##Lista con diccionarios
productosList=[
   {"nombre": "Maracuyá", "precio": 3000}, #0
   {"nombre": "Pera", "precio": 1500},     #1  
   {"nombre": "Cebolla", "precio": 1200}   #2
]

print(productosList[2]["precio"]) #precio de la cebolla
print(productosList[0]["nombre"]) #nombre de la naracuya


carrito={}
def vegetalesMenuDiccionario():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Comprar")
         print("6.- Crear Boleta y salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarProducto()
               case 2:
                  eliminarProducto()
               case 3:
                  actualizarProducto()
               case 4:
                  MostrarProducto()
               case 5:
                    print("comprar")
                    comprar()
                    carritototal=0
               case 6:
                  crearboleta()
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:                 
         print("Error:",e)
vegetalesMenuDiccionario()







productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}
carrito=[]
productosDicc[4]={"nombre": "Piña", "precio": 3500}
def agregarProducto():
   print("Cual es el nombre del producto?")
   nombre = input()
   print("cual es el precio?")
   precio = int(input())
   nuevoKey=list(productosDicc.keys())
   nuevoKey.sort()
   productosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "precio": precio}
def MostrarProducto():
   for key, producto in productosDicc.items():
      print(f"{key} .{producto}")
def eliminarProducto():
   MostrarProducto()
   borrar=int(input("Cual Producto borrará?: "))
   del productosDicc[borrar]
def actualizarProducto():
   MostrarProducto()
   num=int(input("Que producto desea actualizar?: "))
   if num in productosDicc.keys():
      nombre=input("Cual es el nombre nuevo?: ")
      precio=int(input("Cual es el precio nuevo?: "))
      productosDicc[num]={"nombre": nombre, "precio": precio}
   else:
      print("Producto no encontrado")

def comprar():
   while True:
      MostrarProducto()
      try:
         con=int (input("que producto desea comprar?: "))
         if con==0:
            break
         if con in productosDicc.keys():
            carrito.append(productosDicc[con])
      except Exception as e:
           print("Error:",e)

def crearboleta():
   total=0
   print("-"*30 "0", "-"*30)
   print("bienvenido a minimarket")
   for prod in carrito:
      print(f"{prod['nombre']}__${prod['precio']}")
      total+=prod["precio"]
   print("-"*30 "0", "-"*30)
   print(f"el total neto es {total} y el iva es {total*0.19} y el total a pagar es {round(total*1.19)}")
   print("gracias por venir a minimarket ")
   print("-"*30 "0", "-"*30)
         
# print(productosDicc[2]["precio"])  # precio de la pera
# print(productosDicc[3]["nombre"])  # nombre de la cebolla

# for num, veg in productosDicc.items():
#     print(f"{num}.- {veg}")

##Lista con diccionarios
productosList=[
   {"nombre": "Maracuyá", "precio": 3000}, #0
   {"nombre": "Pera", "precio": 1500},     #1  
   {"nombre": "Cebolla", "precio": 1200}   #2
]

print(productosList[2]["precio"]) #precio de la cebolla
print(productosList[0]["nombre"]) #nombre de la naracuya


carrito={}
def vegetalesMenuDiccionario():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Comprar")
         print("6.- Crear Boleta y salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarProducto()
               case 2:
                  eliminarProducto()
               case 3:
                  actualizarProducto()
               case 4:
                  MostrarProducto()
               case 5:
                    print("comprar")
                    comprar()
                    carritototal=0
               case 6:
                  crearboleta()
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:                 
         print("Error:",e)
vegetalesMenuDiccionario()