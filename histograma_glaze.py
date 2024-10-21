import sys  
import os
#sys.path.insert(0, os.path.join('..', 'srcs'))
import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt


def file_to_matriz(nome_file: str) -> np.array:
    
    matriz_colorida = im.imread(nome_file)
    matriz_8bit = matriz_colorida
    matriz_8bit = matriz_8bit.astype(np.uint16)

    return matriz_8bit

def imagem_to_cinza(matrix_colorida: np.array) -> np.array:




    linhas = matrix_colorida.shape[0]
    colunas = matrix_colorida.shape[1]

    matrix_gray = np.zeros((linhas, colunas))

    for i in range(linhas):
        for j in range(colunas):
            r, g, b = matrix_colorida[i, j]
            matrix_gray[i,j] = int((r + g + b) / 3)

    return matrix_gray


nome_file = os.path.join("images", "Glaze.jpg")

matriz_colorida = file_to_matriz(nome_file)

matriz_cinza = imagem_to_cinza(matriz_colorida)
matriz_colorida.shape

#Histograma
histograma = np.zeros(256).astype(int)

linhas = matriz_cinza.shape[0]
colunas = matriz_cinza.shape[1]

for i in range(linhas):
    for j in range(colunas):
        cor = matriz_cinza[i,j]
        cor = int(cor)
        histograma[cor] = histograma[cor] + 1

threshold = 200

linhas = matriz_cinza.shape[0]
colunas = matriz_cinza.shape[1]

matrix_segmentada = np.zeros((linhas, colunas))

for i in range(linhas):
    for j in range(colunas):
        cor = matriz_cinza[i,j]
        if cor < threshold:
            matrix_segmentada[i,j] = 0
        else:
            matrix_segmentada[i,j] = 255

fig, axs = plt.subplots(1,1)
axs[0].imshow(matrix_segmentada, cmap = "gray")
axs[0].set_title("Imagem Segmentada")       

axs[1].plot(range(256), histograma)
axs[1].plot([threshold, threshold], [0, 40_000])

axs[2].plot(range(256), histograma)

plt.tight_layout()     
plt.show()