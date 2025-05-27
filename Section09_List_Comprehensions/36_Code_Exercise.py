# Only Positive Numbers (E)
# Define a function that takes as parameter list of numbers and returns the list containing only the numbers that are greater than 0. 
# For example, I called your function with foo([-5, 3, -1, 101]) it should return [3, 101].

def remove_strings (myList):
    return [item for item in myList if item > 0]
    

print (remove_strings([-5, 3, -1, 101]))