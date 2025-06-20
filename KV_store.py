import sqlite3

class KV_store:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kv_store(key TEXT UNIQUE, value BLOB)")
        self.conn.commit()

    def get_key(self, key):
        self.cursor.execute("SELECT value FROM kv_store WHERE key = ?", (key,))
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def set_key(self, key, value):
        self.cursor.execute("INSERT OR REPLACE INTO kv_store (key, value) VALUES (?, ?)", (key, value))
        self.conn.commit()

    def delete(self, key):
        self.cursor.execute("DELETE FROM kv_store WHERE key = ?", (key,))
        self.conn.commit()


    def close_conn(self):
        self.conn.close()