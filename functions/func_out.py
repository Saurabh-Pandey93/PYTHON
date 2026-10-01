# def greet(name):
#     print("hello",name)

# username = input("Enter Name")
# greet(username)


def userprofile(username='username', follower='0', following='90', post='5'):
    print(username)
    print(follower)
    print(following)
    print(post)
userprofile("saurabh", 22, 44)
userprofile("saurabh",33)
userprofile("saurabh")


def calculate(numbers):
    return sum (numbers)
list = [20,17,19,20,20,19]
print(calculate(list)) 


def calculator(numbers):
    sum = 0 
    for num in numbers:
        sum += num
    return sum
marks_l = [20,17,19,20,20,19]
marks_t = (20,17,19,20,20,19)
marks_s = {20,17,19,20,20,19}
print(calculator(marks_l))
print(calculator(marks_s))
print(calculator(marks_t))



def print_odd_even(numbers):
    even = [i for i in numbers if i % 2 == 0]
    odd  = [i for i in numbers if i % 2 != 0]

    print("Even:", even)
    print("Odd:", odd)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_even(list1)   


x  =  10
def local():
    x = 5
    
    print(x)
local()
print(x)