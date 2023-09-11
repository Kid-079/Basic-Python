class Product():
	name = 'name_product'   # Value on a Class

	def product1(stock):
		print("Ready")

	def product2(stock,condition):
		print(stock.name, "productName", condition)

# Main Program
A = Product()
B = Product()

# Create Product Name
A.name = "Product 1"
B.name = "Product 2"

# Show Product Name
print(A.name)
print(B.name)

# Method Check Condition product
A.product1()
A.product2("Not Ready")