# given a list of tuples with info (info , subjects):
# list all unique subjects and the number of students enrolled in each subject.
# list students enrolled in each subject.
# create  a dictionary ( students, set of courses)

info = {
    ("naval", "math"),
    ("abhay", "pps"),
    ("chandan", "pps"),
    ("Anshu", "physics"),
    ("Saurabh", "physics"),
    ("Abhayjeet", "math"),
    ("prashant", "math")
}

unique_courses = set()

for tup in info:
    unique_courses.add(tup[1])
    
print(unique_courses)
for name,course in info:
    if(course == "pps"):
        print(name)