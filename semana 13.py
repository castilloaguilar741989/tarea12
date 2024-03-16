def temperatura_promedio(ciudades_temperaturas):
    """
    Esta función calcula la temperatura promedio de un conjunto de ciudades.
    Args:
        ciudades_temperaturas (dict): Un diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas como valores.
    Returns:
        dict: Un diccionario que contiene nombres de ciudades como claves
              y temperaturas promedio como valores.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Ejemplo de datos de temperaturas para ciudades
ciudades_temperaturas = {
    "Ambato": [22, 25, 23, 24, 26, 28, 27],
    "Santo Domingo": [28, 27, 26, 25, 24, 23, 22],
    "Ibarra": [23, 24, 25, 26, 27, 28, 29],
    "Cuenca": [18, 19, 20, 21, 22, 23, 24],
    "Quito": [20, 21, 22, 23, 24, 25, 26],
    "Manta": [25, 26, 27, 28, 29, 30, 31]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
