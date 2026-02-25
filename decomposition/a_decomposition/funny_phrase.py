
def funny_phrase(sentence):
    list = sentence.split(" ")
    ans_list = []
    for i in range(len(list)):
        if i %2 ==0:
            ans_list.append(list[i])
        else:
            double_word = double_vowel(list[i])
            ans_list.append(double_word)
    return ans_list


def double_vowel(str):
    ans_str = ""
    for ch in str:
        if ch in "aeiou":
            ans_str = ans_str + ch + ch
        else:
            ans_str += ch
    return ans_str

print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'

