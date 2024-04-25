import heapq
import os
import gzip
from collections import Counter

# Clase para representar los nodos del árbol de Huffman
class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Construir el árbol de Huffman a partir de las frecuencias de los caracteres
def construir_arbol_huffman(diccionario_caracteres):
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in diccionario_caracteres.items()]
    heapq.heapify(cola_prioridad)
    while len(cola_prioridad) > 1:
        nodo_izquierda = heapq.heappop(cola_prioridad)
        nodo_derecha = heapq.heappop(cola_prioridad)
        nodo_padre = NodoHuffman(None, nodo_izquierda.frecuencia + nodo_derecha.frecuencia)
        nodo_padre.izquierda = nodo_izquierda
        nodo_padre.derecha = nodo_derecha
        heapq.heappush(cola_prioridad, nodo_padre)
    return cola_prioridad[0]

# Generar los códigos Huffman para cada caracter
def generar_codigo_huffman(arbol, codigo='', diccionario_codigos={}):
    if arbol is not None:
        if arbol.caracter is not None:
            diccionario_codigos[arbol.caracter] = codigo
        generar_codigo_huffman(arbol.izquierda, codigo + '0', diccionario_codigos)
        generar_codigo_huffman(arbol.derecha, codigo + '1', diccionario_codigos)
    return diccionario_codigos

# Comprimir el texto usando los códigos Huffman
def comprimir_archivo_huffman(texto, diccionario_codigos):
    texto_codificado = ''.join(diccionario_codigos[caracter] for caracter in texto)
    padding = 8 - (len(texto_codificado) % 8)
    texto_codificado += padding * '0'
    padding_info = "{0:08b}".format(padding)
    texto_codificado = padding_info + texto_codificado
    bytes_codificados = bytearray()
    for i in range(0, len(texto_codificado), 8):
        byte = texto_codificado[i:i+8]
        bytes_codificados.append(int(byte, 2))
    return bytes(bytes_codificados)

# Función principal para comprimir el texto usando Huffman
def comprimir_huffman(texto):
    contador = Counter(texto)
    arbol = construir_arbol_huffman(contador)
    diccionario_codigos = generar_codigo_huffman(arbol)
    bytes_codificados = comprimir_archivo_huffman(texto, diccionario_codigos)
    return bytes_codificados, diccionario_codigos

# Leer el texto desde el archivo
texto = ""
print("El texto a leer: ")
with open("Gullivers_Travels.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()
    print(texto)

# Contar los caracteres del texto
num_carac = len(texto)
print("\nNumero de caracteres en el texto son:", num_carac)

# Comprimir el texto usando Huffman
bytes_codificados, diccionario_codigos = comprimir_huffman(texto)

# Guardar el archivo comprimido
with gzip.open("salida.txt.gz", "wb") as salida:
    salida.write(bytes_codificados)

print("Se ha guardado en 'salida.txt.gz' comprimido.")
