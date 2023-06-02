from istorage import IStorage
import csv
import operator
import random


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """This will list all the movies"""

        holding_storage = ""
        counter = 0

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        for title in movies:
            holding_storage += (
                f"\n{title['title']}, is rated "
                f"{title['rating']}, and came out in {title['year']}")

            counter += 1
            if counter == len(movies):
                return holding_storage

    def add_movie(self, title, year, rating, poster):
        """ Adds a movie to the movies database """
        temp_dict = {}
        # Gets the data from the CSV file

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        if title in movies:
            print(f"Movie {title['title']} already exists!")

        else:

            temp_dict["title"] = title

            temp_dict["year"] = year

            temp_dict["rating"] = float(rating)

            temp_dict["poster"] = poster
            movies.append(temp_dict)

            with open(self.file_path, "w", newline='') as fileobj:
                writer = csv.writer(fileobj)
                writer.writerow(
                    ['title', 'year', 'rating', 'poster'])  # Write header row

                for movie in movies:
                    writer.writerow(
                        [movie['title'], movie['year'],
                         movie['rating'], movie['poster']])

            return "Successfully saved!"

    def delete_movie(self, title):
        """Code to remove movies"""
        counter = -1

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)
            for row in reader:
                movies.append(row)

        # the check if the movie is actually in the list
        for name in movies:
            counter += 1
            if title == name['title']:
                del movies[counter]

                with open(self.file_path, "w", newline='') as fileobj:
                    writer = csv.writer(fileobj)
                    writer.writerow(
                        ['title', 'year', 'rating',
                         'poster'])  # Write header row

                    for movie in movies:
                        writer.writerow(
                            [movie['title'], movie['year'], movie['rating'],
                             movie['poster']])

                return f"Movie {title} successfully deleted"

        else:
            return f"Movie {title} doesn't exist!"

    def update_movie(self):
        """The function to update ratings"""
        movie = input("Enter movie name: ")

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        # check if movie is in movies
        movie_exists = False
        for movie_data in movies:
            if movie_data['title'] == movie:
                movie_exists = True
                break

        if not movie_exists:
            return f"Movie {movie} doesn't exist!"
        else:
            rating = input("Enter new movie rating (0-10): ")

            # check if the rating is valid
            if float(rating) < 0 or float(rating) > 10:
                print(
                    "Invalid rating. Please enter a rating between 0 and 10.")
            else:
                for movie_data in movies:
                    if movie_data['title'] == movie:
                        movie_data['rating'] = rating
                        break

                with open(self.file_path, 'w', newline='') as fileobj:
                    fieldnames = movies[0].keys()
                    writer = csv.DictWriter(fileobj, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(movies)

                return f"Movie {movie} successfully updated"

    def stats_movie(self):
        """This code makes handy stats that are
        readable by humans"""
        movie_ratings = []
        local_movie_dct = {}

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        for title in movies:
            local_movie_dct[title['title']] = float(title["rating"])

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

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        # random choice code
        random_result = random.choice(list(movies))
        title = random_result['title']
        rating = random_result['rating']
        return f"Your movie for tonight: {title}, it's rated {rating}"

    def search_movie(self):
        """The search function"""
        holding_storage = ""
        counter = 0

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        srch = input("Enter part of movie name: ")

        for movie in movies:
            counter += 1

            if counter == len(movies):
                if holding_storage == "":
                    return "No movies found"
                else:
                    return holding_storage

            # convert to lowercase and compare
            if srch.lower() in movie['title'].lower():
                holding_storage += f"{movie['title']}, {movie['rating']}\n"

                if counter == len(movies):
                    return holding_storage

    def ratings_sort_movies(self):
        counter = 0
        holding_storage = ""
        local_movie_dct = {}

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        for title in movies:
            local_movie_dct[title['title']] = float(title['rating'])

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

        with open(self.file_path, 'r') as fileobj:
            reader = csv.DictReader(fileobj)
            movies = list(reader)

        for movie in movies:
            title = movie['title']
            year = movie['year']
            poster = movie['poster']

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
                with open("movies_css.html", "w") as fileobj:
                    fileobj.write(data)
                    return "Successfully saved!"
