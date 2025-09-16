import tomllib

import snowflake.connector

def load_config(path="config/settings.toml"):
    with open(path, "rb") as f:
        return tomllib.load(f)

def get_connection():
    config = load_config()
    sf = config["snowflake"]

    return snowflake.connector.connect(
        account=sf["account"],
        user=sf["user"],
        password=sf["password"],
    )
