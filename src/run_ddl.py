def run_ddl(cursor, ddl_path:str="files/RMS_DDL.sql"):
    with open(ddl_path, "r") as f:
        ddl_script = f.read()

    for i, statement in enumerate(ddl_script.split(";")):
        stmt = statement.strip()
        if stmt:
            try:
                print(f"Executing: {stmt[:50]}...")
                cursor.execute(stmt)
            except Exception as e:
                print(f"⚠️ Failed to execute statement [{i + 1}]: {stmt[:50]}")
                print(f"   Error: {e}")

