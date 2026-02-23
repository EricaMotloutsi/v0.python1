# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

def alternating_caps(sentence):
    list_words= sentence.split(" ")
    ans_list = []
    for i in range(len(list_words)):
        if i % 2 ==0:
            ans_list.append(list_words[i].lower())
        else: 
            ans_list.append(list_words[i].upper())
    print(ans_list)

#Example:
alternating_caps("take them to school") #-> 'take THEM to SCHOOL'

alternating_caps("What did ThEy EAT before?") #-> 'what DID they EAT before?'

