-- D. Explain plan (DuckDB's optimizer)
EXPLAIN
SELECT p.specialty, COUNT(*)
FROM core.claims c
JOIN core.providers p ON c.provider_id = p.provider_id
GROUP BY p.specialty;

-- =============================================
-- OPTIMISATION SUGGESTIONS (for larger datasets)
-- =============================================
-- 1. Index creation (DuckDB supports indexes on columns used in WHERE/JOIN)
--    Example: CREATE INDEX idx_claims_provider ON core.claims(provider_id);
--    However, for tables under ~1GB, indexes may not improve speed significantly.
--
-- 2. Data type optimisation: use narrower types (e.g., DECIMAL(10,2) instead of FLOAT).
--
-- 3. Filter early: push conditions into subqueries or CTEs before joining.
--
-- 4. For time‑series filtering (e.g., claim_date), range partitioning is not
--    natively supported in DuckDB, but you can manually partition into separate tables
--    or use a date filter that leverages DuckDB's automatic min/max metadata pruning.
--
-- 5. Use `EXPLAIN` to identify bottlenecks – this query shows a perfect hash join,
--    which is efficient for modest data sizes.
-- =============================================
