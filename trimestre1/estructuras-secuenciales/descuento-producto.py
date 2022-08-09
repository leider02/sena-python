#valor producto
valor_producto = float(input("ingresar valor producto: "))
#descuento 
descuento = 0.35
#valor con descuento
valor_descuento = (valor_producto * descuento)
#valor total
valor_total = (valor_producto - valor_descuento)

print("el valor total a pagar es: " + str(valor_total))