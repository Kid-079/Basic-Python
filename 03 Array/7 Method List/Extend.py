Array1 = [10,20,30,40,50,60,70]
Array2 = [0,1,2,3,4,5,6]

# Create Multidimensional List
Data = [Array1,Array2]
print(Data)

# Append  --> Add Elements at the end of the lists
Data2 = [1,2,3]
Data.append(Data2)
Data.append(["A","B","C"])
Data.append(100)
print(Data)

# Extend  --> Add Elements of a list, to the end of current list
Data3 = ['a','b','c']
Data.extend(Data3)
print(Data)

