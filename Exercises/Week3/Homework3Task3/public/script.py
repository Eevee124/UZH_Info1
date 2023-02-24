#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
plain_text = "...$%@#{[]ZAazyX"
shift_by = 121

# perform a ROTn encoding
def rot_n():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    temp = 0
    real_shift = shift_by % 26
    encoded = ""

    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            temp = ord(plain_text[i]) + real_shift
            if (plain_text[i].islower() and temp > 122) or (plain_text[i].isupper() and temp > 90):
              temp -= 26
              #  temp -= temp % 90
            encoded += chr(temp)
        else: 
            encoded += plain_text[i]
    print(plain_text)
    print(encoded)

    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())

