# RETO_6

1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

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

if __name__ == "__main__":
    a = float(input("Radio esfera "))#se pide el radio de la esfera
    b = float(input("Radio cono "))#se pide el radio del cono
    c = float(input("Altura cono "))#se pide la altura del cono
    cirVandAr = cirVandAr(a) #llaman las funciones
    ConoVandAr = ConoVandAr(b,c)
    print("El volumen en cm3 y Area de la esfera en cm2 es ",cirVandAr)
    print("El volumen en cm3 y Area del cono en cm2 es ",ConoVandAr)

```

2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*


```python
#Una función matemática para calcular el área y el perimetro.
#se importa de las librerias pi
from math import pi

def cirArandPer(r:float): 
    A = pi*r**2
    P = 2*pi*r
    return A,P

def RectArandPer(B:float,A:float):
    Ar = B*A
    P = 2*(B+A)
    return Ar,P

if __name__ == "__main__":
    a = float(input("Radio del circulo "))#se pide el radio del circulo
    b = float(input("Base del rectangulo "))#se pide la base del rectangulo
    c = float(input("Altura del rectangulo "))#se pide la altura del rectangulo
    cirArandPer = cirArandPer(a) #llaman las funciones
    RectArandPer = RectArandPer(b,c)
    print("El Area en cm2 y Perimetro en cm del circulo es ",cirArandPer)
    print("El Area en cm2 y Perimetro en cm del rectangulo es ",RectArandPer)

```
