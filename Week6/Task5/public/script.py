#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    for post in range(len(posts)):
        posts[post] = posts[post].split()

    flat_posts = [word for post in posts for word in post]

    keys = []
    for word in flat_posts:
        if len(word) > 1 and '#' in word[0] and not word in keys and word[1].isalpha():
            keys.append(word)

    d = {}
    for key in keys:
        d[key] = 0

    for word in flat_posts:
        if word in keys:
            d[word] += 1
    d = dict(sorted(d.items(), key=lambda x:x[0]))
    keys = [key[1:] for key in keys]
    keys.sort()

    return dict(zip(keys, list(d.values())))    

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = ['.#c.']
print(analyze(posts))
