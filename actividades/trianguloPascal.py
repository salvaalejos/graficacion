def trianguloPascal(n):
    triangulo = []

    for i in range(n):
        fila = [1] # La primera fila siempre es 1

        if triangulo:
            ultima_fila = triangulo[-1] # Selecciona la última fila del triangulo

            fila.extend([ultima_fila[j] + ultima_fila[j + 1] for j in range(len(ultima_fila) - 1)]) # Suma los diferentes valores en la ultima fila
            fila.append(1) # Nueva fila

        triangulo.append(fila)

    return triangulo
    

n = int(input("Ingrese la cantidad de filas: "))

t = trianguloPascal(n)

for fila in t:
    print(fila)
