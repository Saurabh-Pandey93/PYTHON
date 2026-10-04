list = [1,23,56,7,4,7,8]
even = [x for x in list if x%2 == 0]
odd = [x for x in list if x%2 != 0]
print(even,odd)