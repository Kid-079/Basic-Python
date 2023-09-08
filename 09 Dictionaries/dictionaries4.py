# Dictionaries
# data = {key:value,key:value} <- Key -> Keyword

data1 = {"ID":123,
		 "Name": "Salaman",
		 "Job": "Student",
		 "Status": "None"
		}
print("Data 1")
print(data1)
print(data1.keys())
print(data1["ID"]) # Access Data from Dictionary use Key
print("\n")
print(data1.values())
print(data1.items())
print("\n")

data2 = {"ID":456,
		 "Name": "Paparoti",
		 "Job": "Singer",
		 "Status": "None"
		}

print("Data 2")
print(data2)
print(data2.keys())
print(data2["ID"]) # Access Data from Dictionary use Key
print("\n")
print(data2.values())
print(data2.items())
print("\n")


datalist = {123:data1, 456:data2}

# Access Data
print('Access Data List :')
print(datalist[456])
print("\n")

# Change Values
print('Change Values :')
data2["Status"] = "A"
print(data2)
print("\n")

# Update Dictionary
print('Update Dictionaries :')
data1.update({"Job": "Teacher"})
print(data1)
print("\n")

# Add Items
print('Add Items :')
data1["Hobby"] = "Athletic"
print(data1)
print("\n")

# Remove Items
# 1 Remove Specific Items
print('Remove Specific Items :')
data2.pop("Status")
print(data2)
print("\n")

# 2 Remove last inserted items
print('Remove Last Items :')
data2.popitem()
print(data2)
print("\n")

# 3 Delete Specific Key Name
print('Delete Specific Key Name :')
del data1["Hobby"]
print(data1)
print("\n")

# 4 Clear Dictionary
print('Delete Specific Key Name :')
data1.clear()
print(data1)