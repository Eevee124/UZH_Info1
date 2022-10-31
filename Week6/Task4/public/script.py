#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    print(data)
    if len(data) == 0:
        return ((), [])
    if len(data[0]) == 0:
        return ((), [()])

    for i in range(len(data)):
        data[i] = dict(sorted(data[i], key=data[i].get))
    keytupe = tuple(data[0].keys())

    values = []
    for i in range(len(data)):
        values += [tuple(data[i].values())]

    return (keytupe, values)

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data1 = [{}]
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 5, "c": 7, "b": 8}
]
print(compress(data))