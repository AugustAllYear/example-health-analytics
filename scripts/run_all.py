import duckdb
import yaml
import sys

def main():
    # Load config
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("config.yaml not found. Copy config.default.yaml to config.yaml and edit.")
        sys.exit(1)

    # Connect to DuckDB
    conn = duckdb.connect(config["db_file"])

    # Create schemas if not exist (optional, already in 01_setup.sql)
    for schema in config["duckdb"]["schemas"]:
        conn.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")

    # Execute SQL scripts in order
    for script_path in config["sql_scripts"]:
        print(f"▶️ Running {script_path} ...")
        try:
            conn.execute(f"read('{script_path}')")
        except Exception as e:
            print(f"❌ Error in {script_path}: {e}")
            sys.exit(1)

    print("All scripts executed successfully.")
    conn.close()

if __name__ == "__main__":
    main()
