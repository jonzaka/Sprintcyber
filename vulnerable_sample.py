import sqlite3

def search_user(name):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    # Inseguro (para o SAST identificar): concatenação em SQL
    cur.execute("SELECT * FROM users WHERE name = '%s'" % name)
    return cur.fetchall()
