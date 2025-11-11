from config.config_loader import get_config


def create_schema(cursor):
    config = get_config()
    schema = config["snowflake"]["schema"]
    cursor.execute(f"""CREATE OR REPLACE SCHEMA {schema}""")
