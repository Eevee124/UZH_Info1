#!/usr/bin/env python3x

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    for post in range(len(posts)):
        posts[post] = posts[post].split()
    #split posts into list of lists of the words in each "sentence"

    flat_posts = [word for post in posts for word in post if '#' in word]
    #turns the list of lists into just a list
    flat_posts = [ x[x.find('#'):] for x in flat_posts]
    #turning the list into a list of the words with hashtags starting from the hashtags
    flat_posts = [post.split('#') for post in flat_posts]
    #removing the hashtags and splitting each word with a hashtag into empty strings and words
    flat_posts = [item for sublist in flat_posts for item in sublist]
    #turning new list of lists into just a list once again

    while '' in flat_posts:
        flat_posts.remove('')
    #remove all of the empty strings
    print(flat_posts)
    for index, tag in enumerate(flat_posts):     
        for i, letter in enumerate(tag):
            if not letter.isalnum():
                flat_posts[index] = tag[:i]
    #checks if the letter contains a non alphanumeric character and if it does it terminates the word at that character
    print(flat_posts)
    flat_posts = [word for word in flat_posts if word[0].isalpha()]
    #only accepts words which start with a letter
    print(flat_posts)

    d = {}
    for post in flat_posts:
        d[post] = 0
    #initializing a dictionary where all values are 0 with the keys from our post

    for post in flat_posts:
        if post in d:
            d[post] += 1
    #filling up dictionary with incrementing values whenever the key appears in my array

    return d

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = []
print(analyze(posts))
