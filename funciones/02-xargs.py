def suma(*numeros):   #parametros en plural, no olvidad*qeu sea iterable
    resultado = 0
    for numero in numeros:
        resultado += numero  #que al resultado se sumel anterios
    print(resultado)    #ojo con la IDENTACIO(espacip entre lineas)


suma(2, 8, 9)
suma(5, 5)    
suma(2, 8, 65, 1)
    
 