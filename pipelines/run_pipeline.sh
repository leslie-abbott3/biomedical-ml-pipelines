#!/bin/bash
# Orchestrates ETL pipeline

echo "[INFO] Running SQL ETL pipeline..."
sqlite3 biomedical.db < pipelines/etl_pipeline.sql
echo "[INFO] ETL pipeline completed. Processed table available in biomedical.db"
