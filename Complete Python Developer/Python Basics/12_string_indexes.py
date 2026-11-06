# str -> ordered sequence of characters

selfish = "01234567"

# [start:stop]
print(selfish[0:2])

# [start:stop:step]
print(selfish[0:8:2])

# [1:] -> this says start at 1 and then go all the way to the end
print(selfish[1:])

# [:5] -> this says start at 5 and then go all the way to the beginning
print(selfish[1:])

# [::1] -> start at 0 ends at whenever the string ends, and steps over 1
print(selfish[::1])

# [-1] -> last element of string
print(selfish[-1])

# [::-1] -> it starts from the last element in string and prints backwards -> common reverse operation
print(selfish[::-1])
