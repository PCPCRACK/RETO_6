# RETO_7
#punto1: Una función matemática para calcular el volumen y el área superficial

```python
pi=3.14159265359
def V(r:float):
    return (4/3)*pi*r**3

if __name__ == "__main__":
    R=float(input("radio de la Esfera"))
    v = V(R)
    print("el resultado sale en la unidad de medida que se ingreso")
    print("el Volumen de la esfera es",v)
```
