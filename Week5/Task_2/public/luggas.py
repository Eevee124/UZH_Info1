def invert(d):
    b = {}
    for key in d:
        b[d[key]] = b.get(d[key], []) + [key]

    return b

    """
    d2 = {}
    for i in d:
        if d[i] not in d2:
            new_key = d[i]
            d2[new_key] = [i]

        else:
            key_list = list(d2.keys())
            new_key_index = key_list.index(d[i])
            d2[new_key_index + 1].append(i)

    return d2
    """


print(invert({"b":5, "a":5, "c":5}))

#Edgecases:
# print(invert({"b":5, "a":5, "c":5}))                \\ {5:["b", "a", "c"]}
# print(invert({"b":5, "a":1, "c":2, "d":1, "e":5}))  \\ {1:["a", "d"], 2:["c"], 5:["b", "e"]}
# print(invert({"b":1, "a":2, "c":1}))                \\ {1:["b", "c"], 2:["a"]}
#print(invert({"b":1, "a":1, "c":3}))                 \\ {1:["a", "b"], 3:["c"]}