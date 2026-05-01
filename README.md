# example-health-analytics
A healthcare analytics consultancy project. The client needed a local, reproducible analytics layer to identify cost drivers and provider efficiency. 

```
example-health-analytics/
├── .gitignore
├── .gitattributes
├── README.md
├── requirements.txt
├── scripts/
│   ├── 00_generate_data.py        # creates claims.parquet, providers.json
│   ├── 01_setup.sql               # create schemas (DuckDB native)
│   ├── 02_load.sql                # load data (CSV/Parquet/JSON)
│   ├── 03_transform.sql           # flatten JSON, create core tables
│   ├── 04_analysis.sql            # CTEs, complex queries, aggregations
│   ├── 05_performance.sql         # EXPLAIN, optimisation tricks
│   └── run_all.py                 # optional: executes all SQL scripts
├── data/                          # gitignored – generated locally
│   ├── claims.parquet
│   └── providers.json
└── results/
    └── sample_output.md

```


