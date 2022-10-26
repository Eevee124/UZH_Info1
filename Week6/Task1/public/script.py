#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 100

# build a string 
def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""
    if h == 0:
        return s
    # Enter your code here
    # use nested loops and the range() function
    for i in range(1, h + 2):
        for j in range(1, i):
            s += str(j) + '*'
        s = s[:-1] + "\n"
    strings = s.split("\n")
    strings = strings[1:-1]

    for i in range(len(strings) - 2, -1, -1):
        s += strings[i] + "\n"
    
    print(s[:-1].count("\n"))

    # You don't need to change the following line.
    # It simply returns the string created above.
    return s[:-1]

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



