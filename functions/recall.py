def student(name, age):
    print(name)
    print(age)
student('singham', 22)
student(22,'singham')
student(age=22, name= 'singham')




# def greet(name='Student'):
#     print("hello",name)
# greet('saurabh')
# greet()


# def student(name='student', age='20',course='Btech'):
#     print(name)
#     print(age)
#     print(course)
# student('Saurabh', 21)


# def greet():
#     name = input("Enter the name ")
#     return name
# print(name = greet())


def Sum(*numbers):
    return sum(numbers)
print(Sum(1,2))
print(Sum(1,2,4))
print(Sum(1,2,7,9))
print(Sum(1,2,6,9,0,5))

def Print(*numbers):
    return (numbers)
print(Print(1,2))
print(Print(1,2,3))
print(Print(1,3,7,8))
print(Print(1,6,7,8,9))


def Student(**Details):
    print(Details)
Student(name="Saurabh Pandey", age="20", Sem="5th", Nationality="Indian")
