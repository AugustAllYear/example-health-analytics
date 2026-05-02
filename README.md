# example-health-analytics

A healthcare analytics consultancy project. Demonstrates SQL, data warehousing, semi‑structured data, and performance tuning using **DuckDB**.

## Client (mock)
Example Health Analytics – a healthcare consultancy needing local, reproducible analytics to identify cost drivers and provider efficiency.

## Tech stack
- Python 3.10+
- DuckDB (local analytics database)
- Git + GitHub

## Project structure

```
example-health-analytics/
├── config.default.yaml
├── .gitignore
├── README.md
├── requirements.txt
├── scripts/
│ ├── 00_generate_data.py
│ ├── 01_setup.sql
│ ├── 02_load.sql
│ ├── 03_transform.sql
│ ├── 04_analysis.sql
│ ├── 05_performance.sql
│ └── run_all.py
├── data/ (generated)
└── results/
```

## Quick start
```bash
git clone https://github.com/yourusername/example-health-analytics.git
cd example-health-analytics
python -m venv venv
source venv/bin/activate      # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
cp config.default.yaml config.yaml
python scripts/00_generate_data.py
python scripts/run_all.py
```

All sql scriptes are executed in order. Use `duckdb example-health.duckdb` to explore the database interactivley.


---

## 3. A‑Z Run Instructions

1. **Prerequisites**  
   - Install Python 3.10 or 3.11.  
   - Install Git.  
   - (Optional) Install DuckDB CLI if you want to inspect the database manually – `duckdb example-health.duckdb`.

2. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/example-health-analytics.git
   cd example-health-analytics
   ```
3. **Set up virtual environment**
   	```bash
	python3.10 -m venv venv
	source venv/bin/activate   # Linux/macOS
	# or
	venv\Scripts\activate       # Windows
	```
4. **Install dependencies**
   ```bash
   pip install -r rrequirements.txt
   ```
5. Create local configuration
   ```bash
   cp config.default.yaml config.yaml
   ```
6. Generate synthetic data
   ```bash
   python scripts/00_generate_data.py
   ```
   This creates data/claims.parquet and ata/provider.json
7. Run the full pipeline
   ```bash
   python scripts/run_all.py
   ```
8. Verify the results
   ```bash
   duckdb example-health.duckdb
   ```
   Then run:
   ```sql
   SELECT * FROM core.claims LIMIT 5;
   SELECT * FROM core.providers LIMIT 5;
   ```
9. Explore further
    - Add your own queries to `scritps/04_analysis.sql` and re-run `run_all.py`.
    - Modify `config.yaml` to increase `num_claims` to 500k and tets performance.
