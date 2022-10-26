#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):

    if a == [] or b == []:
        return []

    if len(a) < len(b):
        lengthen(a, len(b))

    elif len(b) < len(a):
        lengthen(b, len(a))

    return list(zip(a, b))

def lengthen(a, length):
    while len(a) < length:
        a.append(a[-1])
    return a

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([1, 1, 6, 8, 9], [2, 3, 4]))
