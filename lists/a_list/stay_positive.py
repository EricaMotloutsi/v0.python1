def stay_positive(numbers):
    new_list = []
    for item in numbers:
        if item > 0:
            new_list.append(item)
    print(new_list)

stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
stay_positive([-11, -30]) #-> []
