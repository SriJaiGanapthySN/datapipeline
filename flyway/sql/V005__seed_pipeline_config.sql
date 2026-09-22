INSERT INTO ingestion.pipeline_config(

    pipeline_name,

    source_name

)

VALUES(

    'TMDB Movies',

    'TMDB API'

)

ON CONFLICT(pipeline_name)

DO NOTHING;