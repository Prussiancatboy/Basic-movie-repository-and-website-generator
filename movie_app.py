import requests


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """This lists the movies"""
        movies = self._storage.list_movies()
        return movies

    def _add_movie(self, title):
        # this part actually grabs movie information

        """This tries to fetch the movie,
        if it fails it should return None or a server error"""
        name = title
        res = requests.get(
            f'https://www.omdbapi.com/?t={name}&apikey=1e3e73a4')
        # store the response of URL

        if res.status_code != 200:
            return "Server error"
        else:
            movie = res.json()
            if movie['Response'] == "False":
                return None
            else:
                title = movie['Title']
                year = movie['Year']
                rating = float(movie['imdbRating'])
                poster = movie['Poster']

                result = self._storage.add_movie(title, year, rating, poster)
                return result

    def _delete_movie(self, title):
        """This deletes movies"""
        return self._storage.delete_movie(title)

    def _update_rating(self):
        """vestigial code, but it updates the rating"""
        return self._storage.update_movie()

    def _command_movie_stats(self):
        """Movie stats function call"""
        return self._storage.stats_movie()

    def _command_random_movie(self):
        """random movie function call"""

        return self._storage.random_movie()

    def _command_search(self):
        """The search function"""
        return self._storage.search_movie()

    def _command_movies_by_ratings(self):
        """function call to sort movies by rating"""
        return self._storage.ratings_sort_movies()

    def _generate_website(self):
        return self._storage.generate_website()

    def run(self):
        """this is the main menu"""
        user_input = input(
            "********** My Movies Database ********** "
            "\nMenu:\n0. Exit\n1. List movies\n2. Add movie\n"
            "3. Delete movie\n4. Update movie\n5. Stats\n6. "
            "Random movie\n7. Search movie\n8. Movies sorted by rating\n"
            f"9. Generate website"
            "\nEnter choice (0-9): ")

        # call to list movies
        if int(user_input) == 0:
            print("Bai :3!")
            exit()

        elif int(user_input) == 1:
            print(self._command_list_movies())

        # call to add movies
        elif int(user_input) == 2:
            result = self._add_movie(input("Enter new movie name: "))
            if result is None:
                print("No movie found")
            else:
                print(result)

        # call to Movie deletion
        elif int(user_input) == 3:
            print(self._delete_movie(input("Enter movie name to delete: ")))

        # Rating update call
        elif int(user_input) == 4:
            print(self._update_rating())

        # stats call
        elif int(user_input) == 5:
            print(self._command_movie_stats())

        # random movie call
        elif int(user_input) == 6:
            print(self._command_random_movie())

        # search call
        elif int(user_input) == 7:
            print(self._command_search())

        # movie by ratings call
        elif int(user_input) == 8:
            print(self._command_movies_by_ratings())

        elif int(user_input) == 9:
            print(self._generate_website())

        # invalid selection code
        else:
            print("Invalid choice")
            self.run()

        input("Press enter to continue")
        self.run()
