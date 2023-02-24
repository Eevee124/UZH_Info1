#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None
    
    f = open(path, 'r')

    contents = f.read()
    print(contents)

    return -1


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("C:\Users\evang\OneDrive\Desktop\UZH\Informatik_I_UZH_folder\UZH_Exercises\Week5\Task_6\public\my_grades.txt"))

