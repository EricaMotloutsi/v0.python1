# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'
def bleep_vowels(text):
    new_str = ""
    for ch in text:
        if ch in "aeiou":
            new_str = new_str + ""
        else:
            new_str = new_str + ch 
    print(new_str)


bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'

