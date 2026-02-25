# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

def shorten_long_words(sentence):
    words_list = sentence.split(" ")
    ans_list = []
    for word in words_list:
        if len(word)<=4:
            ans_list.append(word)
        else:
            ans = remove_vowels(word)
            ans_list.append(ans)
    return " ".join(ans_list)


def remove_vowels(string):
    new_string = ""
    for ch in string:
        if ch not in "aeiou":
            new_string += ch
    return new_string

    

print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'
