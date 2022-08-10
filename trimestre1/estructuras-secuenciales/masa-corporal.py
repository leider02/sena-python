# pedir al usuario el peso
pesoKG = float(input("ingrese su peso en kg: "))
# pedir al usuario la estatura
estatura2 = float(input("ingrese su estatura: "))
# calcular masa corporal
masa_corporal = pesoKG / (estatura2 * estatura2)
# imprimir 
print("su masa corporal es: ", masa_corporal)