# Write a function `wacky_word` that accepts two strings.
# Return a new string made from:
# - the first 3 characters of the first string
# - the last 2 characters of the second string
#
# The first string is at least 3 chars long.
# The second string is at least 2 chars long.

print(wacky_word("very", "kindly"))       # "verly"
print(wacky_word("forever", "sick"))      # "forck"
print(wacky_word("cellar", "door"))       # "celor"
print(wacky_word("bagel", "sweep"))       # "bagep"


def wacky_word(string1,string2):
    first_3 = string1[0] + string1[1] + string1[2]
    last_2 = string2[-1]+ string2[-2]
    return first_3 + last_2

print(wacky_word("very", "kindly"))       # "verly"
print(wacky_word("forever", "sick"))      # "forck"
print(wacky_word("cellar", "door"))       # "celor"
print(wacky_word("bagel", "sweep"))       # "bagep"