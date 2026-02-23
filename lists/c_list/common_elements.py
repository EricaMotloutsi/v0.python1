# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.

def common_elements(arr1, arr2):
    ans_list = []
    for el in arr1:
        if el in arr2:
            ans_list.append(el)
    print(ans_list)

common_elements(["a", "c", "d", "b"], ["b", "a", "y"])

common_elements([4, 7], [32, 7, 1, 4])