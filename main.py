from src.connection import get_connection


def main():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE(), CURRENT_SCHEMA();")
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


if __name__ == "__main__":
    main()
