# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

def lengthiest_word(sentence):
    list_words = sentence.split(" ")
    length = 0
    ans_word = ""

    for word in list_words:
        if len(word) >= length:
            lenght =len(word)
            ans_word = word

    print(ans_word)

lengthiest_word("I am pretty hungry")

lengthiest_word("we should think outside of the box")

lengthiest_word("down the rabbit hole")

lengthiest_word("simmer down")