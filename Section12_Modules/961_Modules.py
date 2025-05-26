import time
import os

while True:
    if os.path.exists("FILES/temps_today.csv"):
        with open("FILES/temps_today.csv") as file:
            print(file.read())
    else:
        print ("File does not exists.")
    time.sleep(10)