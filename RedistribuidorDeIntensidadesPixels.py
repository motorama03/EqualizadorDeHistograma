from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def equalizar_histograma(image_path, output_path):
    # Carregar a imagem em escala de cinza
    imagem = Image.open(image_path).convert("L")
    largura, altura = imagem.size
    total_pixels = largura * altura
    
    # Obter o histograma da imagem
    histograma = imagem.histogram()
    L = len(histograma)  # Número de níveis de intensidade (256 para 8 bits)

    # Calcular as probabilidades
    probabilidade = [h / total_pixels for h in histograma]

    # Calcular a função de transferência cumulativa
    s = [(L-1) * sum(probabilidade[:k+1]) for k in range(L)]
    s = [round(valor) for valor in s]  # Arredondar os valores
    
    # Mapear os pixels da imagem original para a equalizada
    pixel_map = {i: s[i] for i in range(L)}
    pixels = np.array(imagem)
    imagem_equalizada = np.vectorize(pixel_map.get)(pixels)

    # Salvar a imagem equalizada
    imagem_equalizada = Image.fromarray(imagem_equalizada.astype('uint8'))
    imagem_equalizada.save(output_path)

    # Gerar o novo histograma
    novo_histograma = imagem_equalizada.histogram()

    # Exibir os histogramas
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Histograma Original")
    plt.bar(range(L), histograma, color='gray')
    plt.subplot(1, 2, 2)
    plt.title("Histograma Equalizado")
    plt.bar(range(L), novo_histograma, color='gray')
    plt.show()

# Exemplo de uso
input_image = r"C:\Users\mateu\OneDrive\Documentos\BCC\PDI\Fig0316(4)(bottom_left).tif"
output_image = r"C:\Users\mateu\OneDrive\Documentos\BCC\PDI\imagem_equalizada_fig0316(4).tif"
equalizar_histograma(input_image, output_image)
