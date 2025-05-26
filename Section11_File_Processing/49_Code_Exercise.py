'''
Copy n-times (E)
The existing content of data.txt looks like this:
1.3, 1.5
2.3, 2.7
Use Python to modify the content of data.txt so that its content looks like below:
1.3, 1.5
2.3, 2.7
1.3, 1.5
2.3, 2.7
1.3, 1.5
2.3, 2.7
So, you need to find a way to insert the existing content two more times.
'''

with open("FILES/data.txt", "r") as myData:
    contenido = myData.read()

with open("FILES/data.txt", "a") as myNewData:
    i = 0
    while (i < 2):
        myNewData.write ("\n")
        myNewData.write(contenido)
        i = i + 1