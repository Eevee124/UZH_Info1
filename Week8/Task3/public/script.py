#!/usr/bin/env python3

class Fridge:
    
    def __init__(self):

        self.__products = []
        self.__index = -1


    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1

        try:
            return self.__products[self.__index]
        except IndexError: raise StopIteration()


    def __len__(self):
        return len(self.__products)

    def store(self, item):
        self.__products.append(item)
        self.__products.sort()
        #return sorted so that you access the first item that appears by date


    def take(self, item):
        for product in self.__products:
            if item == product:
                self.__products.remove(item)
                return item
        
        raise Warning("No matching item found!")

    def find(self, name):
        for tuple in self.__products:
            if tuple[1] == name:
                return tuple

        return None

    def take_before(self, date):

        expired = []

        for item in self.__products:
            if item[0] < date:
                expired.append(item)
                self.__products.remove(item)

        return expired

#needs to be commented out to work
"""
f = Fridge()
f.store((191127, "Butter"))
f.store((191117, "Milk"))

print("Items in the fridge:")
for i in f:
    print("- {} ({})".format(i[1], i[0]))

f.take((191127, "Butter")) # ok
f.take((191207, "Bread")) # fails
"""