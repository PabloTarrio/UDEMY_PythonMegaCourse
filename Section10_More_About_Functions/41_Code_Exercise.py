# Indefinite Number of Strings Processed (E)
# Define a function that takes an indefinite number of strings as parameters and returns a list containing all the strings in UPPERCASE and sorted alphabetically. 
# For example, if I called your function with foo("snow", "glacier", "iceberg") it should return ["GLACIER", "ICEBERG", "SNOW"].

def process_strings (*args):
    upper_list = []
    for i in args:
        upper_list.append(i.upper())
    return sorted(upper_list)

print (process_strings("snow", "glacier", "iceberg"))
    

