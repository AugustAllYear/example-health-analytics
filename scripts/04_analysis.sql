-- A. CTE for data extraction: find duplicate claims (just in case)
WITH duplicate_claims_cte AS (
    SELECT claim_id, COUNT(*) AS cnt
    FROM core.claims
    GROUP BY claim_id
    HAVING COUNT(*) > 1
)
SELECT 8 FROM duplicate_claims_cte; -- usually empty

-- C. Complex query: aggregate by specialty, filter on avg claim amount
SELECT
    p.speciality,
    COUNT(DISTINCT c.patient_id) AS unique_patients,
    COUNT(c.claim_id) AS total_claims,
    AVG(c.claim_amount) AS avg_claim_amt,
    SUM(c.paid_amount) AS total_paid
FROM core.claims c
JOIN core.providers p ON c.provider_id = p.provider_id
WHERE c.payment_status = 'paid'
GROUP BY p.specialty
HAVING AVG(c.claim_amount) > 1000
ORDER BY avg_claim_amy DESC;
