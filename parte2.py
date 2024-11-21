def descuento(precio, porcentaje=10):       
    precioFinal = precio-(precio*(porcentaje/100))
    return precioFinal
   
precio = float(input("Ingrese el precio del producto: "))
porcentaje = float(input("Ingrese porcentaje de descuento: "))
print(f"El precio final aplicado el descuento es {descuento(precio, porcentaje)}")