# hacer una lista de 3 nombres y otra de 3 apellidos
# mostrar las listas como si fueran nombre
# vale decir, diego robles, adolfo hinako, luis mussolini.

# nombres = ["diego", "adolfo", "luis"]
# apellidos = ["robles", "hinako", "mussolini"]

# for n in range(len(nombres)):
#     print(nombres[n], apellidos[n])

# from unittest import case
# juguetes = ["yo-yo", "pelota", "muñeca"]
# def mostrar():
#      c=1
#      for j in juguetes:
#           print(c,".-",j)  
#           c+=1
#      print("-"*30)
# def actualizar ():
#         mostrar()
#         print("que juguete desea actualizar?")
#         actualizar=int(input())
#         nuevojuguete=input("ingrese el nuevo juguete: ")
#         juguetes[actualizar-1]=nuevojuguete
# def eliminar():
#     mostrar()
#     eliminar=int(input("que juguete desiaria eliminar"))
#     juguetes.pop(eliminar-1)
#     print("juguete eliminado")

# while True:
#     try:
#         print("1.- agregar juguete")
#         print("2.- eliminar juguete")
#         print("3.- actualizar juguete")
#         print("4.- mostrar juguete")
#         print("5.- salir")
#         op=int(input("ingrese una opcion: "))
#         match op:
#            case 1:
#                 ju=input("agregue un juguete: ")
#                 juguetes.append(ju)
#            case 2:
#                 mostrar()
#            case 3:
#                 actualizar()
#            case 4:
#                 mostrar()
#            case 5:
#                 print("saliendo")
#                 break
#            case _:
#                 print("opcion no valida")

                    

#     except Exception as e:
#         print("error: ",e)



#ACTIVIDAD 3.3.3

numeros=input("ingrese numeros enteros separados por espacio:")

listanumeros=numeros.split()
listanumerosint=[]
pares=[]
impares=[]
for n in listanumeros:
    listanumerosint.append(int(n))
    print(n)
for hh in listanumerosint:
    if hh%2==0:
        pares.append(hh)
    else:
        impares.append(hh)
print(f"los numeros pares son: {pares}")
print(f"los numeros impares son: {impares}")


    
    
          

    


