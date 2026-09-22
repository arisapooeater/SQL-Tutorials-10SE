"""Lesson 6 - Build a small books database script"""

import sqlite3

connection = sqlite3.connect("school.db")
# Cursor executes SQL commands and reads query results.
cursor = connection.cursor()

# Create the books table once, then resuse it on later runs.
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")

# Reset demo data so lesson output stays consistent
cursor.execute("DELETE FROM books")

# Add sample book records
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", 
("Holes", "Louis Sachar"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", 
("Wonder", "R. J. Palacio"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)",
("The Hobbit", "J. R. R. Tolkien"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)",
("The Izzuna Book", "Yuna and Izzy"))
cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)",
("I am cooler than probably everyone", "Isabella Usacheva"))
# Query all books in alphabetical order by title.
cursor.execute("SELECT title, author FROM books ORDER BY title")

# fetchall() gives a list of (title, author) tuples to loop through
for title, author in cursor.fetchall():
    print(f"{title} by {author}")

# Commit saves inserted rows to the database file.
connection.commit()
connection.close()