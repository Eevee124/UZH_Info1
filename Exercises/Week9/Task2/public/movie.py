#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):

        if len(title) == 0 or len(actors) == 0: raise Warning("Title or actor list is empty!")

        if duration < 1: raise Warning("Movie must be at least one minute long!")

        self.__title = title
        self.__actors = actors
        self.__duration = duration
    
    #allows for equality comparison '=='
    def __eq__(self, other):
        if isinstance(other, Movie):
            return self.get_title() == other.get_title() and self.get_actors() == other.get_actors() and self.get_duration() == other.get_duration()
        else: return NotImplemented

    #for correct representation
    def __repr__(self):
        repr = f'Movie("{self.get_title()}", {self.get_actors()}, {self.__duration})'
        return repr.replace("'", "\"")

    #needs to be of the form (title, [actor1, actor2], duration)
    def __hash__(self):
        return hash((self.__title, tuple(self.get_actors()), self.__duration()))

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors.copy()

    def get_duration(self):
       return self.__duration

    # also implement the required special functions
