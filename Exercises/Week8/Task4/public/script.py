#!/usr/bin/env python3

class MagicDrawingBoard:
    def __init__(self, x, y):

        if x < 1 or y < 1: raise Warning("Board too small!")
        self.__x = x
        self.__y = y
        self.__image = []

        for _ in range(self.__y):
            line = []
            for _ in range(self.__x):
                line.append('0')
            self.__image.append(line)


    def pixel(self, coords):
        
        if coords[0] < 0 or coords[1] < 0 or coords[1] > self.__y - 1 or coords[0] > self.__x - 1:
            raise Warning("Coordinates out of bounds!")

        self.__image[coords[1]][coords[0]] = '1'

    def img(self):

        string = ''

        for line in self.__image:
            string += "".join(line) + "\n"
        return string.strip()

    def rect(self, coord1, coord2):

        if coord1[0] < 0 or coord1[1] < 0:
            raise Warning("Rectangle cannot start below 0 coordinates!")

        if coord1[0] >= coord2[0] or coord1[1] >= coord2[1]:
            raise Warning("Invalid input! Must start with top left and bottom right!")
        
        if coord2[0] > self.__x or coord2[1] > self.__y:
            raise Warning("Cannot be bigger than the actual board!")

        for i in range(coord1[1], coord2[1]):
            for j in range(coord1[0], coord2[0]):
                self.__image[i][j] = '1'
        

    def reset(self):
        for i in range(self.__y):
            for j in range(self.__x):
                self.__image[i][j] = '0'

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6,4) # instantiation of a specific size
    db.pixel((1,1)) # draw at one coordinate
    db.rect((2,2), (5,4)) # draw a rectangle
    img = db.img() # return the drawn image
    print(img)
    db.reset() # reset the field again
    db.pixel((5,3))
    img = db.img()
    print(img)

