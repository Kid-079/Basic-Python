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

# Copy Dictionaries to New Dictionaries
print('Data 3 :')
newData = data1.copy()
print(newData)
print("\n")

# Change Values 
print('Change Values :')
newData["Name"] = "Semir Khan"
print(newData)
print("\n")

# Add Data 
print('Add Data to Data 3 :')
newData["Hobby"] = "Sports"
print(newData)
