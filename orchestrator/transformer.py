def transform_movie(movie):
    """
    Convert the official TMDB Movie Details response
    into our PostgreSQL movie structure.
    """

    return {
        "movie_id": movie["id"],
        "title": movie["title"],
        "original_title": movie.get("original_title"),
        "overview": movie.get("overview"),
        "tagline": movie.get("tagline"),
        "release_date": movie.get("release_date"),
        "status": movie.get("status"),
        "runtime": movie.get("runtime"),
        "original_language": movie.get("original_language"),
        "popularity": movie.get("popularity"),
        "vote_average": movie.get("vote_average"),
        "vote_count": movie.get("vote_count"),
        "budget": movie.get("budget"),
        "revenue": movie.get("revenue"),
        "imdb_id": movie.get("imdb_id"),
        "homepage": movie.get("homepage"),
        "poster_path": movie.get("poster_path"),
        "backdrop_path": movie.get("backdrop_path"),
        "adult": movie.get("adult"),
        "video": movie.get("video")
    }