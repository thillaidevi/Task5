# Import reduce from functools
from functools import reduce

# Define the list of numbers
list_of_numbers = [6, 7, 2, 3, 4, 5, 1]

# Calculate the total product using reduce and a lambda function
total_product = reduce(lambda a, b: a * b, list_of_numbers)

# Print the result
print("Product of all numbers from the list:",total_product)