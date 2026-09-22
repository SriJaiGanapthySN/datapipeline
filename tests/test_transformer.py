from orchestrator.transformer import transform_movie

movie = {
    "id":550,
    "title":"Fight Club",
    "original_title":"Fight Club",
    "release_date":"1999-10-15",
    "runtime":139,
    "vote_average":8.4,
    "vote_count":28000,
    "popularity":95.3,
    "adult":False,
    "video":False
}

result = transform_movie(movie)

print(result)