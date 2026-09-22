from orchestrator.api_extractor import get_movie

movie = get_movie(550)

print(movie["title"])
print(movie["release_date"])
print(movie["vote_average"])