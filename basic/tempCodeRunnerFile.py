

# user = str(input("enter your name:  "))
# print("hi", user)
# print(type(user))

# age = float(input("enter age: "))
# print(type(age))



# name = input("Enter your name:")
# age = input("Enter your age:")
# print(f"my name is {name} and age is {age}")


# diameter = float(input("Enter the diameter:"))
# radius = diameter/2
# pi = 3.14
# area = pi*radius**2
# print(area)
# print(type(area))

# diameter = float(input("Enter the diameter:"))
# radius = diameter/2
# pi = 3.14
# volume = 4/3*pi*radius**3
# print("volume of the sphere is:", volume)

# ATM_Pin = int(input("Enter  PIN"))
# Pin = 1234
# if Pin != ATM_Pin :
#     print("Incorrect PIN")

# else:
#     print("Correct Pin")



# marks = int(input("Marks of student:"))
# if marks >= 40:
#     print("eligible")

# else:
#      print("not eligible")


# marks = int(input("Enter Marks:"))
# if marks >= 90:
#     print("A")
# elif marks >= 80:
#     print("B")
# elif marks >= 70:
#     print("C")
# elif marks >= 60:
#     print("D")
# elif marks >= 50:
#     print("E")
# else:
#     print("Failed")


# Me = "P"
# friend  = "A"
# Bestfriend = "B"
# name = str(input("Enter Name"))
# if name == Me:
#     print("It's me")
# elif name == friend:
#     print("Saviour")
# elif name == Bestfriend:
#     print("GEM")

# else:
#     print("UNKNOWN")
   

# Day = str(input("Enter the Name of day: "))
# if Day == "Monday"  or Day == "Tuesday" or Day == "Wednesday" or Day == "Thursday" or Day == "Friday":
#     print("The Day is working Day")

# elif Day == "Saturday" or Day == "Sunday":
#     print("Weekend")

# else:
#     print("Invalid day")




# Age = int(input("Age of the Person : "))


# access = True

# if Age >= 18 and access == True:
#     print("The user is allowed to access")
# else:
#     print("You're not allowed to access")


# age = int(input("Enter the age of candidate :"))
# has_voter_id = False
# if age >= 18 :
#     if has_voter_id == True:
#         print(" can vote ")
#     else:
#         print("Get your voter id card")

# else:
#     print("you're not eligible")


# num1 = int(input("Enter the  1st number :"))
# num2 = int(input("Enter the  2nd number :"))
# num3 = int(input("Enter the  3rd number :"))

# if num1>num2:
#     if num1>num3:
#         print("The highest value is : " ,num1)
#     else:
#         print( "The highest value is :", num3)

# elif num2 > num3:
#     print("The highest value is : ", num2)

# else:
#     print("The highest value is :", num3)


# for name in range(5):
#     print("Saurabh")


# for i in range(1, 31):
#     print(i**2)

# for i in range(120,0,-12):
#     print(i)

# num = 10
# while num>1:
#     print("chup")

# Num = int(input("Enter the Number :"))
# if Num % 2 == 0:
#     print("The number is even number")

# else:
#     print("The  number is odd ")

# for num1 in range(1,6):
#     for num2 in range(1,6):
#         print(num1,num2)

#     print()

# n = 5                       
# for i in range(1,n+1):      
#      print("*" *i)          

# n = 2
# for i in range(1,11):
#     print(f"{n}*{i}={i*2}" )

# n = int(input("Enter the number :"))
# total = 0
# for i in range (1,n+1):
#     if i % 2 == 0:
#         total += i
# print(f"sum from 1 to {n} is {total}")


# name = "Saurabh"
# print(name[:])

# # slicing with steps and how to reverse strings

# text = "Python"
# reversed_text = text[::-1]
# print(reversed_text)  # Output: nohtyP   


# i = "hello"         #code, pseudocode and dry run
# reversed_str = ""
# for char in i:
#     reversed_str = char + reversed_str
# print(reversed_str)

# name = "   Saurabh   "
# print(name.strip())

# oo = name
# print(oo)

# phrase = "hi how are you dear"
# phrase1 = "I'm doing great"
# print(phrase.find("dear"))
# print(phrase.count("h"))
# phrase1 = phrase.replace("dear","deer")
# print(phrase1)

# list = ["10", 10.0, 'ten', 10]
# print(list[2][1])

# tuple = (80, 90, 78, 49, 69)
# for num in tuple:
#     total = 0
# for num in tuple:
#     total += num
# print(total)  

# Username, following, follower, posts= ("Saurabh_Pandey", 78, 79, 0)
# print(Username)
# print(follower)
# print(following)
# print(posts)

# userpro = ["abc", 45, 78, 0]
# username, follower, following, posts = userpro
# print("username :", username)
# print("follower :", follower)
# print("following :", following)
# print("posts :", posts)

# set = {1,1,1,2,3,3,4,5,5,5,6,7,575}
# print(set)
# for i in set:
#     print(i)

# set2 = {1,1,7,9,2,3,3,7,8,6,5,6,3,4,4}
# print(set2)            # how to take input in list and tuple and set read about unordered set,  STL in  python 
# set2.add("saurabh")
# print(set2)
# set2.remove(3)
# print(set2)
# set2.discard(88)
# print(set2)


# set = {10,20,10,30,20,40,50}
# print(sum(set)) 

# set1 = {90, 85, 75, 93, 46}
# avg = sum(set1)/len(set1)
# print("Average of the Marks :",avg)

total = 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))

print(f"Sum: {total}")   