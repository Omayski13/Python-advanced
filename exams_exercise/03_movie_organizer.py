def movie_organizer(*args):
    movies = {}
    for movie,genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)
    sorted_dict = sorted(movies.items(),key=lambda x: (-len(x[1]), x[0],))
    result = []
    for genres,movie_name in sorted_dict:
        result.append(f"{genres} - {len(movie_name)}\n")
        sorted_movies = sorted(movie_name)
        for movie in sorted_movies:
            result.append(f"* {movie}\n")
    return "".join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))




