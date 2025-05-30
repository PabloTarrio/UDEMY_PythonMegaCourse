import cv2


# Cargamos la imagen desde el directorio
# En el siguiente parámetro indicamos "como queremos leer la imagen"
#           [1] Imagen a color, "la imagen como es"
#           [0] Imagen en B/N
#           [-1] Imagen a color, pero con la banda alpha o transparencia
img = cv2.imread("./resources/galaxy.jpg",0)

# La impresion del tipo de la variable creada es un objeto numpy, una matriz de numeros enteros que representan los píxeles
print (type(img))
# Imprime la matriz con miles de pixeles
print (img)
# Imprimir el número de píxeles que forman la imagen -> RESOLUCION
print (img.shape)
# Imprimir las dimensiones -> en este caso 2 dimensiones.
print (img.ndim)

# Para mostrar la imagen en una ventana usamos el método IMSHOW
#       Antes la redimensiomaos con el método RESIZE, indicando la imagen y el tamaño de salida TUPLA (ancho, alto) en los parámetros
#           la redimensión se realiza cojiedo el parámetro directamente desde SHAPE dividio entre 2, esto nos devuelve un FLOAT, por o que forzamos la conversión a INT
#           que es lo que espera la función RESIZE.
resized_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow ("Galaxy", resized_img)
# Guardamos la nueva imagen generada: BN y redimensionada
cv2.imwrite("./resources/Galaxy_resized.jpg", resized_img)
# Esperamos a pulsar cualquier tecla durante 2 segundos y tras ello destruimos o cerramos la imagen
cv2.waitKey(2000)
cv2.destroyAllWindows()

