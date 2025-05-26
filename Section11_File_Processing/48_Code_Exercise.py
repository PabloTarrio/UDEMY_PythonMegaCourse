'''
Read and Append (E)
Append the text of bear1.txt to bear2.txt. 
In other words, bear2.txt should contain its text and the text of bear1.txt after that.
'''
with open("FILES/bear1.txt", "r") as myBearFile1:
    content1 = myBearFile1.read()

with open("FILES/bear2.txt", "a+") as MyBearFile2:
    MyBearFile2.write(content1)
    MyBearFile2.seek(0)
    print (MyBearFile2.read())