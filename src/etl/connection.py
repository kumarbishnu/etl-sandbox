import snowflake.connector

from config.config_loader import get_config


def get_connection():
    config = get_config()
    sf = config["snowflake"]

    return snowflake.connector.connect(
        account=sf["account"],
        user=sf["user"],
        password=sf["password"],
        warehouse=sf["warehouse"],
        database=sf["database"],
        role=sf["role"],
        schema=sf["schema"],
    )


def check_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE(), CURRENT_SCHEMA();"
        )
        result = cursor.fetchone()
        print("✅ Connection successful!")
        print("User:", result[0])
        print("Role:", result[1])
        print("Database:", result[2])
        print("Schema:", result[3])
        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Connection failed:", e)
