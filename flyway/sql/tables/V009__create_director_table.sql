CREATE TABLE IF NOT EXISTS tmdb.movie_director (

    d_id INTEGER PRIMARY KEY,

    d_name VARCHAR(100) NOT NULL,

    created_at TIMESTAMPTZ DEFAULT NOW()

);