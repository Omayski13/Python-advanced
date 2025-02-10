def movie_organizer(*args):
    movies = {}
    result = []
    for data in args:
        movie = data[0]
        genre = data[1]
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)
    sorted_movies = dict(sorted(movies.items(),key=lambda x: (-len(x[1]), x[0])))
    for genre,movies in sorted_movies.items():
        result.append(f"{genre} - {len(movies)}\n")
        for movi in sorted(movies):
            result.append(f"* {movi}\n")
    return "".join(result)



print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

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

