import duckdb
import yaml
import sys
import os

def main():
    # Load config
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("config.yaml not found. Copy config.default.yaml to config.yaml and edit.")
        sys.exit(1)

    # Connect to DuckDB (creates file if not exists)
    db_file = config.get("db_file", "example-health.duckdb")
    conn = duckdb.connect(db_file)

    # Optionally create schemas (already in 01_setup.sql, but safe to have)
    for schema in config["duckdb"]["schemas"]:
        conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")

    # Execute each SQL script
    for script_path in config["sql_scripts"]:
        if not os.path.exists(script_path):
            print(f"File not found: {script_path}")
            sys.exit(1)

        print(f"Running {script_path} ...")
        try:
            with open(script_path, "r") as f:
                sql_script = f.read()
            conn.execute(sql_script)
        except Exception as e:
            print(f"Error in {script_path}: {e}")
            sys.exit(1)

    print("All scripts executed successfully.")
    conn.close()

if __name__ == "__main__":
    main()
