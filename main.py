from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    """This starts up the entire program, and chooses the file type"""

    user_input = input(f"1. JSON\n2. CSV\n Enter format: ")

    if user_input == "1":
        storage = StorageJson('movies.json')
        movie_app = MovieApp(storage)
        movie_app.run()

    elif user_input == "2":
        storage = StorageCsv('movies.csv')
        movie_app = MovieApp(storage)
        movie_app.run()


if __name__ == "__main__":
    main()
