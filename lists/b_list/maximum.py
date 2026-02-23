# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(list):
    large_num = 0
    for num in list:
        if num > large_num:
            large_num = num
    print(large_num)

maximum([5, 6, 3, 7])
maximum([17, 15, 19, 11, 2])
maximum([])

