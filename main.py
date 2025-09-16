from src.connection import get_connection, load_config
from src.setup_stage import create_file_format, create_stage


def main():
    config = load_config()

    conn = get_connection(config=config)
    cursor = conn.cursor()

    format_name = config["etl"]["format_name"]
    stage_name = config["etl"]["stage_name"]

    create_file_format(cursor, format_name)
    create_stage(cursor, stage_name, format_name)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
