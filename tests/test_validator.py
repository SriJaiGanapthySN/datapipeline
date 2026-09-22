from orchestrator.validator import validate_movie

movie = {
    "id":550,
    "title":"Fight Club",
    "release_date":"1999-10-15",
    "vote_average":8.4
}

validate_movie(movie)

print("Validation Passed")