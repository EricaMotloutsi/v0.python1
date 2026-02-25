
def double_vowel(str):
    ans_str = ""
    for ch in str:
        if ch in "aeiou":
            ans_str = ans_str + ch + ch
        else:
            ans_str += ch
    return ans_str


print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'

