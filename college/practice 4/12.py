def list_min():
    numbers = input("Enter numbers separated by spaces: ")
    list_ = list(map(int, numbers.split()))

    smallest = list_[0]

    for num in list_:
        if num < smallest:
            smallest = num

    return smallest

print(list_min())
