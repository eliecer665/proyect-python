n1 = input("ingresa tu primer numero") # con inptu llama o pide que ingrese datos
n2 = input("ingresa el segundo numero")

n1 = int(n1)
n2 = int(n2)


suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
para los numero {n1} y {n2},
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la  multi es {multi}.
el resultado de la  div es {div}.
"""

print(mensaje)
