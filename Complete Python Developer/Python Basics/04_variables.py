# Variables naming best practices:
# - snake_case
# - start with lowercase or underscore
# - letters, numbers, underscores
# - case sensitive
# - don't overwrite keywords

user_iq = 190
_user_iq = 190  # underscore in python signifies that the variable is private

# constants -> constants are variables that cannot be changed over time
# best practice for constant variables is to name variables all in uppercase
PI = 3.14

# tuple unpacking ( python term, also known as destructuring in javascript )
# it's a way of declaring multiple values at once
a, b, c = 1, 2, 3

first, *rest = "hello"  # first = "h" | rest = ['e', 'l', 'l', 'o']
