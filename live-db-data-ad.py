import sqlite3
from datetime import datetime

def manual_add_live_wallpaper():
    # Database connect kora
    conn = sqlite3.connect('database-live.db')
    cursor = conn.cursor()

    print("\n--- 🎬 Live Wallpaper Manual Entry ---")
    
    # User Input
    title = input("Enter Wallpaper Title: ")
    
    # Category Input
    print("Allowed Categories: [Mobile] or [Desktop]")
    category = input("Enter Category: ").strip().capitalize()
    
    # Strict Category Check
    if category not in ['Mobile', 'Desktop']:
        print("❌ Error: Invalid Category! Only 'Mobile' or 'Desktop' allowed.")
        return

    file_name = input("Enter Video Filename (e.g. anime_live.mp4): ")
    tags = input("Enter Tags (comma separated): ")
    
    # Automatic Upload Date (YYYY-MM-DD)
    upload_date = datetime.now().strftime("%Y-%m-%d")

    try:
        # Database Table Columns: title, category, file_name, tags, downloads, views, upload_date
        cursor.execute('''
            INSERT INTO wallpapers (title, category, file_name, tags, downloads, views, upload_date)
            VALUES (?, ?, ?, ?, 0, 0, ?)
        ''', (title, category, file_name, tags, upload_date))
        
        conn.commit()
        print(f"\n✅ Success! '{title}' has been added to the database.")
        print(f"📅 Upload Date: {upload_date}")
        
    except sqlite3.Error as e:
        print(f"\n❌ Database Error: {e}")
    
    finally:
        conn.close()

if __name__ == '__main__':
    while True:
        manual_add_live_wallpaper()
        choice = input("\nAdd another live wallpaper? (y/n): ")
        if choice.lower() != 'y':
            break