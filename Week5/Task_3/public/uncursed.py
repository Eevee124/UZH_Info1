from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello hello",
    "This is the WORLD",
    "hello again"
 ]

 #returns this dictionary {'hello': [0, 2], 'is': [1], 'the': [1], 'world': [0, 1], 'this': [1], 'again': [2]}
#
# actual res : {'hello': [0, 2], 'world': [0, 1], 'this': [1], 'is': [1], 'the': [1], 'again':[2]

def reverse_index(dataset):
    dataset = [words.lower() for words in dataset]
    wordlist = list(set((" ".join(dataset)).lower().split()))
    #create a list of all words that appear in dataset after making everything lowercase

    inside = [is_in(word, dataset) for word in wordlist]
    print(inside)
    #list of lists of indices of words that appear in each element in dataset

    return dict(zip(wordlist, inside))
    #create dictionary by zipping two lists
    
def is_in(word, data):
    return [i for i, w in enumerate(data) if word in w.lower().split()]
#method that returns list of sentence indices of appearance if word appears in sentence

# don't forget to return your resulting dictionary
# You can see the output of your function here
print(reverse_index(dataset))
