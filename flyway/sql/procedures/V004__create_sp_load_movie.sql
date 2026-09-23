CREATE OR REPLACE PROCEDURE ingestion.sp_load_movie(
    IN p_pipeline_run_id UUID
)
LANGUAGE plpgsql
AS $$
DECLARE

    v_payload JSONB;

    v_movie_id BIGINT;

    v_title TEXT;

    v_original_title TEXT;

    v_overview TEXT;

    v_tagline TEXT;

    v_release_date DATE;

    v_status TEXT;

    v_runtime INTEGER;

    v_original_language TEXT;

    v_popularity NUMERIC;

    v_vote_average NUMERIC;

    v_vote_count INTEGER;

    v_budget BIGINT;

    v_revenue BIGINT;

    v_imdb_id TEXT;

    v_homepage TEXT;

    v_poster_path TEXT;

    v_backdrop_path TEXT;

    v_adult BOOLEAN;

    v_video BOOLEAN;

BEGIN

    SELECT payload
    INTO v_payload
    FROM ingestion.pipeline_run_payload
    WHERE pipeline_run_id = p_pipeline_run_id
    ORDER BY received_at DESC
    LIMIT 1;

    IF v_payload IS NULL THEN
        RAISE EXCEPTION
            'No payload found for pipeline run %',
            p_pipeline_run_id;
    END IF;

    v_movie_id          := (v_payload->>'id')::BIGINT;

    v_title             := v_payload->>'title';

    v_original_title    := v_payload->>'original_title';

    v_overview          := v_payload->>'overview';

    v_tagline           := v_payload->>'tagline';

    v_release_date      := NULLIF(v_payload->>'release_date','')::DATE;

    v_status            := v_payload->>'status';

    v_runtime           := NULLIF(v_payload->>'runtime','')::INTEGER;

    v_original_language := v_payload->>'original_language';

    v_popularity        := NULLIF(v_payload->>'popularity','')::NUMERIC;

    v_vote_average      := NULLIF(v_payload->>'vote_average','')::NUMERIC;

    v_vote_count        := NULLIF(v_payload->>'vote_count','')::INTEGER;

    v_budget            := NULLIF(v_payload->>'budget','')::BIGINT;

    v_revenue           := NULLIF(v_payload->>'revenue','')::BIGINT;

    v_imdb_id           := v_payload->>'imdb_id';

    v_homepage          := v_payload->>'homepage';

    v_poster_path       := v_payload->>'poster_path';

    v_backdrop_path     := v_payload->>'backdrop_path';

    v_adult             := COALESCE(
                                (v_payload->>'adult')::BOOLEAN,
                                FALSE
                            );

    v_video             := COALESCE(
                                (v_payload->>'video')::BOOLEAN,
                                FALSE
                            );

    RAISE NOTICE
        'Movie=% Title=% Runtime=% Rating=%',
        v_movie_id,
        v_title,
        v_runtime,
        v_vote_average;

    INSERT INTO tmdb.movie(

        movie_id,

        title,

        original_title,

        overview,

        tagline,

        release_date,

        status,

        runtime,

        original_language,

        popularity,

        vote_average,

        vote_count,

        budget,

        revenue,

        imdb_id,

        homepage,

        poster_path,

        backdrop_path,

        adult,

        video

    )

    VALUES(

        v_movie_id,

        v_title,

        v_original_title,

        v_overview,

        v_tagline,

        v_release_date,

        v_status,

        v_runtime,

        v_original_language,

        v_popularity,

        v_vote_average,

        v_vote_count,

        v_budget,

        v_revenue,

        v_imdb_id,

        v_homepage,

        v_poster_path,

        v_backdrop_path,

        v_adult,

        v_video

    )

    ON CONFLICT(movie_id)

    DO UPDATE

    SET

        title = EXCLUDED.title,

        original_title = EXCLUDED.original_title,

        overview = EXCLUDED.overview,

        tagline = EXCLUDED.tagline,

        release_date = EXCLUDED.release_date,

        status = EXCLUDED.status,

        runtime = EXCLUDED.runtime,

        original_language = EXCLUDED.original_language,

        popularity = EXCLUDED.popularity,

        vote_average = EXCLUDED.vote_average,

        vote_count = EXCLUDED.vote_count,

        budget = EXCLUDED.budget,

        revenue = EXCLUDED.revenue,

        imdb_id = EXCLUDED.imdb_id,

        homepage = EXCLUDED.homepage,

        poster_path = EXCLUDED.poster_path,

        backdrop_path = EXCLUDED.backdrop_path,

        adult = EXCLUDED.adult,

        video = EXCLUDED.video,

        updated_at = NOW();

    RAISE NOTICE
        'Movie % successfully loaded.',
        v_movie_id;

EXCEPTION

    WHEN OTHERS THEN

        RAISE EXCEPTION
            'sp_load_movie failed for pipeline run %: %',
            p_pipeline_run_id,
            SQLERRM;

END;
$$;