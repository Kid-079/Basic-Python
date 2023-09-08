# Intersection and Union

even = {1,3,5,7,9}
odd = {2,4,6,8,10}
number = {0,1,2,3,4,5,6,7,8,9}


# Union
print(even | odd)
print(odd.union(even))

# Intersection
print(odd & even)
print(odd.intersection(even))
print(even.intersection(even))
print(odd.intersection(odd))
print(odd.intersection(number))

# Difference 
print(even - odd)
print(even.difference(odd))

# Symmetric Difference
print(even ^ odd)
print(even.symmetric_difference(odd))


# Intersection        --> Returns a set, the intersecction of two or more sets
# Union               --> Returns a set containing the union sets
# Difference          --> Returns the difference of two or more sets as a new set
# Symmetric Dfference --> Returns the symmetric difference of two sets as a new set