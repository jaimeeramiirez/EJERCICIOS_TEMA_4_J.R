            #          ' ' (17)
            #        /      \
            #      /         \
            #     /            \
            #    /               \
            # ',' (2)             'E' (14)
            #                   /      \
            #                 /         \
            #               /            \
            #             /               \
            #           'A' (11)        'R' (10)
            #          /      \           /     \
            #        /         \        /        \
            #      /            \     /           \
            #    /               \  /              \
            #  'B' (2)         'C' (4)         'D' (3)
            #                  /    \           /    \
            #                 /      \         /      \
            #               /         \      /         \
            #             /            \   /            \
            #           'G' (3)     'I' (6)       'L' (6)
            #                          /   \         /    \
            #                        /      \      /       \
            #                      /         \   /          \
            #                   'M' (3)   'N' (6)        'O' (7)
            #                                /   \         /    \
            #                               /      \      /       \
            #                             /         \   /          \
            #                           'P' (4)   'S' (4)        'T' (3)
            #                                        /   \
            #                                       /      \
            #                                     /         \
            #                                   'U' (4)   'V' (2)

import heapq
from collections import defaultdict

#Tabla de frecuencias
caracter_cantidad = {
    'A': 11, 'B': 2, 'C': 4, 'D': 3, 'E': 14, 'G': 3, 'I': 6, 'L': 6,
    'M': 3, 'N': 6, 'O': 7, 'P': 4, 'Q': 1, 'R': 10, 'S': 4, 'T': 3,
    'U': 4, 'V': 2, ' ': 17, ',': 2
}

# Calcular frecuencias
total_caracteres = sum(caracter_cantidad.values()) 
frecuencias = {caracter: cantidad / total_caracteres for caracter, cantidad in caracter_cantidad.items()} 

#Arbol de Huffman
def crear_arbol_huffman(frecuencias):
    heap = [[peso, [caracter, ""]] for caracter, peso in frecuencias.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

huffman_tree = crear_arbol_huffman(frecuencias) # Arbol de Huffman
huffman_codes = {caracter: code for caracter, code in huffman_tree[1:]} # Diccionario de codigos Huffman

#Mensajes que debemos descodificar
mensaje1 = "100010111010110000101110100011100000110110000001111001111010010110000110100111001101000101110101111111010000111100111111001111010001100011000000101101011110111111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100011001011010111001100111101000110001100000010110101111100111001"
mensaje2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"


# Descomprimir mensaje
def descomprimir_mensaje(mensaje, huffman_codes):
    resultado = ""
    codigo_actual = ""
    diccionario_codigos = {code: caracter for caracter, code in huffman_tree[1:]}
    for bit in mensaje:
        codigo_actual += bit
        if codigo_actual in diccionario_codigos:
            resultado += diccionario_codigos[codigo_actual]
            codigo_actual = ""
    return resultado

#Imprimimos los mensajes descodificados
mensaje1_descodificado = descomprimir_mensaje(mensaje1, huffman_codes)
mensaje2_descodificado = descomprimir_mensaje(mensaje2, huffman_codes)

print("Mensaje 1 descodificado: ", mensaje1_descodificado)
print("Mensaje 2 descodificado: ", mensaje2_descodificado)



#ESPACIO DE MEMORIA

def calcular_espacio_memoria(mensaje_original, mensaje_comprimido):
    espacio_original = len(mensaje_original) * 8  # 8 bits por cada caracter
    espacio_comprimido = len(mensaje_comprimido)
    return espacio_original, espacio_comprimido

espacio_mensaje1 = calcular_espacio_memoria(mensaje1, mensaje1_descodificado)
espacio_mensaje2 = calcular_espacio_memoria(mensaje2, mensaje2_descodificado)

print("Espacio mensaje 1: ", espacio_mensaje1)
print("Espacio mensaje 2: ", espacio_mensaje2)


#PORCENTAJE DE COMPRESION
def calcular_porcentaje_compresion(mensaje_original, mensaje_comprimido):
    espacio_original, espacio_comprimido = calcular_espacio_memoria(mensaje_original, mensaje_comprimido)
    porcentaje_compresion = (espacio_original - espacio_comprimido) / espacio_original * 100
    return porcentaje_compresion

porcentaje_compresion_mensaje1 = calcular_porcentaje_compresion(mensaje1, mensaje1_descodificado)
porcentaje_compresion_mensaje2 = calcular_porcentaje_compresion(mensaje2, mensaje2_descodificado)

print("Porcentaje de compresion mensaje 1: ", porcentaje_compresion_mensaje1)
print("Porcentaje de compresion mensaje 2: ", porcentaje_compresion_mensaje2)

