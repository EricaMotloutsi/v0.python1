# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.
def remove_capitals(text):
    ans = ""
    for ch in text:
        if ch.lower() ==ch:
            ans = ans +ch
            print(ans)

def remove_capitals(text):
    ans = ""
    for ch in text:
        if ch.islower():   # keeps only lowercase letters
            ans += ch
    return ans  # return final result




remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'

