# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.

def remove_first_vowel(string):
    for i in range(len(string)):
        if string[i] in "aeiou":
            first = string[:i]
            second = string[ i+1:]
    return first + second



print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'

