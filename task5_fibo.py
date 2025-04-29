fibonacci = lambda n: [0 if i == 0 else (1 if i == 1 else fibonacci(n - 1)[i - 1] + fibonacci(n - 1)[i - 2]) for i in range(n)]
"""This defines an anonymous function (lambda function) that accepts n argument,
loop conditions- This is a list comprehension that iterates from 0 up to n.
# In each iteration, i represents the index of the nth term"""

n_terms = 10 # Initialized nth term as 10

result = fibonacci(n_terms) # fibonacci list series assigned to result

print(f"Fibonacci series up to {n_terms} terms: {result}") # Print the fibonacci series with 10 values

print(fibonacci(2)) # Print the fibonacci series with 2 values

print(fibonacci(3)) # Print the fibonacci series with 3 values

print(fibonacci(4)) # Print the fibonacci series with 4 values

print(fibonacci(5))  # Print the fibonacci series with 5 values



