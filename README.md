# RETO_6
#punto1: Dado la figura de la imagen, desarrolle:

1:Una función matemática para calcular el volumen y el área superficial.

2:Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

3:Revise como utilizar el valor de pi usando import math y math.pi.

```python
#Una función matemática para calcular el volumen y el área superficial
from math import sqrt #se importa de  las librerias la raiz cuadrada y pi
from math import pi

def cirVandAr(r:float):
    V = (4/3)*pi*r**3 
    A = 4*pi*(r*2)**2
    return V,A

def ConoVandAr(r:float,h:float):
    V = 1/3*h*pi*r**2
    g = sqrt((r**2)+(h**2))
    A = pi*r*(g+r)
    return V,A
    
a = float(input("Radio esfera "))#se pide el radio de la esfera
b = float(input("Radio cono "))#se pide el radio del cono
c = float(input("Altura cono"))#se pide la altura del cono
cirVandAr = cirVandAr(a) #llaman las funciones
ConoVandAr = ConoVandAr(b,c)
print("El volumen en cm3 y Area de la esfera en cm2 es ",cirVandAr)
print("El volumen en cm3 y Area del cono en cm2 es ",ConoVandAr)

```
