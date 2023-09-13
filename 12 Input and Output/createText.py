# Input Output File

"""
w  = Write Mode
r  = Read Only Mode
a  = Appending Mode
r+ = Write and Read Mode
"""

# Create File Text
file = open("TEXT1.txt",'w')

file.write("This is Text 1")
file.write("\nThis is Text 2")
file.write("\nThis is Text 3")
file.write("\nThis is Text 4")

file.close()


