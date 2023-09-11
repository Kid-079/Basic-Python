# Class
class Product():
	name = 'name_product'

	def company_name(companyName):
		print("NAME")

	def __init__(stock, input_value, input_name):
		stock.value = input_value
		stock.name = input_name

	def product_name(stock, condition):
		print(stock.name, "nameProduct", condition)
		return


# Main Program
A = Product(123, "Product 1")
B = Product(456, "Product 2")
C = Product(789, "Product 3")

# Show Company and Product Name
A.company_name()
A.product_name("Ready")
B.product_name("Ready")
C.product_name("Ready")
print("\n")

# Modify Object
C.name = 'Product 4'
C.product_name("Ready")
print(C.value)
