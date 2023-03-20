import cv2  # importando a biblioteca do OpenCv

# definindo um objeto de captura(Camera). O número "0" pode definir qual dispositivo irá ser conectado. Caso haja apenas uma camera, geralmente será a 0.
vid = cv2.VideoCapture(0)

while (True):
    # capturando o video frame por frame
    ret, frame = vid.read()

    # Gerar uma janela que irá exibir a imagem
    cv2.imshow('frame', frame)

    # definindo o botão para parar a aplicação, que nesse caso é o "q". O valor 0xFF é uma máscara binária que é frequentemente usada para extrair os últimos 8 bits de um valor inteiro (que é o equivalente a um byte). Isso é útil porque, em Python, a função cv2.waitKey() retorna um inteiro de 32 bits que contém informações sobre o evento do usuário.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fecha o arquivo de vídeo ou o dispositivo de captura
vid.release()

# Destroi todas as janelas feitas pela aplicação
cv2.destroyAllWindows()
