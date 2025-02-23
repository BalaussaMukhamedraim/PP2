def is_highly_rated(movie):
    """Takes a dictionary with movie information and returns True if its IMDB rating is above 5.5"""
    return movie["imdb"] > 5.5


def filter_high_rated_movies(movies):
    """Returns a sublist of movies with an IMDB score above 5.5"""
    return [movie for movie in movies if movie["imdb"] > 5.5]


def get_movies_by_category(movies, category):
    """Returns a list of movies belonging to a specific category"""
    return [movie for movie in movies if movie["category"].lower() == category.lower()]


def average_imdb_score(movies):
    """Computes the average IMDB score of a list of movies"""
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)


def average_imdb_score_by_category(movies, category):
    """Computes the average IMDB score of movies in a specific category"""
    category_movies = get_movies_by_category(movies, category)
    return average_imdb_score(category_movies)

# Example usage:
example_movie = {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}
print(is_highly_rated(example_movie))  # Output: True

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
]

print(filter_high_rated_movies(movies))
print(get_movies_by_category(movies, "Romance"))
print(average_imdb_score(movies))
print(average_imdb_score_by_category(movies, "Thriller"))
