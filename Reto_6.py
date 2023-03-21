# Función para calcular el promedio de una lista de números
def promedio(nums):
    total = sum(nums)
    return total / len(nums)

# Función para calcular la mediana de una lista de números
def mediana(nums):
    nums = sorted(nums)
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[mid-1] + nums[mid]) / 2
    else:
        return nums[mid]

# Función para calcular el promedio multiplicativo de una lista de números
def promedio_multiplicativo(nums):
    total = 1
    for num in nums:
        total *= num
    return total ** (1/len(nums))

# Función para ordenar una lista de números de forma ascendente
def orden_ascendente(nums):
    return sorted(nums)

# Función para ordenar una lista de números de forma descendente
def orden_descendente(nums):
    return sorted(nums, reverse=True)

# Función para calcular la potencia del mayor número elevado al menor número
def potencia_mayor_menor(nums):
    mayor = max(nums)
    menor = min(nums)
    return mayor ** menor

# Función para calcular la raíz cúbica del menor número
def raiz_cubica_menor(nums):
    menor = min(nums)
    return menor ** (1/3)

"""
if __name__ == "__main__":
    numeros = [] # Pedir 5 números al usuario
    for i in range(5):
        numeros.append(float(input("Ingrese un número real: ")))
    # Calcular y mostrar los resultados
    print(promedio(numeros))
    print(mediana(numeros))
    print(promedio_multiplicativo(numeros))
    print(orden_ascendente(numeros))
    print(orden_descendente(numeros))
    print(potencia_mayor_menor(numeros))
    print(raiz_cubica_menor(numeros))
"""
