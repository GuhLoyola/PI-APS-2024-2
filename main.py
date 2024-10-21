import sys
import os
import numpy as np
import matplotlib.image as im
import matplotlib.pyplot as plt

# sys.path.insert(0, os.path.join('..', 'srcs'))

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

# Selecionando o arquivo de Imagem: 

nome_file = os.path.join('images', 'Limes.jpg')

# Lendo a imagem e transformando ela em uma matriz:

matriz_colorida = file_to_matriz(nome_file)

# Passando a imagem pra escala cinza:

matriz_cinza = imagem_to_cinza(matriz_colorida)

# Passando o filtro de blur na imagem:

matriz_com_blur = matriz_cinza.copy()

lins = matriz_cinza.shape[0]
cols = matriz_cinza.shape[1]

m = matriz_cinza

for i in range(1, lins - 1):
    for j in range(1, cols -1):
        matriz_com_blur[i][j] = (
             1*m[i-1][j-1] + 1*m[i-1][j] + 1*m[i-1][j+1] + 
             1*m[i][j-1] + 1*m[i][j] + 1*m[i][j+1] + 
             1*m[i+1][j-1] + 1*m[i+1][j] + 1*m[i+1][j+1]
        ) / 9
       

# Exibindo as imagem com os filtros: 

fig, axs = plt.subplots(1,3)

axs[0].imshow(matriz_colorida)
axs[0].set_title("Imagem colorida")

axs[1].imshow(matriz_cinza, cmap='gray')
axs[1].set_title("Imagem em escala cinza")

axs[2].imshow(matriz_com_blur, cmap='gray')
axs[2].set_title("Imagem com blur")


plt.tight_layout()
plt.show()