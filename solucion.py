# while True:
#     try:
#         cantP=int(input{"cuantos pasajes va a vender"})
#         break
#     except Exception as e:
#         print("solo valores enteros. error: ", e)
# totalingresos=0
# for i in range (cantP):
#     while True:
#         try:
#             pasaje=int(input{f"ingrese el precio del pasaje {i+1}"})
#             totalingresos=pasaje
#             break
#         except ValueError as e:
#             print("solo valores enteros. error: ", e)
# print(f"el total de los pasajes es{totalingresos}")


 


while True:
    try:
        cantP = int(input("cuantos bultos son"))
        break
    except ValueError as e:
        print("solo valores enteros. error:", e)
bilvianos = 0
bnormales = 0
for i in range(cantP):
    while True:
        try:
            bulto = float(input(f"ingrese el bulto {i+1}: "))
            if bulto <=5:
                bilvianos+=1
            else:
                bnoreales+=1
            break
        except ValueError as e:
            print("solo valores enteros. error:", e)



print(f"bultos livianos: {bilvianos*1000}")
print(f"bultos normales: {bnormales*2000}")