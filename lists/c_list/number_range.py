# Write a function `number_range(min_val, max_val, step)` that accepts three numbers as arguments.
# The function should return a list of numbers starting from min_val to max_val (inclusive),
# incremented by step

def number_range(min_val, max_val, step):
    ans_list = []
    for num in range(min_val, max_val+1,step):
        ans_list.append(num)
    print(ans_list)

number_range(10,40,5)

number_range(14,24,3)

number_range(8,35,6)
