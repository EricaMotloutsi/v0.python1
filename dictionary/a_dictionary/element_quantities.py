def element_quantities(dictionary):
    ans_list = []
    for key, value in dictionary.items():
        for i in range(value):
            ans_list.append(key)
    return ans_list




quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']

