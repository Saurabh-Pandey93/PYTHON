def list_max():
    numbers = input("Enter numbers separated by spaces: ")
    list_ = list(map(int, numbers.split()))

    largest = list_[0]

    for num in list_:
        if num > largest:
            largest = num

    return largest
print(list_max())