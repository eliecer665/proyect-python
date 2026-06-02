animal = "   chanCHito feliz   "
print(animal.upper())   #lo convierte en mayusculas la frase
print(animal.lower())  # lo convierte en minuscula
print(animal.capitalize()) 
print(animal.title()) #la orimera letra en mayuscula
print(animal.strip())  #quita los prmeros espacios  y empieza a escribir
print(animal.strip().capitalize())  #quita espacion y escrine normal
print(animal.lstrip())    #quita los primeros espacios 
print(animal.rstrip())     #quita los ultimos espacios
print(animal.find("CH"))
print(animal.find("cH"))    
print( "ito" in animal)   # busca la palabra o letra y devuelve f o v
print( "ito" not in animal)
