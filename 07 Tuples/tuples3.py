import sys

# Tuples is immutabel ordered group of items or elements
# 1
print("Data 1")
data_list = [1,2,3,4,5,"Enjoy","Relax","Pretty",True]
data_tuple = [1,2,3,4,5,"Proud","Mistake","Great",False]

print(data_list)
print(data_tuple)

size_datalist = sys.getsizeof(data_list)
size_datatuple = sys.getsizeof(data_list)

print("Memory Size data list : ", size_datalist)
print("Memory Size data tuple : ", size_datatuple)
print("===========================================")
# 2
print("Data 2")
data_list = [0,1,2,3,4,5,6,7,8,9,"Enjoy","Great","Proud",False]
data_tuple = [0,1,2,3,4,5,6,7,8,9,"Relax","Pretty","Mistake",True]

print(data_list)
print(data_tuple)

size_datalist = sys.getsizeof(data_list)
size_datatuple = sys.getsizeof(data_list)

print("Memory Size data list : ", size_datalist)
print("Memory Size data tuple : ", size_datatuple)
