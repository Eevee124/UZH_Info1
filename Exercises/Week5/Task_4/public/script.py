#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    n = len(top)
    option = -1
    for num in range(1, 7):
        options = all(num in domino for domino in zip(top, bottom))
        #print(f"{num=} for {options=}")
        
        if options:
            option = num
            break

    return n - max(top.count(option), bottom.count(option)) if option != -1 else option

# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
