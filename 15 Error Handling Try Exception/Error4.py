print("Create a Input Number")

# A = int(input("Insert Number : "))

while True:
	try:
		A = int(input("Insert a Number 1 : ")) # Integer
		B = int(input("Insert a Number 2 : "))
		total = A/B
		break

	except ValueError:
		print("Please Insert a Number... ")
	except ZeroDivisionError:
		print("Value is 0, choose another number\n")
	except ImportError:
		print ("No Module, Import Error")
	except Exception as error:
		print(error)

print("Congratulations, you insert a number: ", total)


# Type of Exception Errors
# 1. IOError
# 2. ImportError
# 3. ValueError
# 4. Division by zero
# 5. KeyboardInterupted
# 6. EOFError