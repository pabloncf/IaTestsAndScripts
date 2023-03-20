import cv2
import numpy as np
import subprocess

subprocess.run("pip install --upgrade pyqt5 lxml", shell=True)

# Cria o classificador Haar Cascade para detecção de pessoas
classificador = cv2.CascadeClassifier('pessoa.xml')

# Inicializa a câmera do computador
captura = cv2.VideoCapture(0)

# Loop infinito para capturar imagens da câmera e detectar pessoas em tempo real
while True:
    # Captura uma imagem da câmera
    ret, imagem = captura.read()

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detecta as pessoas na imagem
    pessoas = classificador.detectMultiScale(gray)

    # Desenha um retângulo em volta de cada pessoa detectada na imagem
    for (x, y, largura, altura) in pessoas:
        cv2.rectangle(imagem, (x, y), (x + largura,
                      y + altura), (0, 255, 0), 2)

    # Exibe a imagem com as pessoas detectadas
    cv2.imshow('Imagem com pessoas detectadas', imagem)

    # Verifica se a tecla 'q' foi pressionada para encerrar o loop
    if cv2.waitKey(1) == ord('q'):
        break

# Libera a câmera e fecha as janelas
captura.release()
cv2.destroyAllWindows()
