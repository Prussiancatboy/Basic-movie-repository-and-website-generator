from istorage import IStorage
import json
import random
import operator


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """This will list all the movies"""

        holding_storage = ""
        counter = 0
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        # print total movies
        print(f"{len(movies)} movies in total")

        for title in dict.items(movies):
            holding_storage += (
                f"\n{title[0]}, is rated "
                f"{title[1]['rating']}, and came out in {title[1]['year']}")

            counter += 1
            if counter == len(movies):
                return holding_storage

    def add_movie(self, title, year, rating, poster):
        """ Adds a movie to the movies database """

        temp_dict = {}
        # Gets the data from the JSON file
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        if title in movies:
            return f"Movie {title} already exists!"

        else:

            movie_title = title

            temp_dict["year"] = year

            temp_dict["rating"] = float(rating)

            temp_dict["poster"] = poster

            movies[movie_title] = temp_dict

            with open(self.file_path, "w") as fileobj:
                json.dump(movies, fileobj)
                return "Successfully saved!"

    def delete_movie(self, title):
        """Code to remove movies"""
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        # the check if the movie is actually in the list
        if title in movies:
            del movies[title]
            with open(self.file_path, "w") as fileobj:
                json.dump(movies, fileobj)

            return f"Movie {title} successfully deleted"

        else:
            return f"Movie {title} doesn't exist!"

    def update_movie(self):
        """The function to update ratings"""
        movie = input("Enter movie name: ")

        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        # check if movie is in movies
        if movie not in movies:
            return f"Movie {movie} doesn't exist!"
        else:
            rating = input("Enter new movie rating (0-10): ")

            # check if the rating is valid
            if int(float(rating)) < 10 or int(float(rating)) > 1:
                movies[movie]["rating"] = int(float(rating))

                with open(self.file_path, "w") as fileobj:
                    json.dump(movies, fileobj)

                return f"Movie {movie} successfully updated"

    def stats_movie(self):
        """This code makes handy stats that are
        readable by humans"""
        movie_ratings = []
        local_movie_dct = {}
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        for title in dict.items(movies):
            local_movie_dct[title[0]] = float(title[1]["rating"])

        for movie in local_movie_dct.values():
            movie_ratings.append(movie)
        sorted_ratings = sorted(movie_ratings, key=lambda x: float(x))

        # highest and lowest values
        highest_rating = sorted_ratings[-1]
        lowest_rating = sorted_ratings[0]
        highest = list(local_movie_dct.keys())[
            list(local_movie_dct.values()).index(highest_rating)]
        lowest = list(local_movie_dct.keys())[
            list(local_movie_dct.values()).index(lowest_rating)]

        # averager code
        average = 0
        for movie in movie_ratings:
            average += float(movie)
        average = average / len(movie_ratings)
        average = round(average, 1)

        # median finder
        ratings_len = len(movie_ratings)
        if ratings_len % 2 == 0:
            median = (movie_ratings[ratings_len // 2] + movie_ratings[
                ratings_len // 2 - 1]) / 2
            median = round(median, 1)
        else:
            median = movie_ratings[ratings_len // 2]
        return (
            f"Average rating: {average} \nMedian rating:"
            f"{median} \nBest movie: {highest}, "

            f"{highest_rating} \n"
            f"Worst movie: {lowest}, {lowest_rating}")

    def random_movie(self):
        """This code picks a random movie"""
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        # random choice code
        movie, movie_info = random.choice(list(movies.items()))
        rating = movie_info["rating"]
        return f"Your movie for tonight: {movie}, it's rated {rating}"

    def search_movie(self):
        """The search function"""
        holding_storage = ""
        counter = 0
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        srch = input("Enter part of movie name: ")

        for movie in movies:
            counter += 1

            if counter == len(movies):
                if holding_storage == "":
                    return "No movies found"
                else:
                    return holding_storage

            # convert to lowercase and compare
            if srch.lower() in movie.lower():
                holding_storage += f'{movie}, {movies[movie]["rating"]}\n'

                if counter == len(movies):
                    return holding_storage

    def ratings_sort_movies(self):
        counter = 0
        holding_storage = ""
        local_movie_dct = {}
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        for title in dict.items(movies):
            local_movie_dct[title[0]] = float(title[1]["rating"])

        # to sort movies
        movies_sorted = sorted(local_movie_dct.items(),
                               key=operator.itemgetter(1), reverse=True)
        for movie in movies_sorted:
            holding_storage += f"{movie[0]}, {movie[1]}\n"
            counter += 1
            if counter == len(movies_sorted):
                return holding_storage

    def generate_website(self):
        counter = 0
        final_string = ""
        with open(self.file_path) as fileobj:
            movies = json.load(fileobj)

        for movie in movies:
            title = movie
            year = movies[movie]['year']
            poster = movies[movie]['poster']

            final_string += '<li>\n' \
                            '<div class="movie">\n' \
                            f'    <img class="movie-poster" src="' \
                            f'{poster}" title="">\n' \
                            f'    <div class="movie-title">{title}</div>\n' \
                            f'    <div class="movie-year">{year}</div>\n' \
                            f'</div>\n'
            counter += 1

            if counter == len(movies):
                with open("index_template.html", "r") as fileobj:
                    data = fileobj.read()
                    data = data.replace("__TEMPLATE_MOVIE_GRID__",
                                        final_string)

                # this part writes the text into a new file
                with open("movies_json.html", "w") as fileobj:
                    fileobj.write(data)
                    return "Successfully saved!"
