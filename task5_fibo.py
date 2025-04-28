# Import reduce from functools
from functools import reduce

# Calculate the fibonacci series of n values using reduce and a lambda function
fib = lambda n: reduce(lambda x, _: x+ [x[-1] + x[-2]],
                       range(n - 2), [0, 1])

# Print the fibonacci series with n values
print(fib(5))  # Print the fibonacci series with 5
print(fib(10)) # Print the fibonacci series with 10
print(fib(20)) # Print the fibonacci series with 20
print(fib(35)) # Print the fibonacci series with 35