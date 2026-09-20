Number = int(input("Enter a number: "))
digit_sum = 0
while Number != 0 :
    digit_sum += Number%10 
    Number = Number//10
print("sum of digits ", digit_sum)
    




