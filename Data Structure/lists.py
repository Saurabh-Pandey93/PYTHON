nums = [1, 2, 3, 5]
 
nums.append(7)
print(nums)

nums.insert(6,10)
print(nums)

nums.sort()
print(nums)

nums.reverse()
print(nums)


numbers = [ 1, 2, 3, 4, 5, 6]

x = 5
idx = 0 
for val in numbers:
    if(val == x):
        print(f"{x} found at idx={idx}")
        break
    idx += 1