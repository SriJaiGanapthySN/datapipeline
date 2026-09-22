CREATE TABLE IF NOT EXISTS tmdb.movie_genre (

    genre_id INTEGER PRIMARY KEY,

    genre_name VARCHAR(100) NOT NULL,

    created_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE INDEX IF NOT EXISTS idx_movie_genre_name
ON tmdb.movie_genre(genre_name);