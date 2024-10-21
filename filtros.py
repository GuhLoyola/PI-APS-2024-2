from PIL import Image  
import numpy as np    

def carregar_imagem(caminho):
    # Define uma função que carrega uma imagem a partir do caminho especificado
    imagem = Image.open(caminho)  # Abre a imagem localizada no caminho fornecido
    return np.array(imagem), imagem.size  # Converte a imagem em um array NumPy e retorna o array e o tamanho da imagem (largura, altura)

def main():
    # Define a função principal do programa
    caminho_imagem = input("Digite o caminho da imagem: ")  # Pede ao usuário para inserir o caminho da imagem
    imagem, tamanho = carregar_imagem(caminho_imagem)  # Chama a função para carregar a imagem e armazena o array da imagem e seu tamanho
    print(f"Imagem carregada com sucesso! Tamanho: {tamanho}")  # Exibe uma mensagem informando que a imagem foi carregada e mostra seu tamanho

 # Exibir a imagem carregada
    img = Image.fromarray(imagem)  # Converte o array de volta para uma imagem
    img.show()  # Mostra a imagem


if __name__ == "__main__":
    # Verifica se o arquivo está sendo executado diretamente
    main()  # Chama a função main para iniciar a execução do programa
    
