-- Load Parquet (claims)
CREATE OR REPLACE TABLE	staging.claims_raw AS
SELECT * FROM read_parquet('data/claims.parquet');

-- Load JSON (providers) - semi-structured
CREATE OR REPLACE TABLE staging.providers_raw AS
SELECT * FROM read_json_auto('data/providers.json');
