from orchestrator.db import get_connection

def create_pipeline_run():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO ingestion.pipeline_run(
            pipeline_config_id,
            status
        )
        SELECT pipeline_config_id, 'RUNNING'
        FROM ingestion.pipeline_config
        WHERE pipeline_name='TMDB Movies'
        RETURNING pipeline_run_id;
    """)

    run_id = cur.fetchone()[0]

    conn.commit()
    conn.close()

    return run_id
import json

def store_payload(run_id, payload):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO ingestion.pipeline_run_payload(
            pipeline_run_id,
            payload
        )
        VALUES (%s,%s)
    """, (run_id, json.dumps(payload)))

    conn.commit()
    conn.close()

def load_movie(run_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL ingestion.sp_load_movie(%s);",
        (run_id,)
    )

    conn.commit()
    conn.close()

def update_pipeline_status(run_id, status):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE ingestion.pipeline_run
        SET
            status=%s,
            completed_at=NOW()
        WHERE pipeline_run_id=%s;
    """, (status, run_id))

    conn.commit()
    conn.close()

from orchestrator.api_extractor import get_movie
from orchestrator.validator import validate_movie
from orchestrator.transformer import transform_movie

def run_pipeline(movie_id):

    run_id = create_pipeline_run()
    print(f"Pipeline started for movie_id: {movie_id}, run_id: {run_id}")

    try:

        movie = get_movie(movie_id)

        validate_movie(movie)

        normalized_movie = transform_movie(movie)

        store_payload(run_id, movie)
        load_movie(run_id)

        update_pipeline_status(run_id, "COMPLETED")

        print(f"Pipeline completed for {normalized_movie['title']}")

        return normalized_movie

    except Exception as e:

        update_pipeline_status(run_id, "FAILED")

        raise e
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--movie-id",
        required=True,
        type=int
    )

    args = parser.parse_args()

    run_pipeline(args.movie_id)