# Average Function (E)
# Define a function that takes an indefinite number of numbers as arguments and returns their average.
# If I called your function with foo(10, 20, 30, 40) it should return the 25, the average of those numbers.

def average (*args):
    return sum(args) / len(args)

print (average (10, 20, 30, 40))