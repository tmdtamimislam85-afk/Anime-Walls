import sqlite3
import os

def manual_add_wallpaper():
    # Database connect kora
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    print("--- Manual Wallpaper Entry ---")
    
    # User Input
    title = input("Enter Wallpaper Title: ")
    mobile_img = input("Enter Mobile Image Filename (e.g. m1.jpg): ")
    desktop_img = input("Enter Desktop Image Filename (e.g. d1.jpg): ")
    
    print("\nCategories: Aesthetic, Action & Battle, Romantic / Couple, Dark / Sad Anime, Fantasy & Magic Worlds, Cyberpunk / Futuristic, Abstract / 3D, Chibi / Cute Anime, Nature + Anime Blend, Character-Focused Wallpapers")
    category = input("Enter Category: ")
    
    tags = input("Enter Tags (comma separated): ")

    try:
        # Database-e Data Insert kora
        cursor.execute('''
            INSERT INTO wallpapers (title, filename_mobile, filename_desktop, category, tags, downloads, views)
            VALUES (?, ?, ?, ?, ?, 0, 0)
        ''', (title, mobile_img, desktop_img, category, tags))
        
        conn.commit()
        print(f"\n✅ Success! '{title}' has been added to the database.")
        
    except sqlite3.Error as e:
        print(f"\n❌ Database Error: {e}")
    
    finally:
        conn.close()

if __name__ == '__main__':
    while True:
        manual_add_wallpaper()
        choice = input("\nAdd another one? (y/n): ")
        if choice.lower() != 'y':
            break