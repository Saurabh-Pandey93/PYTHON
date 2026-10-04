s = input("enter the string").lower()
count = sum(1 for c in s if c in 'aeiou')
print(count)