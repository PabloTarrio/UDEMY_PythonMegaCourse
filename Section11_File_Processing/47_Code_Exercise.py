'''
Write First 90 (E)
Create a first.txt file that contains the first 90 characters of bear.txt.

Note that you should read the content of bear.txt with Python, extract its first 90 characters with Python, and write those characters in first.txt with Python.
'''

with open("FILES/bear.txt", "r") as myBear:
    content = myBear.read()
    
    
with open("FILES/first.txt", "w") as myFirst:
    myFirst.write (content[:90])