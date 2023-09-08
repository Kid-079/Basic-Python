# Dictionaries
# data = {key:value,key:value} <- Key -> Keyword

data1 = {"ID":123,
		 "Name": "Salaman",
		 "Job": "Student",
		 "Status Member": "None"
		}

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
		 "Status Member": "None"
		}

datalist = {123:data1, 456:data2}

print(datalist[456])


# Insert Dictionary to the list
# Create dictionary become database who can access