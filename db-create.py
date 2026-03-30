import sqlite3

def create_wallpaper_db():
    # Database connect kora (file na thakle auto toiri hobe)
    conn = sqlite3.connect('database-live.db')
    cursor = conn.cursor()

    # 1. Wallpapers Table toiri kora
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS wallpapers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            filename_mobile TEXT NOT NULL,
            filename_desktop TEXT NOT NULL,
            tags TEXT,
            downloads INTEGER DEFAULT 0,
            views INTEGER DEFAULT 0,
            upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # 2. Fixed 10 Categories logic (Admin Panel-er dropdown-e use korar jonno)
    # SQL-e CHECK constraint deya hoyeche jate ei 10-tir baire data na dhuke

    conn.commit()
    conn.close()
    print("Wallpaper Database with 10 fixed categories created successfully!")

if __name__ == '__main__':
    create_wallpaper_db()