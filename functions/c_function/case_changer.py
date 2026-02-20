#Write a function `case_change(text, make_upper)`:

#If `make_upper` is **True**, return the string in **uppercase**
#If False, return it in **lowercase**


print(case_change("Super", True))      # SUPER
print(case_change("Super", False))     # super
print(case_change("tAmBourine", True)) # TAMBOURINE
print(case_change("tAmBourine", False))# tambourine

def case_change(string,boolen):
    if boolen:
        return string.upper()  
    else:
        return string.lower
print(case_change("Super", True))      # SUPER
print(case_change("Super", False))     # super
print(case_change("tAmBourine", True)) # TAMBOURINE
print(case_change("tAmBourine", False))# tambourine

def case_change(string, boolen):
    if boolen:
        return string.upper()
    else:
        return string.lower()

print(case_change("Super", True))      
print(case_change("Super", False))     
print(case_change("tAmBourine", True)) 
print(case_change("tAmBourine", False))