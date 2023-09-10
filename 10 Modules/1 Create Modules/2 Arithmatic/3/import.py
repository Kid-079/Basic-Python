# Import from Library Python
import math
# Import from Module
import folder

# Import Module
from folder import mathematic 
from folder import formula
# Import Specific formula from Module
from folder import sum
from folder import minus 

# Mathematic
# 1 From Module
mathematic.sum(1,5)
mathematic.minus(10,2)

# 2 From Specific Module
folder.sum(1,2)
sum(1,5)
minus(1,5)
print("\n")

# Formula
# 1 From Module
A = folder.A(10,20,3)
print(A)

B = folder.B(10,20)
print(B)

C = folder.C(20,4)
print(C)

# 2 From Speciifc Module
formula.B(20,5)
print(B)
print("\n")

# Import From Library
print(math.cos(3.14))

