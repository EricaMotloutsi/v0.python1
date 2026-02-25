def max_object_value(obj):
    ans_k = ""
    ans_v = 0
    for key,value in obj.items():
        if value > ans_v:
            ans_v = value 
            ans_k = key 
    return[ans_k,ans_v]



print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))

# ['rambutan', 13]