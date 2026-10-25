def largest_of_3(a,b,c):
    if a > b and a > c:
        return a 
    elif a > b and b > c:
        return b
    else: 
        return c

a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))

print(largest_of_3(a,b,c))