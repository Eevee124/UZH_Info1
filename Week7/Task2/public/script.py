#!/usr/bin/env python3

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

    invalid = ["IIII", "XXXX" "CCCC", "VV", "LL", "DD", "VX"]

    for char in roman:
        if char not in roman_single_digits or roman in invalid:
            raise Warning("Invalid Input")


    res = 0
    i = 0
 
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

print(convert_roman_to_int("IIII"))


# The following lines calls the function and prints the return
# value to the Console.
i = convert_roman_to_int("IIMX")
print(i)

