# Access Tuple
data = ("Enjoy","RELAX","Mistake","Pretty","Proud")
print(data[1])
print(data[-1])

# Change Tuple
data = ("Enjoy","RELAX","Mistake","Pretty","Proud")
changeData = list(data)
changeData[1] = "Great"
data = tuple(changeData)

print(data)

# Unpack Tuple
data = ("Enjoy","RELAX","Mistake","Pretty","Proud")
(A,B,C,D,E) = data

print(A)
print(B)
print(C)
print(D)
print(E)
