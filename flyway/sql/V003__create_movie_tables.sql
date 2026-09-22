CREATE TABLE IF NOT EXISTS tmdb.movie (

    movie_id BIGINT PRIMARY KEY,

    title TEXT NOT NULL,

    original_title TEXT,

    overview TEXT,

    tagline TEXT,

    release_date DATE,

    status TEXT,

    runtime INTEGER,

    original_language TEXT,

    popularity NUMERIC,

    vote_average NUMERIC,

    vote_count INTEGER,

    budget BIGINT,

    revenue BIGINT,

    imdb_id TEXT,

    homepage TEXT,

    poster_path TEXT,

    backdrop_path TEXT,

    adult BOOLEAN,

    video BOOLEAN,

    created_at TIMESTAMPTZ DEFAULT NOW(),

    updated_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE INDEX IF NOT EXISTS idx_movie_release_date
ON tmdb.movie(release_date);

CREATE INDEX IF NOT EXISTS idx_movie_language
ON tmdb.movie(original_language);

CREATE INDEX IF NOT EXISTS idx_movie_rating
ON tmdb.movie(vote_average DESC);