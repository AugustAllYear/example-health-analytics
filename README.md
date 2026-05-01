# example-health-analytics
A healthcare analytics consultancy project. The client needed a local, reproducible analytics layer to identify cost drivers and provider efficiency. 


**Portfo**Portfolio project** demonstrating SQL, data warehousing, semi‑structured data, and performance tuning using **DuckDB** for a mock healthcare analytics client.

## Client (mock)
Example Health Analytics – a healthcare consultancy needing local, reproducible analytics to identify cost drivers and provider efficiency.

## Tech stack
- Python 3.10+
- DuckDB (local analytics database)
- Git + GitHub

## How to run
1. Clone repo
2. Create virtual environment (see instructions in README)
3. Install dependencies: `pip install -r requirements.txt`
4. Generate synthetic data: `python scripts/00_generate_data.py`
5. Run DuckDB CLI or Python script to execute `.sql` files in order

Example using DuckDB CLI:
```bash
duckdb -init scripts/01_setup.sql
duckdb -init scripts/02_load.sql
...


```
	example-health-analytics/
	├── config.yaml               # user‑editable configuration
	├── config.default.yaml       # default template (committed)
	├── .gitignore                # ignore config.yaml (but keep .default)
	├── .gitattributes
	├── README.md
	├── requirements.txt
	├── scripts/
	│   ├── 00_generate_data.py   # uses config
	│   ├── run_all.py            # reads config, runs SQL scripts
	│   ├── 01_setup.sql
	│   ├── 02_load.sql
	│   ├── 03_transform.sql
	│   ├── 04_analysis.sql
	│   └── 05_performance.sql
	├── data/                     # gitignored – generated
	└── results/
```


### Quick Start
```
	git clone https://github.com/yourusername/example-health-analytics.git
	cd example-health-analytics
	python3.10 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	python scripts/00_generate_data.py
	# then run DuckDB SQL scripts in order (or use run_all.py)	
```
