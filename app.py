from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Database connection function
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row # Column name diye data access korar jonno
    return conn

@app.route('/')
def home():
    return render_template('index.html')

# Search page logic
@app.route('/main')
def main_page():
    query = request.args.get('q', '').strip()
    category = request.args.get('cat', '').strip() # Category dhorar jonno jog kora holo
    wp_type = request.args.get('type', '')
    
    conn = get_db()
    sql = "SELECT * FROM wallpapers WHERE 1=1"
    params = []

    # Search query thakle seta filter korbe
    if query:
        sql += " AND (title LIKE ? OR tags LIKE ? OR category LIKE ?)"
        params.extend(['%' + query + '%', '%' + query + '%', '%' + query + '%'])
    
    # Category select korle sudu sei category-r result dekhabe
    if category:
        sql += " AND category = ?"
        params.append(category)
    
    sql += " ORDER BY id DESC"
    
    wallpapers = conn.execute(sql, params).fetchall()
    conn.close()
    
    # current_cat pathano hocche jate active button chinhte pare
    return render_template('main.html', wallpapers=wallpapers, query=query, wp_type=wp_type, current_cat=category)



# download page
@app.route('/download/<int:wp_id>')
def download_page(wp_id):
    conn = get_db()
    # 1. Main wallpaper details ana
    wallpaper = conn.execute('SELECT * FROM wallpapers WHERE id = ?', (wp_id,)).fetchone()
    
    if wallpaper is None:
        conn.close()
        return "Wallpaper not found", 404

    # 2. Related wallpapers ana (ek-i category-r onno wallpaper)
    related = conn.execute('''
        SELECT * FROM wallpapers 
        WHERE category = ? AND id != ? 
        LIMIT 4
    ''', (wallpaper['category'], wp_id)).fetchall()

    conn.close()
    return render_template('download.html', wp=wallpaper, related=related)



# Live Wallpaper database connection function
def get_live_db():
    conn = sqlite3.connect('database-live.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/live')
def live_page():
    conn = get_live_db()
    # Database theke shob live wallpaper fetch kora hocche
    # Page load-e shob data fetch hobe, filter hobe JavaScript diye
    wallpapers = conn.execute('SELECT * FROM wallpapers ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('live-wallpaper.html', wallpapers=wallpapers)


@app.route('/live-search')
def live_search():
    query = request.args.get('q', '').strip()
    
    conn = get_live_db() # Live wallpaper database connect kora
    
    # Query logic: Title ba Tags match korle result dekhabe
    if query:
        sql = "SELECT * FROM wallpapers WHERE title LIKE ? OR tags LIKE ? ORDER BY id DESC"
        wallpapers = conn.execute(sql, ('%' + query + '%', '%' + query + '%')).fetchall()
    else:
        # Query faka thakle shob wallpaper dekhabe
        wallpapers = conn.execute("SELECT * FROM wallpapers ORDER BY id DESC").fetchall()
        
    conn.close()
    
    # live-main.html page-e data pathano hocche
    return render_template('live-main.html', wallpapers=wallpapers, query=query)


@app.route('/live-download/<int:wp_id>')
def live_download_page(wp_id):
    conn = get_live_db() # database-live.db-er sathe connect hobe
    
    # ১. Main wallpaper details ana
    wallpaper = conn.execute('SELECT * FROM wallpapers WHERE id = ?', (wp_id,)).fetchone()
    
    if wallpaper is None:
        conn.close()
        return "Wallpaper not found", 404

    # ২. Related wallpapers (একই ক্যাটাগরির অন্য ভিডিও)
    # LIMIT 4 diye amra sudhu ৪টি related video nibo
    related = conn.execute('''
        SELECT * FROM wallpapers 
        WHERE category = ? AND id != ? 
        ORDER BY RANDOM() LIMIT 4
    ''', (wallpaper['category'], wp_id)).fetchall()

    conn.close()
    return render_template('live-download.html', wp=wallpaper, related=related)


@app.route('/app-coming-soon')
def app_coming_soon():
    return render_template('mobile-app.html')


if __name__ == '__main__':
    app.run(debug=True)