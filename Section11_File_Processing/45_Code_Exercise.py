'''
File Processing Inside Function (E)
Define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file.
'''
def caracterInText (caracter, filepath):
    with open(filepath) as myfile:
        content = myfile.read()
        
    return content.count(caracter)

print (caracterInText ('c', "FILES/copy_from_fruits.txt"))