"uso de while infinito"
c = 18
while True:

    print(c)
#while validacion
vocal=input("ingrese vocal:")
while vocal not in("a","e","i","o","u"):
    if vocal == ".":
        break
    vocal=input("vocal:")
    print("su vocal o punto es:{}".format(vocal))