# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).

def remove_vowels(string):
    new_string = ""
    for ch in string:
        if ch not in "aeiou":
            new_string += ch 
    return new_string
print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'



