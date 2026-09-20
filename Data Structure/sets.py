# collections of unique elements
set = {2, 2, 2, 3, 6, 3, 2, 7, 0}

set.add(11)
set.remove(3)
set.pop()

print(set)
print(type(set))
print(len(set))



s1 = {1, 2, 3, 4, 5, 6}
s2 = {7, 8, 9, 10}

print(s1.union(s2))
print(s1.intersection(s2))