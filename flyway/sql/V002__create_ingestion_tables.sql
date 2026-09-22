CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE IF NOT EXISTS ingestion.pipeline_config (

    pipeline_config_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    pipeline_name TEXT NOT NULL UNIQUE,

    source_name TEXT NOT NULL,

    is_active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE TABLE IF NOT EXISTS ingestion.pipeline_run (

    pipeline_run_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    pipeline_config_id UUID NOT NULL REFERENCES ingestion.pipeline_config(pipeline_config_id),

    status TEXT NOT NULL CHECK (
        status IN ('RUNNING','COMPLETED','FAILED')
    ),

    started_at TIMESTAMPTZ DEFAULT NOW(),

    completed_at TIMESTAMPTZ

);

CREATE TABLE IF NOT EXISTS ingestion.pipeline_run_payload (

    payload_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    pipeline_run_id UUID NOT NULL REFERENCES ingestion.pipeline_run(pipeline_run_id) ON DELETE CASCADE,

    payload JSONB NOT NULL,

    received_at TIMESTAMPTZ DEFAULT NOW()

);

CREATE INDEX IF NOT EXISTS idx_pipeline_run_status
ON ingestion.pipeline_run(status);

CREATE INDEX IF NOT EXISTS idx_pipeline_payload_run
ON ingestion.pipeline_run_payload(pipeline_run_id);

CREATE INDEX IF NOT EXISTS idx_payload_json
ON ingestion.pipeline_run_payload
USING GIN(payload);