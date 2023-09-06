# Function with return value and Multiple Argumen
#2
def sum(value1,value2):
	total = value1 + value2
	print(value1,'+',value2,'=',total)
	return total   # use for return number, list, string

def minus(value1,value2):
	total = value1 - value2
	print(value1,'-',value2,'=',total)
	return total

a = sum(1,2)
b = minus(1,a)
print(a)
print(b)
print()