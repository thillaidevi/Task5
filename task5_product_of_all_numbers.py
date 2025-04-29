def my_reduce(func, iterable):  #created reduce function
    result = iterable[0]  # Start with the first element, initialized result as first value
    for item in iterable[1:]:  # Iterate through the rest
        result = func(result, item)  # Apply function cumulatively
    return result

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Using lambda and custom reduce function to calculate product
total_product = my_reduce(lambda a, b: a * b, numbers)

# Print the result
print("Product of all numbers from the list:", total_product)