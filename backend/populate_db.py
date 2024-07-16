import sqlite3
import json

# Path to the JSON file
json_file_path = 'dishes.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Connect to the SQLite database
conn = sqlite3.connect('dishes.db')
c = conn.cursor()

# Create the dishes table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    dishId INTEGER PRIMARY KEY,
    dishName TEXT NOT NULL,
    imageUrl TEXT NOT NULL,
    isPublished BOOLEAN NOT NULL
)
''')

# Insert data into the dishes table
for dish in data:
    c.execute('''
    INSERT INTO dishes (dishId, dishName, imageUrl, isPublished) 
    VALUES (?, ?, ?, ?)
    ''', (dish['dishId'], dish['dishName'], dish['imageUrl'], dish['isPublished']))

# Commit the transaction and close the connection
conn.commit()
conn.close()

