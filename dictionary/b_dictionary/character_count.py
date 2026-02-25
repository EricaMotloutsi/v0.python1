
def character_count(str):
    ans_dic = {}
    for ch in str:
        if ch in ans_dic:
            ans_dic[ch] += 1
        else:
            ans_dic[ch] = 1
    return ans_dic





print(character_count("evening"))
# { 'e': 2, 'v': 1, 'n': 2, 'i': 1, 'g': 1 }

print(character_count("mississippi"))
# { 'm': 1, 'i': 4, 's': 4, 'p': 2 }

print(character_count("chili"))
# { 'c': 1, 'h': 1, 'i': 2, 'l': 1 }

