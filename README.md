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

3.Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.


```python
#una función que calcule la cantidad de carne de aves en kilos 

def suma(N:float,M:float,K:float):
    return (N*6)+(M*7)+(K*1)#multiplica y suma todo
    

if __name__ == "__main__":
    N = float(input("N° de gallinas? "))#pregunta cuantos de cada uno
    M = float(input("N° de gallos? "))
    K = float(input("N° de pollitos? "))
    suma = suma(N,M,K)#llama la funcion
    print("La cantidad de carne de aves en kilos es ",suma)
```

5.Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
#Hacer un programa que me diga las vueltas (o lo que quedo debiendo)

def suma(N:float,M:float,K:float,B:float):
    return B-((N*300)+(M*3300)+(K*350)) #multiplica y suma y luego resta el billete
    

if __name__ == "__main__":
    P = float(input("N° de Panes? ")) #pregunta cuantos de cada uno
    M = float(input("N° de Bolsas de leche? "))
    H = float(input("N° de Huevos ? "))
    B = float(input("Valor billete "))
    suma = suma(P,M,H,B) #llama la funcion
    if suma>0: #si suma es mayor a cero
        print("Las vueltas son ",suma)
    else :
        print("Quedaste debiendo ",suma)
```

5.Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```python
def valor_prestamo(p, i, n):
    """
    Esta función calcula el valor de un préstamo utilizando interés compuesto.
    
    p: el monto del préstamo inicial
    i: la tasa de interés anual (como fracción, por ejemplo, 0.05 para una tasa del 5%)
    n: el número de meses para los cuales se calcula el interés
    
    return: el valor del préstamo después de n meses con interés compuesto
    """
    r = (1 + i/12)**n # cálculo del factor de interés compuesto
    return p*r # cálculo del valor final del préstamo

if __name__ == "__main__":
    prestamo_inicial = float(input("Prestamo inicial "))
    tasa_interes_anual = float(input("Tasa de interes "))
    num_meses = float(input("Tiempo en meses "))
    valor_final = valor_prestamo(prestamo_inicial, tasa_interes_anual, num_meses)
    print("El valor final del préstamo es: ", valor_final)
```

6.El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
def Num_contagios(x:float,a:float):
    D = 0
    while D<a: #mientras D sea menor que los dias
        x *= 2 #se miltiplica X por 2
        D += 1 #se suma uno a D hasta que sea igual a A
    return x

if __name__ == "__main__":
    x = float(input("numero de contagiados ")) #pregunta N° de contagiados y de dias
    A = float(input("numero de Dias "))
    N = Num_contagios(x,A)#llama la funcion
    print("El numero total de contagiados es ",N, " en un total de ",A," dias" )
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python
import math

# Función para calcular el promedio de los números
def promedio(nums):
    return sum(nums) / len(nums)

# Función para calcular la mediana de los números
def mediana(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    else:
        return sorted_nums[n//2]

# Función para calcular el promedio multiplicativo de los números
def promedio_multiplicativo(nums):
    producto = 1
    for num in nums:
        producto *= num
    return producto ** (1/len(nums))

# Pedir 5 números al usuario
nums = []
for i in range(5):
    nums.append(float(input("Ingrese un número real: ")))

# Calcular y mostrar los resultados
print("El promedio es:", promedio(nums))
print("La mediana es:", mediana(nums))
print("El promedio multiplicativo es:", promedio_multiplicativo(nums))
print("Los números ordenados de forma ascendente son:", sorted(nums))
print("Los números ordenados de forma descendente son:", sorted(nums, reverse=True))
print("El mayor número elevado al menor número es:", max(nums) ** min(nums))
print("La raíz cúbica del menor número es:", math.pow(min(nums), 1/3))
```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

9. Consultar qué es y cómo funciona *pip* en python.

10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.

