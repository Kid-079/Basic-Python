# Input Output File

"""
w  = Write Mode
r  = Read Only Mode
a  = Appending Mode
r+ = Write and Read Mode
"""


# Read File Text
file2 = open("TEXT.txt",'r')

print(file2.read())
# print(file2.read(20))
# print(file2.readline())
# print(file2.readline())

file2.close()


