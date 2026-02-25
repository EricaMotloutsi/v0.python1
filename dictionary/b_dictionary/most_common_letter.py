
def most_common_letter(str):
    dictionary = {}
    for ch in str:
        if ch in dictionary:
            dictionary[ch] +=1
        else:
            dictionary[ch] =1
            print(dictionary)

print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'


def most_common_letter(str):
    dictionary = {}
    for ch in str:
        if ch in dictionary:
            dictionary[ch] +=1
        else:
            dictionary[ch] =1
            print(dictionary)

print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

