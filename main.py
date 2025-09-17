from src.connection import get_connection
from src.create_schema import create_schema
from src.load_data import load_data
from src.run_ddl import run_ddl
from src.setup_stage import create_file_format, create_stage
from src.upload_files import upload_files


def main():
    conn = get_connection()
    cursor = conn.cursor()

    create_schema(cursor)
    create_file_format(cursor)
    create_stage(cursor)
    upload_files(cursor)
    run_ddl(cursor)
    load_data(cursor)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    # test_connection()
    main()
