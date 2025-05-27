# Convert and Sum Up (E)
# Define a function that takes as parameter a list that contains decimal numbers as strings and returns the sum of those numbers.
# For example, I called your function with foo(['1.2', '2.6', '3.3']) it should return 7.1. Note that the floats of the input list are string datatypes.
def convert_sumup (my_list):
    new_list = [float(i) for i in my_list if isinstance(i, str) ]
    sumup = 0
    for j in new_list:
        sumup = sumup + j
    return (sumup)

print (convert_sumup(['1.2', '2.6', '3.3']))