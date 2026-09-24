CREATE TABLE IF NOT EXISTS tmdb.movie_flop (

    genre_id INTEGER PRIMARY KEY,

    genre_name VARCHAR(100) NOT NULL,

    created_at TIMESTAMPTZ DEFAULT NOW()

);

