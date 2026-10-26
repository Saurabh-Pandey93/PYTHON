def even_list(numbers):
    list_ = list(map(int, numbers.split()))

    even = []

    for num in list_:
        if num % 2 == 0:
            even.append(num)

    return even

numbers = input("Enter the list elements with spaces: ") 

even_numbers = even_list(numbers)
print(even_numbers)
print(len(even_numbers))