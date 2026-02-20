#Write a function that checks if a string is a palindrome (same forward & backward).
print(is_palindrome("level"))          # True
print(is_palindrome("Race car"))       # True
print(is_palindrome("python"))         # False


def is_palindrome(string):
    # Remove spaces and make lowercase
    cleaned = string.replace(" ", "").lower()
    # Check if it reads the same backward
    return cleaned == cleaned[::-1]


# Test cases
print(is_palindrome("level"))          # True
print(is_palindrome("Race car"))       # True
print(is_palindrome("python"))         # False
