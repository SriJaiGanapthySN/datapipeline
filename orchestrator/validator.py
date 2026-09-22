def validate_movie(movie):
    """
    Validate the TMDB Movie Details response.
    """

    required_fields = [
        "id",
        "title",
        "release_date",
        "vote_average"
    ]

    missing = []

    for field in required_fields:
        if field not in movie or movie[field] is None:
            missing.append(field)

    if missing:
        raise ValueError(
            f"Missing required fields: {', '.join(missing)}"
        )

    if not isinstance(movie["id"], int):
        raise TypeError("Movie ID must be an integer.")

    return True