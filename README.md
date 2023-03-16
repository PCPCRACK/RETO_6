# RETO_7
#punto1: Dado la figura de la imagen, desarrolle:

1:Una función matemática para calcular el volumen y el área superficial.

2:Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

3:Revise como utilizar el valor de pi usando import math y math.pi.

```python
#Una función matemática para calcular el volumen y el área superficial
def VandAr(r:float,d:float):
    pi = 3.14159265359
    r = (4/3)*pi*r**3 
    d = 4*pi*d**2
    return r,d
    
a = float(input("Radio "))#se pide el radio de la esfera
b = float(input("diametro "))#se pide el diametro de la esfera
VandAr=VandAr(a,b) #llama la funcion
print("Radio y Diametro de la esfera ",VandAr)
```
