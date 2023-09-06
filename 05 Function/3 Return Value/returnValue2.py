# Function with return value and Multiple Argumen
#1
def sum(value1,value2):
	total = value1 + value2
	print(value1,'+',value2,'=',total)
	return [total,1,2,3]   # use for return number, list, string

def minus(value1,value2):
	total = value1 - value2
	print(value1,'-',value2,'=',total)
	return [total,1,2,3] 

a = sum(1,2)
b = minus(1,2)
print(a)
print(b)
print()