def create_file_format(cursor, format_name:str):
    cursor.execute(f"""CREATE OR REPLACE FILE FORMAT {format_name}
    TYPE = 'CSV'
    COMPRESSION = 'GZIP'
    SKIP_HEADER = 1
""")

def create_stage(cursor, stage_name:str, format_name:str):
    cursor.execute(f"""CREATE OR REPLACE STAGE {stage_name}
    DIRECTORY = ( ENABLE = true ) 
	ENCRYPTION = ( TYPE = 'SNOWFLAKE_SSE' ) 
    FILE_FORMAT = {format_name}
""")
