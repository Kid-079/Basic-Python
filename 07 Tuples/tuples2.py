# Access Tuple
data = ("A","B","C","D","E")
print(data[1])
print(data[-1])

# Change Tuple
data = ("A","B","C","D","E")
changeData = list(data)
changeData[1] = "Abc"
data = tuple(changeData)

print(data)

# Unpack Tuple
data = ("Abc","ABC","abc")
(A,B,C) = data

print(A)
print(B)
print(C)