# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.
def no_ohs(string):
    for ch in string:
        if ch != "o":
            print(ch)


# Example:
no_ohs("code")
# d
# e

