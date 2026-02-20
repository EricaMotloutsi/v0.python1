# Write a function `one_or_none` that accepts two boolean values.
# Return True if EXACTLY ONE of them is True.
# Return False if both are True OR both are False.

print(one_or_none(False, False))   # False
print(one_or_none(True, False))    # True
print(one_or_none(False, True))    # True
print(one_or_none(True, True))     # False

def one_or_none(boolen1,boolen2):
    if boolen1 != boolen2:
        return True 
    else:
        False

print(one_or_none(True, False))    # True
print(one_or_none(False, True))    # True
print(one_or_none(True, True))