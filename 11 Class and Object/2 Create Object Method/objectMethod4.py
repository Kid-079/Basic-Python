# Class
class Product():
	name = 'name_product'
	__value = 0     # Private

	def company_name(companyName):
		print("NAME")

	def __init__(stock, input_id, input_name):    # Init --> Initialitation
		stock.id = input_id          # Public
		stock.name = input_name      # Public

	def valueProduct1(stock, input_value):
		stock.__value += input_value

	def valueProduct2(stock, input_value):
		stock.__value += input_value

	def check_condition(stock):
		if stock.__value <= 50:
			print(stock.name, 'Ready')
		else:
			print(stock.name, 'Not Ready')

# Main Program
A = Product("Product 1", 123)
B = Product("Product 2", 456)

# 1
A.valueProduct1(10)
A.check_condition()

# 2
A.valueProduct1(60)
A.check_condition()

# 3 
B.valueProduct2(50)
B.check_condition()
