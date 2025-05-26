# Zeros Instead (E)
# Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros instead of strings. 
# For example, I called your function with foo([99, 'no data', 95, 94, 'no data']) it should return [99, 0, 95, 94, 0].

def zero_instead (my_list):
    return [i if type(i) is int else 0 for i in my_list]

print (zero_instead([99, 'no data', 95, 94, 'no data']))