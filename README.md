# RETO_7
#punto1: Dado la figura de la imagen, desarrolle:

1:Una función matemática para calcular el volumen y el área superficial.

2:Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

3:Revise como utilizar el valor de pi usando import math y math.pi.

```python
#Una función matemática para calcular el volumen y el área superficial
def VandAr(r:float):
    pi = 3.14159265359
    V = (4/3)*pi*r**3 
    A = 4*pi*(r*2)**2
    return V,A
    
a = float(input("Radio "))#se pide el radio de la esfera
VandAr=VandAr(a) #llama la funcion
print("El volumen y Area de la esfera es ",VandAr)

```
