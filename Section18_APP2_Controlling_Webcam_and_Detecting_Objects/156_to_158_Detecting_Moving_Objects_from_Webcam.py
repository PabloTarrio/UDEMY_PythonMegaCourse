import cv2, time, pandas
from datetime import datetime

df = pandas.DataFrame(columns=["Start", "End"])
motion_status_list = [None, None]                                                                           # Creamos una lista vacía para saber los estodos de detección de movimiento
times = []
first_frame = None                                                                                          # Variable "vacía" en la que guardaremos el primer frame
video = cv2.VideoCapture(0)

# BUCLE PARA CAPTURA DE VIDEO.
# Leemos la imagen desde la cámara, la editamos a escala de grises,
#   mostramos la imagen por pantalla e imprimimos el dataFrame
#   Salimos del bucle y del programa con la tecla 'q'
while True:
    check, frame = video.read()
    motion_status = False                                                                                   # Variable para el control del movimiento
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21, 21), 0)

    # Si la primera captura está vacía, asignamos a esta variable el primer array numpy para poder comparar más tarde.
    if first_frame is None:
        first_frame = gray
        continue                                                                                            # Saltamos el resto del bucle y comenzamos la 2 iteración

    delta_frame = cv2.absdiff(first_frame, gray)                                                            # Comparamos el primer frame (base) con los siguientes.
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    (cnts, _) = cv2.findContours (thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)          # Encontramos los contornos de la imagen
    
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        motion_status = True                                                                                # Activamos el trigger de detección de movimiento
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    motion_status_list.append(motion_status)                                                                # Añadimos el estado del control de movimento a la lista 
    if motion_status_list[-1] == 1 and motion_status_list[-2] == 0:                                         # Comparamos el estado de la lista con el anterior, en caso de cambiar
        times.append(datetime.now())                                                                         #       grabamos la fecha y hora en la que se produce el disparo.
    if motion_status_list[-1] == 0 and motion_status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow ("Capturing...", gray)
    cv2.imshow ("Delta Frame", delta_frame)
    cv2.imshow ("Threshold...", thresh_frame)
    cv2.imshow ("Color Frame", frame)

    key = cv2.waitKey(1)
    if key==ord('q'):
        if motion_status == True:
            times.append(datetime.now())
        break

for i in range (0, len(times), 2):
    df = df._append ({"Start":times[i], "End":times[i+1]}, ignore_index = True)
df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()