x=int(input("ingresa un valor entero:"))
if x < 0:
    x = 0
    print("es un valor negativo se cambia a cero")
elif x == 0:
     print("cero es igual 0")
elif x == 1:
     print("uno")
else:

     print("ninguna opcion")

print("ok") if type(x) == int else print("-")