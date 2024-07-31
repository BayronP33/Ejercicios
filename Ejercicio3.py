def calcular_producto_directo(v, w):
    # Verificamos que los arreglos tengan el mismo tamaño
    if len(v) != len(w):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    # Inicializamos un nuevo arreglo para almacenar el producto directo
    producto_directo = []  
    # Iteramos a través de los elementos de los arreglos
    for i in range(len(v)):
        # Calculamos el producto de los elementos correspondientes
        producto = v[i] * w[i]
        # Agregamos el resultado al nuevo arreglo
        producto_directo.append(producto)  
    return producto_directo

def main():
    # Solicitar al usuario que ingrese los dos arreglos
    entrada_v = input("Ingresa los números del primer arreglo, separados por espacios: ")
    entrada_w = input("Ingresa los números del segundo arreglo, separados por espacios: ")
    # Convertir las entradas en listas de números reales
    v = [float(num) for num in entrada_v.split()]
    w = [float(num) for num in entrada_w.split()] 
    # Verificar que los arreglos tengan el mismo tamaño
    if len(v) != len(w):
        print("Error: Los arreglos deben tener el mismo tamaño.")
        return
    # Calcular el producto directo usando la función
    producto_directo = calcular_producto_directo(v, w) 
    # Mostrar el resultado
    print(f"El producto directo de los arreglos es: {producto_directo}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
