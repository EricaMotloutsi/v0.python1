# Write a function `longer` that accepts two strings.
# Return the string that is longer.
# If both strings have the same length, return the first string.

print(longer("drum", "piranha"))       # "piranha"
print(longer("basket", "fork"))        # "basket"
print(longer("flannel", "sustainable"))# "sustainable"
print(longer("disrupt", "ability"))    # "disrupt"
print(longer("bird", "shoe"))          # "bird"

def longer(string1,string2):
    if string1>=string2:
        return string1
    else:
        return string2
print(longer("drum", "piranha"))       # "piranha"
print(longer("basket", "fork"))        # "basket"
print(longer("flannel", "sustainable"))# "sustainable"
print(longer("disrupt", "ability"))    # "disrupt"
print(longer("bird", "shoe")) 
