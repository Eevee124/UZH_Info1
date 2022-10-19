from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = ['Hellohello', 'hello']

 #returns this dictionary {'hello': [0, 2], 'is': [1], 'the': [1], 'world': [0, 1], 'this': [1], 'again': [2]}
#
# actual res : {'hello': [0, 2], 'world': [0, 1], 'this': [1], 'is': [1], 'the': [1], 'again':[2]

def reverse_index(dataset):
    return dict(zip(list(set((" ".join(dataset)).lower().split())), [[i for i, w in enumerate([words.lower() for words in dataset]) if word in w.lower().split()] for word in list(set((" ".join(dataset)).lower().split()))]))
    #create dictionary by zipping two lists
    
# don't forget to return your resulting dictionary
# You can see the output of your function here
print(reverse_index(dataset))
