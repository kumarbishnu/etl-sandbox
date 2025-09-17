from src.config_loader import get_config


def parse_mappings(mapping_path="files/mapping.txt"):
    mappings = {}
    with open(mapping_path, "r") as f:
        for line in f:
            line = line.strip()
            if "->" in line:
                table, file = map(str.strip, line.split("->"))
                mappings[table] = file
    return mappings


def parse_table_names(mapping_path="files/mapping.txt"):
    tables = []
    with open(mapping_path, "r") as f:
        for line in f:
            line = line.strip()
            if "->" in line:
                table = line.split("->")[0].strip()
                tables.append(table)
    return tables


def load_data(cursor):
    config = get_config()
    stage_name = config["etl"]["stage_name"]
    file_format = config["etl"]["format_name"]

    tables = parse_table_names()

    for table in tables:
        filename = f"{table}_0_0_0.csv.gz"
        print(f"Loading {filename} into {table}")
        try:
            cursor.execute(f"""COPY INTO {table} 
            FROM @{stage_name}/{filename} 
            FILE_FORMAT = (FORMAT_NAME = {file_format})
            ON_ERROR = 'CONTINUE'
""")
            results = cursor.fetchall()
            for row in results:
                print(row)
        except Exception as e:
            print(f"⚠️ Failed to load {filename} into {table}: {e}")
