def calcular_producto_punto(v, w):
    # Verificamos que los arreglos tengan el mismo tamaño
    if len(v) != len(w):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    # Inicializamos la variable para almacenar el producto punto
    producto_punto = 0
    # Iteramos a través de los elementos de los arreglos
    for i in range(len(v)):
        producto_punto += v[i] * w[i]
    return producto_punto

def main():
    # Solicitar al usuario que ingrese los dos arreglos
    entrada_v = input("Ingresa los números del primer arreglo, separados por espacios: ")
    entrada_w = input("Ingresa los números del segundo arreglo, separados por espacios: ")
    # Convertir las entradas en listas de números reales (o enteros)
    v = [float(num) for num in entrada_v.split()]
    w = [float(num) for num in entrada_w.split()]
    # Verificar que los arreglos tengan el mismo tamaño
    if len(v) != len(w):
        print("Error: Los arreglos deben tener el mismo tamaño.")
        return 
    # Calcular el producto punto usando la función
    producto = calcular_producto_punto(v, w)
    # Mostrar el resultado
    print(f"El producto punto de los arreglos es: {producto}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
