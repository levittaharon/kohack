import sqlite3
class expire:
    def __init__(self,category):
        pass
    
    def check_expired(self):
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute(f"DELETE FROM {category} WHERE time_expire <= datetime('now');")
        
        
        con.close()
"""
#thes are all for testing
instance = expire()
con = sqlite3.connect("expire.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (time);")
cur.execute("INSERT INTO test (time) VALUES ('2023-02-25 10:10:10')")
con.commit()
instance.check_expired()
"""

