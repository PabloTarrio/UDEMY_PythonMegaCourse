import cv2, time

# Capturamos el video desde la cámara del portatil, en este caso 0
# Creamos el objeto video . El parámetro puede ser el número de dispositivo o el PATH a la cámara
video = cv2.VideoCapture(0)

frameCounter = 1
while True:
    frameCounter = frameCounter + 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # time.sleep(1)                                     #Introducir un tiempo de parada para obser que la cámara realmente se activa [comentamos ya que no es necesario realmente]
    print (check)                                       # check = indica si la cámara está hablitada o no
    print (frame)                                       # frame = numpy array de la primera imagen que leemos.
    
    cv2.imshow("Capturing...", gray)
    key = cv2.waitKey(1)  

    if key==ord('q'):                                   # Sólo presionando la tecla 'q' cerramos el programa.
        break

print (frameCounter)
# Liberamos la cámara
video.release()
cv2.destroyAllWindows()