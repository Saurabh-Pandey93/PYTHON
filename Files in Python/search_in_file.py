data = True
line = 1
word = "Saurabh"

with open("sample.txt", "r") as f:
    while data:
       data = f.readline()
       if("Saurabh" in data):
           print("word found")
           break
       
       line += 1

    