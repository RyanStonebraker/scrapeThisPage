import sqlite3

conn = sqlite3.connect("scrape.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='cats'
""")

if not cursor.fetchone()[0]:
    cursor.execute("""
        CREATE TABLE cats(
            id integer PRIMARY KEY,
            firstname varchar(255),
            lastname varchar(255),
            link varchar(255),
            price int
        );
    """)

conn.commit()
