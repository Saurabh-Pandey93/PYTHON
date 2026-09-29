# function help to organize code into logical blocks that perform specific tasks. 
def f1():
    print("Hello")

f1()
f1()

def f2(name):
    print(name)
f2("Saurabh")
f2("Virat")

def square(x):
    return x**2
x = float(input("Enter the number :"))
out = square(x)
print("The square of ", x, "is", out)