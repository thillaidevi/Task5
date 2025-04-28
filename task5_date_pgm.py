# Import the 'datetime' module to work with date and time
import datetime

# Get the current date and time using 'datetime.datetime.now()' and store it in the variable 'now'
now = datetime.datetime.now()

# Display the current date and time stored in 'now'
print(now)

# Define a lambda function 'year' to extract the year from a given datetime object 'x'
year = lambda x: x.year

# Define a lambda function 'month' to extract the month from a given datetime object 'x'
month = lambda x: x.month

# Define a lambda function 'day' to extract the day from a given datetime object 'x'
day = lambda x: x.day

# Define a lambda function 't' to extract the time from a given datetime object 'x'
t = lambda x: x.time()

# Print the year extracted from the current datetime object 'now'
print(year(now))

# Print the month extracted from the current datetime object 'now'
print(month(now))

# Print the day extracted from the current datetime object 'now'
print(day(now))

# Print the time extracted from the current datetime object 'now'
print(t(now))
