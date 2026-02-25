# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# You can assume the sentence contains at least one word.
# If there is a tie, return the word that appears first in the sentence.



def most_letter_word(sentence, char):
    dictionary = {}
    list = sentence.split(" ")
    for word in list:
        char_count= word.count(char)
        dictionary[word] = char_count
    val = 0
    key = ""
    for k, v in dictionary.items():
        if v >= val:
            val = v
            key = k
        elif v == val:
            continue
    return key 



print(most_letter_word(
'she received an award for excellence in science','e'
))# 'excellence'

print(most_letter_word(
'she received an award for excellence in science','a'
))# 'award'

print(most_letter_word(
'I hope sophomore year comes soon','o'
))# 'sophomore'

print(most_letter_word(
'I hope sophomore year comes soon','s'
))# 'sophomore'