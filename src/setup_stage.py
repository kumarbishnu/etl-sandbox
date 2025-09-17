from src.config_loader import get_config


def create_file_format(cursor):
    config = get_config()
    format_name = config["etl"]["format_name"]

    cursor.execute(f"""CREATE OR REPLACE FILE FORMAT {format_name}
    TYPE = 'CSV'
    COMPRESSION = 'GZIP'
    FIELD_DELIMITER = '|'
    SKIP_HEADER = 1
    NULL_IF = ('\\\\N')
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    DATE_FORMAT = 'YYYY-MM-DD'
""")

def create_stage(cursor):
    config = get_config()
    format_name = config["etl"]["format_name"]
    stage_name = config["etl"]["stage_name"]

    cursor.execute(f"""CREATE OR REPLACE STAGE {stage_name}
    DIRECTORY = ( ENABLE = true ) 
	ENCRYPTION = ( TYPE = 'SNOWFLAKE_SSE' ) 
    FILE_FORMAT = {format_name}
""")
