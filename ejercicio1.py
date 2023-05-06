class Nodo:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso
        self.izq = None
        self.der = None


def decodificar_huffman(secuencia, raiz):
    decodificacion = ""
    nodo_actual = raiz
    for bit in secuencia:
        if bit == "0":
            nodo_actual = nodo_actual.izq
        elif bit == "1":
            nodo_actual = nodo_actual.der
        if nodo_actual.valor is not None:
            decodificacion += nodo_actual.valor
            nodo_actual = raiz
    return decodificacion


# Construir árbol de Huffman
espacio = Nodo(' ', 17)
coma = Nodo(',', 2)
V = Nodo('V', 2)
Q = Nodo('Q', 1)
B = Nodo('B', 2)
G = Nodo('G', 3)
D = Nodo('D', 3)
T = Nodo('T', 3)
M = Nodo('M', 3)
C = Nodo('C', 4)
P = Nodo('P', 4)
S = Nodo('S', 4)
U = Nodo('U', 4)
I = Nodo('I', 6)
L = Nodo('L', 6)
N = Nodo('N', 6)
O = Nodo('O', 7)
R = Nodo('R', 10)
A = Nodo('A', 11)
E = Nodo('E', 14)

nuevo_nodo1 = Nodo(None, 12)
nuevo_nodo1.izq = I
nuevo_nodo1.der = L

nuevo_nodo2 = Nodo(None, 25)
nuevo_nodo2.izq = nuevo_nodo1
nuevo_nodo2.der = E

nuevo_nodo3 = Nodo(None, 35)
nuevo_nodo3.izq = nuevo_nodo2
nuevo_nodo3.der = R

nuevo_nodo4 = Nodo(None, 38)
nuevo_nodo4.izq = nuevo_nodo3
nuevo_nodo4.der = Nodo(None, None)

raiz = nuevo_nodo4

# Decodificar mensajes
mensaje1 = "100010111010110000101110100011100000110110000001111001111010010110"
mensaje2 = "0001101001110011010001011101011111110100001111001111110011110100011000110000"
mensaje3 = "00101101011110111111101110101101101110011101101111001111111001010010100101000001"
mensaje4 = "011010110001011001101000111001001011000011001000110101101010111111111110110111"
mensaje5 = "0111001000010010101100011111110001000111011001100101101000110111110101101000"
mensaje6 = "110111000000011100100101010001111110000110010110101110011111010"


print(decodificar_huffman(mensaje1, raiz))
print(decodificar_huffman(mensaje2, raiz))
print(decodificar_huffman(mensaje3, raiz))
print(decodificar_huffman(mensaje4, raiz))
print(decodificar_huffman(mensaje5, raiz))
print(decodificar_huffman(mensaje6, raiz))

