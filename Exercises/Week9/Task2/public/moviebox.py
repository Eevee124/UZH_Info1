#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie

class MovieBox(Movie):

    #title not empty and movies not empty
    def __init__(self, title, movies):
        if len(title) == 0 or len(movies) == 0: raise Warning("Title or movies cannot be empty!")

        if not all(isinstance(movie, Movie) for movie in movies): raise Warning("Not all movies are of object Movie!")

        self.__title = title
        self.__movies = movies

    def __eq__(self, other):
        if isinstance(other, MovieBox):
            return self.get_title() == other.get_title() and self.get_movies() == other.get_movies()
        else: return NotImplemented

    def __repr__(self):
        repr = f'MovieBox("{self.get_title()}", {self.get_movies()})'
        return repr.replace("'", "\"")

    def __hash__(self):
        return hash((self.get_title(), tuple(self.get_movies())))

    def get_title(self):
        return self.__title

    def get_actors(self):
        actors = []
        for movie in self.__movies:
            actors.extend(movie.get_actors())

        actors = sorted(set(actors))

        return actors

    def get_duration(self):
        length = 0
        for movie in self.__movies:
            length += movie.get_duration()
        return length

    def get_movies(self):
    	return self.__movies.copy()

    # also implement the required special functions
