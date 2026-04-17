# titulo="Clima actual" #tipo string
# temp=18.6 #float
# diaDelMes=16 #int
# mes=4 #int
# llueve=True

# print(f"{titulo}")
# print(f"Fecha de hoy: {diaDelMes}-{mes}")
# print(f"Tempreatura actual {temp} grados")

# if llueve :
#     print("Saco el paraguas")
# else:
#     print("No saco el paraguas")

# num=10

# 7>num --->False
# "blue"=="blue"--->True

# num=int(input("Ingrese un numero: "))

# for i in range(num):

#     print(f"{i+1} Hola Camello")

nombre=input("Ingrese su nombre: ")
vocales=0
cons=0
for i in nombre:
    print(i)
    # vocales=vocales+1
    if i in "aeiou":
        vocales+=1
    elif i==" ":
        print()
    else:
        cons+=1
print(f"La cant de vocales es {vocales}")
print(f"La cant de consonantes es {cons}")


