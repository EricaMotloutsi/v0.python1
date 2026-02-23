# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(num):
    sum = 0
    for n in range(1, num + 1):
        sum = sum + n
    print(sum)


print(sum_up_to(4))  # 10
print(sum_up_to(5))  # 15
print(sum_up_to(2))  # 3
