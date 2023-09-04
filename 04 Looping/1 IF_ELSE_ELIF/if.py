# Loop IF
# 1 
A = 75

if A == 75:
	print("Value : ", A)
if A == 80:
	print("Value : ", A)

print("\n")

#2 
B = 80
C = 75

if B == 80:
	print("Value : ", B)
	print("Step 1")
	if C == 75:
		print("Value : ", C)
		print("Step 2")

print("\n")

#3 
B = 80
C = 70

if B == 80:
	print("Value : ", B)
	print("Step 1")
	if C == 75:
		print("Value : ", C)
		print("Step 2")

print("\n")

#4no
B = 50
C = 75

if B == 80:
	print("Value : ", B)
	print("Step 1")
	if C == 75:
		print("Value : ", C)
		print("Step 2")

# NOTED :
# Example #2 : Value Step 1 and 2 is enough, can Process Step 1 and 2
# Example #3 : Value Step 2 not enough, cannot Process Step 2
# Example #4 : Value Step 1 not enough, so automaticaly cannot process step 2
