# Nested Loop
String = ['Abc','ABC']
Char = ['A','B','C','D','E']
Number = [1,2,3,4,5,6]

Array = [String,Char,Number]
print(Array)

print("\n")

for data in Array:
	print(data)
	for bundle in data:
		print(bundle)