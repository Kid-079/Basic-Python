class Product():
	name = 'name_product'   # Value on a Class

	def product1(stock):
		stock = 0
		if stock > 0:
			print(stock, "Ready")
		else:
			print(stock, "Not Ready")


	def product2(stock,condition):
		stock = 1
		if stock > 0:
			print(stock, condition)
		else:
			print(stock, "Not Ready")

# Main Program
A = Product()
B = Product()

# Create Product Name
# 1
A.name = "Product 1"
# 2
B.name = "Product 2"

# Show Product Name
print(A.name)
print(B.name)

# Method Check Condition product
A.product1()
A.product2("Ready")
