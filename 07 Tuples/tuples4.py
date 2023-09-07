import timeit

data_list = timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]",number=1000)
data_tuple = timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]",number=1000)

print("Time Process List : ", data_list)
print("Time Process Tuple : ", data_tuple)