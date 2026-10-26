def add_list():
    numbers = input("Enter numbers separated by spaces: ")
    my_list = list(map(int, numbers.split()))

    total = sum(my_list)

    return total

result = add_list()
print("Sum of list elements:", result)