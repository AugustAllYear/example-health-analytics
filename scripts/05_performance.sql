-- D. Explain plan (DuckDB's optimizer)
EXPLAIN
SELECT p.specialty, COUNT(*)
FROM core.claims c
JOIN core.providers p ON c.provider_id = p.provider_id
GROUP BY p.specialty


