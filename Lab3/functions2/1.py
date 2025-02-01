# Список фильмов, представленный в задании
movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]

# 1) function that takes a single movie and returns `True` if its IMDB score is above 5.5
def is_imdb_above_5_5(movie):
    return movie["imdb"] > 5.5

# 2) function that returns a sublist of movies with an IMDB score above 5.5.
def high_rating_movies(movie_list):
    return [m for m in movie_list if is_imdb_above_5_5(m)]

# 3) function that takes a category name and returns just those movies under that category.
def get_movies_by_category(movie_list, category):
    return [m for m in movie_list if m["category"] == category]

# 4) function that takes a list of movies and computes the average IMDB score.
def average_imdb(movie_list):
    total_score = sum(m["imdb"] for m in movie_list)
    return total_score / len(movie_list)

# 5) function that takes a category and computes the average IMDB score.
def average_imdb_by_category(movie_list, category):
    movies_in_cat = get_movies_by_category(movie_list, category)
    if not movies_in_cat:
        return 0
    
    return average_imdb(movies_in_cat)
