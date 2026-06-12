print("welcome a mi calculadora")
print("para salir solo escribes la palabra salir")
print("las operaciones que realizamos son suma, resta ,multi y div")


resultado = ""
while True: 
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingresa operacion") 
    if op.lower() == "salir":
        break
    n2 = input("ingresa el otro numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() =="suma":
       resultado += n2
    elif op.lower() =="resta":
       resultado -= n2
    elif op.lower() =="multi":
       resultado *= n2
    elif op.lower() =="div":
       resultado /= n2
    else:
       print("operacion no vailda")
       break

    print(resultado)

print(f"el resultado es {resultado}.") 

#se realizo una calculadora con algunas especificaciones como de sumar o restar el valor final del resultado