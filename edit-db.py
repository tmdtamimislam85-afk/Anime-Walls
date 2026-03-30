import sqlite3

def add_extension_to_filenames():
    # Database connect kora
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        # 1. Filename_mobile column update kora (jodi .png na thake)
        cursor.execute('''
            UPDATE wallpapers 
            SET filename_mobile = filename_mobile || '.png'
            WHERE filename_mobile NOT LIKE '%.png' 
            AND filename_mobile NOT LIKE '%.jpg' 
            AND filename_mobile NOT LIKE '%.jpeg'
        ''')

        # 2. Filename_desktop column update kora (jodi .png na thake)
        cursor.execute('''
            UPDATE wallpapers 
            SET filename_desktop = filename_desktop || '.png'
            WHERE filename_desktop NOT LIKE '%.png' 
            AND filename_desktop NOT LIKE '%.jpg' 
            AND filename_desktop NOT LIKE '%.jpeg'
        ''')

        conn.commit()
        print(f"✅ Success! All filenames without extensions have been updated with '.png'.")
        print(f"Rows affected: {cursor.rowcount}")

    except sqlite3.Error as e:
        print(f"❌ Error: {e}")
    
    finally:
        conn.close()

if __name__ == '__main__':
    add_extension_to_filenames()