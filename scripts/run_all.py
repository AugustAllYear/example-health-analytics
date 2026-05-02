import duckdb
import yaml
import sys

def main():
    # Load config
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Connect to DuckDB (persistent database)
    conn = duckdb.connect(config["db_file"])

    for sql_script in config["duckdb"]["sql_scripts"]:
        print(f"Executing {sql_script} ...")
        try:
            conn.execute(f"read('{sql_script}')")
        except Exception as e:
            print(f"Error in {sql_script}: {e}")
            sys.exit(1)

    conn.close()
    print("✅ All scripts executed successfully.")

if __name__ == "__main__":
    main()
