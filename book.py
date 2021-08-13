import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
    DROP TABLE IF EXISTS books
""")

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        pages INTERGER,
        current_page INTERGER
    )
""")

cursor.execute("""
    INSERT INTO books VALUES(
        0, 'A great book', 213, 27
    )
""")
cursor.execute("""
    INSERT INTO books VALUES(
        1, 'Another great book', 395, 27
    )
""")
rows = cursor.execute("""
    SELECT id FROM books WHERE title = 'A great book'
""")

def calculate_read_time():
    read_speed = input("How many pages do you read per minute? ")
    for row in rows:
        read_time = row[1] / float(read_speed) / 60
        print('book:' )
    print(row)

# cursor.execute("""
#     DELETE FROM books WHERE id=0
#     )
# """)
cursor.execute("""
    UPDATE books SET current_page = 100 WHERE id=1
    )
""")

connection.commit()

connection.close()
