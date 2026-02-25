
def letter_map(str,dic):
    ans_str =""
    for ch in str:
        if ch in dic:
            ans_str += dic[ch]
        else: 
            ans_str += ch
    return ans_str





print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'

