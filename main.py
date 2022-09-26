import cv2
import numpy as np

'''
Demonstrando como funciona a Transformada de Hough quando aplicada a circunferencias,
para ver o procedimento das imagens basta executar o código e apertar qualquer tecla para que seja mostrado o proximo processo aplicado.
'''

# Imagem original
imgO = cv2.imread('.\img\cafe.png', cv2.IMREAD_COLOR)
img = cv2.resize(imgO, (400, 300))
cv2.imshow('Original', img)
cv2.waitKey(0)

# Imagem em cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cinza', gray)
cv2.waitKey(0)

# Imagem borrada
gray_blurred = cv2.blur(gray, (9, 9))
cv2.imshow('Blur', gray_blurred)
cv2.waitKey(0)

# Detectando os circulos
detected_circles = cv2.HoughCircles(
    gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)

# Validacao
if detected_circles is not None:

    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
        # Printando o centro e raio de cada circulo encontrado
        print("Centro ({:}, {:}), raio = {:}".format(a, b, r))

        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        # Imagem com as circunferencias
        cv2.imshow("Circunferencias", img)
        cv2.waitKey(0)
