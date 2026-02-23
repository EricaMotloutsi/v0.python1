# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

def choose_divisible(lst, num):
    ans_list = []
    for n in lst:
        if n % num == 0:
            ans_list.append(n)
    print(ans_list)


choose_divisible([40, 7, 22, 20, 24], 4)

choose_divisible([9, 33, 8, 17], 3)

choose_divisible([4, 25, 1000], 10)

