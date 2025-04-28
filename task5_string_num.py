is_number = lambda s: s.replace('.', '', 1).isdigit() if s.count('.') <= 1 else False
#lambda function uses isdigit() method checks if all characters in the string are digits.

"""Replacing the first occurrence of a period (.) with an empty string to handle decimal numbers.
Checking if the remaining string is composed entirely of digits.
Ensuring that there is at most one period in the string to validate proper decimal format."""


print(is_number("123"))      # True It returns True for strings like "123"
print(is_number("123.45"))   # True It returns True for strings like "123.45"
print(is_number("123.45.67"))# False Output: False. Returns False, since it an invalid floating number"
print(is_number("abc"))      # False Output: False. Returns False for strings containing non-digit characters "abc"