def no_space(texto):                       #se define fn de no espacio para el string
    nuevo_texto = ""                       #para ingresar el nuevo texto
    for char in texto:                     #  fn for"  y secompara texto
        if char != " ":                    # char que es un caracter se dicesi es diferente"!  en espacio
            nuevo_texto += char             #al uevo texto se le suma el char
    return nuevo_texto                      # que retorne en nuevo texto
def reverse(texto):                         # se define texto al reves
    texto_al_reves = ""                      # se asigna un texto
    for char in texto:
        texto_al_reves = char + texto_al_reves       # se concatena ? mira que es diferente a la fn de arriba para que de alrevex
    return texto_al_reves    


def es_palindromo(texto):                        # se define fn palindromo
    texto = no_space(texto)
    texto_al_reves = reverse (texto)
    return texto.lower() == texto_al_reves.lower()   # lower para que  no afecte mayucilas o minusculass


print(es_palindromo("Amo la paloma") ) 
print(es_palindromo("hola eiecer")  )
print(es_palindromo("reConocer")  )


#se desea realizar una funcion donde se diga si es palindromo o no  se trata de explicar paso apaso


        