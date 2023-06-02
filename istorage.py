from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """This code will list movies"""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """This code adds movies"""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """This code deletes movies"""
        pass

    @abstractmethod
    def update_movie(self):
        """This code only updates ratings"""
        pass

    @abstractmethod
    def random_movie(self):
        """This code picks out a random movie"""
        pass

    @abstractmethod
    def search_movie(self):
        """This code allows you to search movies"""
        pass

    @abstractmethod
    def ratings_sort_movies(self):
        """This code sorts movies by ratings"""
        pass