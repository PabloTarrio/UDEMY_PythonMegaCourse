import cv2, time

# Capturamos el video desde la cámara del portatil, en este caso 0
video = cv2.VideoCapture(0)
check, frame = video.read()

time.sleep(5)


cv2.imshow("Capturing...", frame)
cv2.waitKey(0)
# Liberamos la cámara
video.release()
cv2.destroyAllWindows()