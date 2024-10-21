import sys
import os
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


nome_file = os.path.join('images', 'Red_Wine_Glass.jpg')

matriz_colorida = file_to_matriz(nome_file)

matriz_cinza = imagem_to_cinza(matriz_colorida)

lins = matriz_cinza.shape[0]
cols = matriz_cinza.shape[1]


matriz_imagem_sobel_vertical = matriz_cinza.copy()
matriz_imagem_sobel_horizontal = matriz_cinza.copy()

# Passando filtro Sobel vertical:


m = matriz_cinza
for i in range(1, lins-1):
    for j in range(1, cols-1):
        matriz_imagem_sobel_vertical[i][j] = (
                                    1*m[i-1][j-1] + 0*m[i-1][j  ] + -1*m[i-1][j+1] + 
                                    2*m[i  ][j-1] + 0*m[i  ][j  ] + -2*m[i  ][j+1] + 
                                    1*m[i+1][j-1] + 0*m[i+1][j  ] + -1*m[i+1][j+1]
                                    )
        matriz_imagem_sobel_vertical[i][j] = max(0, matriz_imagem_sobel_vertical[i][j])
        matriz_imagem_sobel_vertical[i][j] = min(255, matriz_imagem_sobel_vertical[i][j])

# Passando filtro Sobel horizontal:

m = matriz_cinza
for i in range(1, lins-1):
    for j in range(1, cols-1):
        matriz_imagem_sobel_horizontal[i][j] = (
                                    1*m[i-1][j-1] +  2*m[i-1][j  ] +  1*m[i-1][j+1] + 
                                    0*m[i  ][j-1] +  0*m[i  ][j  ] +  0*m[i  ][j+1] + 
                                   -1*m[i+1][j-1] + -2*m[i+1][j  ] + -1*m[i+1][j+1]
                                    )
        matriz_imagem_sobel_horizontal[i][j] = max(0, matriz_imagem_sobel_horizontal[i][j])
        matriz_imagem_sobel_horizontal[i][j] = min(255, matriz_imagem_sobel_horizontal[i][j])

# Passando filtro Sobel horizontal + vertical: 

matriz_imagem_sobel = matriz_imagem_sobel_horizontal + matriz_imagem_sobel_vertical
for i in range(1, lins-1):
    for j in range(1, cols-1):
        matriz_imagem_sobel[i][j] = max(0, matriz_imagem_sobel[i][j])
        matriz_imagem_sobel[i][j] = min(255, matriz_imagem_sobel[i][j])

fig, axs = plt.subplots(1,3)

axs[0].imshow(matriz_imagem_sobel_vertical, cmap='gray')
axs[0].set_title("Filtro Sobel Vertical")

axs[1].imshow(matriz_imagem_sobel_horizontal, cmap='gray')
axs[1].set_title("Filtro Sobel Horizontal")

axs[2].imshow(matriz_imagem_sobel, cmap='gray')
axs[2].set_title("Filtro Sobel Horizontal + Vertical")

plt.tight_layout()
plt.show()