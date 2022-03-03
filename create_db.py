import sqlite3

connection = sqlite3.connect('myapp.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS occupation (
    OccupationCode TEXT NOT NULL,
    RoadName TEXT NOT NULL,
    Description TEXT NOT NULL,
    Latitude REAL NOT NULL,
    Longitude REAL NOT NULL
)
""")

connection.commit()