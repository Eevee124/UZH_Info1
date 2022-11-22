#!/usr/bin/env python3
import re
# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def convert_roman_to_int(roman):

    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    invalid = ["IIII", "XXXX" "CCCC", "VV", "LL", "DD", "XM", "IM", "IVIV", "IXIX",  "VX", "VL", "VC", "VD", "VM", "LC", "LD", "LM", "DM",  "IL", "IC", "ID", "IM", "XD", "XM"]

    for char in roman:
        if char not in roman_single_digits or roman in invalid:
            raise Warning("Invalid Input")

    x = re.search("^M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman)
    
    if x == None:
        raise Warning("Invalid Input")

    res = 0
    i = 0
    appearance = []

    while (i < len(roman)):
 
        # Getting value of symbol s[i]
        s1 = roman_single_digits[roman[i]]
 
        if (i + 1 < len(roman)):
 
            # Getting value of symbol s[i + 1]
            s2 = roman_single_digits[roman[i + 1]]
 
            
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2


        else:
            res = res + s1
            i = i + 1

    return res