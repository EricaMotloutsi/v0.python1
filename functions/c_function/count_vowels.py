#Write `count_vowels(text)`
#Return how many vowels are in the string.

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3

def count_vowels(string):
    count = 0
    vowels = "aeiou"

    for char in string.lower():
        if char in vowels:
            count += 1

    return count


print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3