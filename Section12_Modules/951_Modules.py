import time

while True:
    with open("../Section11/FILES/vegetables.txt") as file:
        print(file.read())
        time.sleep(10)