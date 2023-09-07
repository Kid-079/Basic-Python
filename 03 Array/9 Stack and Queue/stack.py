Data = [1,2,3,4,5,6]
print('Data Now : ', Data)

# Add New Data
Data.append(7)
print('Input : ', 7)
print('Data Now : ', Data)

Data.append(8)
print('Input : ', 8)
print('Data Now : ', Data)

# Stack or Heap --> Reduce data from behind
out = Data.pop()
print('Output : ', out)
print('Data Now : ', Data)

out = Data.pop()
print('Output : ', out)
print('Data Now : ', Data)

# Add New Data
Data.append(9)
print('Input : ', 9)
print('Data Now : ', Data)