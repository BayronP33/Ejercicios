def calcular_promedio(arreglo):
    # Verificamos que el arreglo no esté vacío
    if len(arreglo) == 0:
        return 0
    # Calculamos la suma de los elementos del arreglo
    suma = sum(arreglo)  
    # Calculamos el promedio dividiendo la suma entre el número de elementos
    promedio = suma / len(arreglo)
    return promedio

def main():
    # Solicitar al usuario que ingrese los números reales, separados por espacios
    entrada = input("Ingresa los números reales separados por espacios: ")
    # Convertir la entrada en una lista de números reales
    arreglo_reales = [float(num) for num in entrada.split()]
    # Calcular el promedio usando la función
    promedio = calcular_promedio(arreglo_reales)   
    # Mostrar el resultado
    print(f"El promedio del arreglo es: {promedio}")
# Ejecutar la función principal
if __name__ == "__main__":
    main()
