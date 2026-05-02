-- Flatten nested JSON into relational table
CREATE OR REPLACE TABLE core.providers AS 
SELECT
    provider_id,
    name AS provider_name,
    specialty,
    npi::VARCHAR AS npi,
    location.city::VARCHAR AS city,
    location.state::VARCHAR AS state,
    contract_network
FROM staging.providers_raw;

-- Clean claims (add data types, filter)
CREATE OR REPLACE TABLE core.claims AS
SELECT
    claim_id,
    patient_id,
    provider_id,
    claim_amount::DECIMAL(12,2) AS claim_amount,
    paid_amount::DECIMAL(12,2) AS paid_amount,
    claim_date::DATE AS claim_date,
    payment_status
FROM staging.claims_raw
WHERE claim_amount > 0;
    
