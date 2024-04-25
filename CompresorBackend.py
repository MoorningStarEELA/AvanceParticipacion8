import gzip  # Importar la biblioteca gzip para comprimir archivos
from collections import Counter  # Importar Counter para contar los caracteres del txt

print("El texto a leer: ")
# Leer, abrir y mostrar el texto seleccionado
with open("Gullivers_Travels.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()  # Leer el contenido del archivo
    print(contenido)  # Mostrar el contenido del archivo en la consola
    contador = Counter(contenido)  # Contar la frecuencia de cada caracter en el texto

# Ordenar los caracteres por frecuencia
carac_ordenar = sorted(contador.items(), key=lambda x: x[1], reverse=True)

# Contar los caracteres del texto
num_carac = len(contenido)
print("\nNumero de caracteres en el texto son:", num_carac)

# Crear y escribir en el archivo comprimido
with gzip.open("salida.txt.gz", "wt", encoding="utf-8") as salida:
    salida.write("Numero de caracteres en el texto son: " + str(num_carac) + "\n\n")
    salida.write("Caracter : frecuencia\n")
    for caracter, frecuencia in carac_ordenar:
        salida.write(f"{caracter}:{frecuencia}\n")

print("Se ha guardado en 'salida.txt.gz' comprimido.")
