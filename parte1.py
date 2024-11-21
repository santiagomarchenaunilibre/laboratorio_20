#Bienvenida
def bienvenida(nombre):
    print(f"Hola! {nombre} bienvenido a este pequeño progrma de Python! :)")

nombre = input("Ingrese su nombre: ")
bienvenida(nombre)

#Area círculo
import math
def area_circulo(radio):
    area = math.pi*radio**2
    return area

radio = float(input("Ingresa radio del círculo para calcular su área: "))
print("El área del círculo es ",area_circulo(radio))



