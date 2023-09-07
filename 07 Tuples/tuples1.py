# List 
even = [1,3,5,7,9]

# Tuple ---> Tuple not support append, item assignment and remove
odd = [2,4,6,8,10]

print(type(even))
print(type(odd))

print(even)
print(odd)


# Difference List and Tuple
even[1] = 10
odd[2] = 20  # Tuple Not Support item Assignment

# dir ---> Check Function
print(dir(even))
print(dir(odd))