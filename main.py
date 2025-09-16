from src.connection import get_connection, test_connection
from src.setup_stage import create_file_format, create_stage
from src.upload_and_load import upload_files


def main():
    conn = get_connection()
    cursor = conn.cursor()

    # create_file_format(cursor)
    # create_stage(cursor)
    upload_files(cursor)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    # test_connection()
    # upload_files(None)
    main()
