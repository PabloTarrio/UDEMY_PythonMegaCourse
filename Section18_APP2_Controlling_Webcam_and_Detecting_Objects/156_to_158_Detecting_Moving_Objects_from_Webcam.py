import cv2, time

first_frame = None                                                        # Variable "vacía" en la que guardaremos el primer frame
video = cv2.VideoCapture(0)

# BUCLE PARA CAPTURA DE VIDEO.
# Leemos la imagen desde la cámara, la editamos a escala de grises,
#   mostramos la imagen por pantalla e imprimimos el dataFrame
#   Salimos del bucle y del programa con la tecla 'q'
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21, 21), 0)

    # Si la primera captura está vacía, asignamos a esta variable el primer array numpy para poder comparar más tarde.
    if first_frame is None:
        first_frame = gray
        continue                                                          # Saltamos el resto del bucle y comenzamos la 2 iteración

    delta_frame = cv2.absdiff(first_frame, gray)                          # Comparamos el primer frame (base) con los siguientes.
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    # Encontramos los contornos de la imagen
    (cnts, _) = cv2.findContours (thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)
        
    cv2.imshow ("Capturing...", gray)
    cv2.imshow ("Delta Frame", delta_frame)
    cv2.imshow ("Threshold...", thresh_frame)
    cv2.imshow ("Color Frame", frame)

    print (gray)
    print (delta_frame)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()