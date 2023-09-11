# Class
class Product():
	name = "name_product"   # .. ( 1 )
	total_value = 0         # .. ( 2 )

	def __init__(self,input_id,input_name):
		self.id = input_id       # Public
		self.name = input_name   # Public
		
		# .. ( 2 )
		Product.total_value += 1

# Main Program
# .. ( 1 )
Product.name = "Product 1"
print(Product.name)
Product.name = "Product 2"
print(Product.name)
print("\n")

# .. ( 2 )

A = Product(123, "Product 1")
B = Product(456, "Product 2")
C = Product(789, "Product 3")
D = Product(0123, "Product 4")

print(Product.total_value)

# .. ( 3 )
A.name = "ABCDE" 
B.name = "abcde" 
print(A.name)
print(B.name)