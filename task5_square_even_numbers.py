list_of_numbers = [4, 6, 9, 7, 3, 2, 0]
# Define the list of numbers

even_numbers = filter(lambda n: n % 2 == 0, list_of_numbers)
# Getting the even number from the list

square_even_list_no_func = list(map(lambda n: n * n, even_numbers))
# Create a list, mapping the square values of the even numbers into it

print("Square of even number list", square_even_list_no_func)
# Print the result