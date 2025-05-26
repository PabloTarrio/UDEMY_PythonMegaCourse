# Only Numbers (E)
# Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers.
# For example, if I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 95, 94].
def remove_strings (myList):
    return [item for item in myList if type(item) is not str]
    

print (remove_strings([-10, -2, 6, -4, 3, 0, -1, -9, 2, 9, 'no data', 'no data']))