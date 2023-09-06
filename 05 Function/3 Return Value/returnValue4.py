# Function with return value and Multiple Argumen
#3
def sum(value1,value2):
	total = value1 + value2
	print(value1,'+',value2,'=',total)
	return total   # use for return number, list, string

def minus(value1,value2):
	total = value1 - value2
	print(value1,'-',value2,'=',total)
	return total

a = minus(1,sum(1,2))
print(a)
