#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    # implement this function
    if d == {}:
        return {}

    sorted_d = sorted(d.items(), key=lambda x:x[1])

    dee = dict(sorted_d)

    keese = list(dee.values())
    val = list(dee.keys())

    values = []
    same = []

    for i in range(len(keese)):
        entered = False
        for j in range(len(keese)):
            if i != j and keese[i] == keese[j]:
                entered = True
                same.append(val[i])
            if not entered and j == len(keese) - 1:
                values.append([val[i]])
                same = []
        if entered:
            values.append(same)

    final_values = []
    final_values.append(values[0])
    final_keys = []
    final_keys.append(keese[0])

    no_dupes(final_values, values)
    no_dupes(final_keys, keese)

    if len(final_keys) == 1:
        final_values = [sorted(val)]

    return dict(zip(final_keys, final_values))

def no_dupes(a, b):
    for i in range(len(b)):
        for j in range(len(b)):
                if not (b[i] in a):
                    a.append(b[i])
    return a

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":1, "b":1, "c":3}))
