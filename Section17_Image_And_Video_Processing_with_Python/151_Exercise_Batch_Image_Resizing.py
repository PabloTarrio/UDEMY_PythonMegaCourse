# Exercise: Batch Image Resizing
# Write a script that resizes all images in a directory to 100x100. You can find an attached ZIP file with some image files in the Resources.
import cv2
import glob

# Creamos una lista con los nombres de los archivos mediante el paquete GLOB
imagesNamesList = glob.glob ("./resources/sample_images/*.jpg")

# Recorremos la lista de imagenes y cada una de ellas la redimensionamos a la mitad de tamaña
#            y mostramos la original y la redimensionada, cerrado cada una de ellas tras 1 seg. 
#            Finalmente, guardamos la imagen redimensionada en una carpeta para cada imagen, 
#                   en cuyo nombre se incluye el nombre de la imagen
for imageName in imagesNamesList:
    img = cv2.imread(imageName, 0)
    resized_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
    cv2.imshow ("Original", img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imshow("Resized", resized_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite ("./resources/sample_images/resized"+imageName+".jpg", resized_img)
