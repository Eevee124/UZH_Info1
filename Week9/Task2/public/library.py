#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie
from public.moviebox import MovieBox

class Library(MovieBox):

    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        if not movie in self.__movies: self.__movies.append(movie)

    def get_movies(self):

        films = []
        film_dict = {}

        for movie in self.__movies:
            if isinstance(movie, MovieBox):
                
                for temp in movie.get_movies():
                    film_dict[temp.get_title()] = temp
                    
            else: film_dict[movie.get_title()] = movie
        
        for key in sorted(film_dict):
            films.append(film_dict[key])

        return films

    def get_total_duration(self):
        length = 0

        for movie in self.__movies:
            length += movie.get_duration()

        return length