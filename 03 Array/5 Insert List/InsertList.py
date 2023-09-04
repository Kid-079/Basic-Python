# Insert List to New Variable

Array1 = [10,20,30,40,50,60,70]
Array2 = [0,1,2,3,4,5,6]

# Add List
Data = Array1 + Array2
print(Data)

# Insert List
a = Data[:]     # [:] --> Insert all file from data to a
# a[5] = 100      # insert/change Specific indeks
# a[6] = 10 
# a[10] = 40

print(a)