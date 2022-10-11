#!/usr/bin/env python3

import os

def absolute_value(a):
    a = abs(a)
    return a

def gcd(a, b):

    """
    Use the euclidean algorithm in a recursive way to get the gcd of 2 numbers:

        - Step 1: divide a/b
        - Step 2: divide divisor from step 1 by a%b
        - Step 3: repeat until a%b == 0, if reached the gcd is b (last divisor)     
    """

    if a < 0:
        a = absolute_value(a)
    if b < 0:
        b = absolute_value(b)
    if a == 0 and b == 0:
        return None
    if a == 0:
        return b
    if b == 0:
        return a
    
    #anchor - set gcd to b because the divisor of the last division (no rest) is the biggest of a and b
    if a % b == 0:
        return b

    #calling gcd again with b as the new a and a%b as the new b
    return gcd(b, a%b)

a = 26
b = 13
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")

