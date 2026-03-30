import sqlite3
from datetime import datetime

def create_live_wallpaper_db():
    db_name = "database-live.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Table toiri korar SQL Query with CHECK Constraint
    create_table_query = """
    CREATE TABLE IF NOT EXISTS wallpapers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL CHECK(category IN ('Mobile', 'Desktop')), 
        file_name TEXT NOT NULL,
        tags TEXT,
        downloads INTEGER DEFAULT 0,
        views INTEGER DEFAULT 0,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    try:
        cursor.execute(create_table_query)
        conn.commit()
        print(f"Success: '{db_name}' created with Strict Category (Mobile/Desktop).")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_live_wallpaper_db()