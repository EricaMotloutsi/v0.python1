def pair_print(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            print(list[i], list[j])

pair_print(["artichoke", "broccoli", "carrot", "daikon"])
