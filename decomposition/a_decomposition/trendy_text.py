# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# You can assume the sentence contains at least one word.
# If there is a tie, return the word that appears first in the sentence.


def trendy_text(sentence):
    words = sentence.split(" ")
    ans_list = []
    for word in words:
        ans = remove_last_vowel(word)
        ans_list.append(ans)
    return " ".join(ans_list)
    
def remove_last_vowel(str):
    for i in range(len(str)-1, -1, -1):
        ch = str[i]
        if ch in "aeiou":
            first = str[0:i]
            second = str[i+1:]
            return first + second
    return str 

print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'

