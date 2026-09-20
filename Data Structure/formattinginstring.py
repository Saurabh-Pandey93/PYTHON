a = 5
b = 22
sum = a+b

#normal formatting
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a, b, sum))


#index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum))


#value based formatting   
print("{a}values of vars {a} & {b}".format(a = 5, b = 22))