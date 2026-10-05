dict = {
    "stud1" : 55,
    "stud2" : 66,
    "stud3"  : 76,
    "stud4" : 97
}
print(dict)

highest = 0
top = " "

for name, marks in dict.items():
    if marks > highest:
        highest = marks
        top = name

print(f"{top} scored {highest}")