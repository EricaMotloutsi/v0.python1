# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.
def reverse_array(arr):
    new_list = []
    for i in range(len(arr) -1,-1, -1):
        new_list.append(arr[i])
    print(new_list)


reverse_array(["zero", "one", "two", "three"]) #-> ['three', 'two', 'one', 'zero'] [8, 1, 7]
reverse_array([7, 1, 8]) #-> [8, 1, 7]

