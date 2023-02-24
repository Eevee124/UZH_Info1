#!/usr/bin/env python3

def evolve(state, steps):
    # implement this function

    if not type(state) == tuple:
        raise Warning("Invalid world type!")
    
    if not type(steps) == int or steps <= 0:
        raise Warning("Steps must be a positive Integer!")

    if len(state) < 3 or len(state[0]) < 3:
        raise Warning("Invalid world dimensions!")

    if not all (len(line) == len(state[0]) for line in state):
        raise Warning("Each line must have the same length!")

    if not all(chars in "-| #"  for line in state for chars in line):
        raise Warning("Invalid characters in world!")
    
    if not all(chars == '-' for chars in state[0]) or not all(chars == '-' for chars in state[-1]):
        raise Warning("Invalid characters in first or last line of world!")
    
    for i in range(1, len(state) - 1):
        if not (state[i][0] == '|' and state[i][-1] == '|'):
            raise Warning("Invalid characters in world edge!")
        
        for j in range(1, len(state[0]) - 1):
            if not (state[i][j] == ' ' or state[i][j] == '#' ):
                raise Warning("Invalid characters in world body!")

    #all exceptions checked

    map = []
    for i in range(1, len(state) - 1):
        map.append(state[i])
    
    next = []

    #loop through each field in the body and determine next state to use
    for i, line in enumerate(map):
        #adds border whenever you are at beginning of line and new element to list
        next.append('|')

        #ignoring the edges because we add them before and after looping through a line
        #print(i)

        #print(i)
        for j, field in enumerate(map[i]):

            if j == 0 or j == len(map[0]) - 1: continue
            
            n = 0

            #left neighbour
            if j > 1:
                if map[i][j - 1] == '#': n += 1

            #right neighbour
            if j < len(map[0]) - 1:
                if map[i][j + 1] == '#': n += 1

            ####BOTTOMS####
            #bottom neighbour
            if i < len(map) - 1:
                #print('bot')
                if map[i + 1][j] == '#': n += 1
            
            #bottom left neighbour
                if j > 1:
                    if map[i + 1][j - 1] == '#': n += 1

            #bottom right neighbour
                if j < len(map[0]) - 1:
                    if map[i + 1][j + 1] == '#': n += 1

            #####TOPS#####
            #top neighbour
            if i > 0:

                if map[i -1][j] == '#': n += 1

            #top left neighbour
                if j > 1:
                    if map[i - 1][j - 1] == '#': n += 1

            #top right neighbour
                if j < len(map[0]) - 1:
                    if map[i - 1][j + 1] == '#': n += 1

            #checking state of neighbours
            if field == '#':
                if n < 2 or n > 3:
                    next[i] += ' '
                else:
                    next[i] += '#'
                
            else:
                if n == 3:
                    next[i] += '#'
                else:
                    next[i] += ' '

        next[i] += '|'


    #inserts first and last line of '-' symbols
    next.insert(0, state[0])
    next.append(state[-1])

    if steps == 1:

        alive = 0

        for line in next:
            for char in line:
                if char == '#':
                    alive += 1
        
        return tuple(next), alive # placeholder
    else:

        return evolve(tuple(next), steps - 1)

field = (
    "--------------",
    "|            |",
    "|  ###       |",
    "|  #         |",
    "|   #        |",
    "|            |",
    "--------------"
)

"""
field = (
    "---------",
    "|  #####|",
    "---------"
)

"""
steps = 1

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
print(result)
print(f"{alive_cells} are alive.")

