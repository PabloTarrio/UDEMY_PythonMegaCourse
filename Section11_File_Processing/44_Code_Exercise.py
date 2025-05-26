'''
Reading and Processing Text (E)
Read the bear.txt file, and print out the first 90 characters of its content
'''
with open("FILES/bear.txt") as myfile:
    content = myfile.read()
print (content[:90])