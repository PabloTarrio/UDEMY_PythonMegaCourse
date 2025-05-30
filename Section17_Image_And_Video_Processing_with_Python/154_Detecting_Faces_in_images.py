import cv2

# Creamos el objeto CASCADA 
face_cascade = cv2.CascadeClassifier("./resources/Files/haarcascade_frontalface_default.xml")

# Leer la imagen, en este caso la leemos en color
img = cv2.imread ("./resources/Files/photo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
faces = face_cascade.detectMultiScale(resized_img,
                                    scaleFactor = 1.05,         # Factor de escalado: para la busqueda de caras en la imagen.
                                    minNeighbors= 5,            # 
                                    )
print (type(faces))
print (faces)                                                   # Mostramos los pixeles en los cuales se detecta la cara

for x, y, w, h in faces:                                        # Dibujamos el rectángulo en la cara detectada
    img = cv2.rectangle(
        resized_img,
        (x, y),                                                 # Punto superior izquierdo (x, y) obtenido anteriomente en FACES
        (x+w, y+h),                                             # Punto inferior derecho (x+ancho, y+alto) con los datos obtenidos anteriormente
        (0, 255, 0),                                            # Definimos el color del rectángulo en BGR
        3                                                       # Ancho de la linea del rectángulo
        ) 
cv2.imshow("Gray", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()