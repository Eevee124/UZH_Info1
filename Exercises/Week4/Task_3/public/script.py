#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    # implement this function
    return abs(a)

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    # implement this function
    if a < 0:
        a = absolute_value(a)
    if b < 0:
        b = absolute_value(b)

    if a == 0 and b == 0:
        return None
    if a == 0 or b == 0:
        return a if b == 0 else b
    if a < b:
        return gcd(a, b % a)
    else:
        return gcd(a % b, b )

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = -1000000000000000010
b = -100000000000000000
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")

