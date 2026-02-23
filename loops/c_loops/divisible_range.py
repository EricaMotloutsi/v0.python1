# Write a function `divisible_range(min_val, max_val, num)` that prints all numbers
# between min_val and max_val (exclusive) that are divisible by num.
# The function does not return a value, just prints.
def divisible_range(min,max,num):
    for n in range(min+1,max):
        if n % num ==0:
            print(n)


divisible_range(17, 40, 9)


divisible_range(10, 24,16)
# 12
# 16
# 20

