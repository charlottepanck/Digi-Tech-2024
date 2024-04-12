import sqlite3

def fetch_all_books():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # title column format
    sql1 = "SELECT Title FROM Books ORDER BY Length(title) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "

    # author column format
    sql2 = "SELECT name FROM author ORDER BY Length(name) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        alg = len(x)
        asp = (alg-6) * " "

    # series column format
    sql3 = """SELECT series_title FROM series
    ORDER BY Length(series_title) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        slg = len(x)
        ssp = (slg-6) * " "

    # print table
    sql = """SELECT Books.book_id, Books.Title,
    Author.name, Series.series_title, Books.availability
    FROM Books
    LEFT JOIN Author ON Books.Author = Author.id
    LEFT JOIN Series ON Books.series = series.id;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"\nBook ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}")
    db.close()


def fetch_all_avaliable_books():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # title column format
    sql1 = "SELECT Title FROM Books WHERE availability = 'Avaliable' ORDER BY Length(title) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "

    # author column format
    sql2 = """SELECT author.name
FROM books 
LEFT JOIN author ON books.author = author.id
WHERE availability = 'Avaliable'
ORDER BY Length(name) desc LIMIT 1;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        alg = len(x)
        asp = (alg-6) * " "

    # series column format
    sql3 = """SELECT series.series_title
FROM books 
LEFT JOIN series ON books.series = series.id
WHERE availability = 'Avaliable'
ORDER BY Length(series_title) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        slg = len(x)
        ssp = (slg-6) * " "

    # print table
    sql = """SELECT Books.book_id, Books.Title,
    Author.name, Series.series_title, Books.availability
    FROM Books
    LEFT JOIN Author ON Books.Author = Author.id
    LEFT JOIN Series ON Books.series = series.id
    WHERE availability = 'Avaliable';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Book ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}")
    db.close()


def fetch_all_unavaliable_books():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # title column format
    sql1 = "SELECT Title FROM Books WHERE availability = 'Unavaliable' ORDER BY Length(title) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "

    # author column format
    sql2 = """SELECT author.name
FROM books 
LEFT JOIN author ON books.author = author.id
WHERE availability = 'Unavaliable'
ORDER BY Length(name) desc LIMIT 1;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        alg = len(x)
        asp = (alg-6) * " "

    # series column format
    sql3 = """SELECT series.series_title
FROM books 
LEFT JOIN series ON books.series = series.id
WHERE availability = 'Unavaliable'
ORDER BY Length(series_title) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        slg = len(x)
        ssp = (slg-6) * " "

    # print table
    sql = """SELECT Books.book_id, Books.Title,
    Author.name, Series.series_title, Books.availability
    FROM Books
    LEFT JOIN Author ON Books.Author = Author.id
    LEFT JOIN Series ON Books.series = series.id
    WHERE availability = 'Unavaliable';"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Book ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}")
    db.close()

def add_book(title, author_id, series_id, avaliability):
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()
    sql = f"""INSERT INTO Books (title, author, series, availability)
VALUES ('{title}', '{author_id}', '{series_id}', '{avaliability}');"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close()

def check_id(table, userinputid):
    #   checks if inputed id exists
    db = sqlite3.connect("PraticeHome.db")
    cursor = db.cursor()
    sql = f"SELECT id FROM {table} WHERE {userinputid} = id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    x = len(results)
    db.close()
    if x <= 0:
        return False
    else:    
        return True

a = check_id("author", "qej")
if a == False:
    print("False")
if a == True:
    print("True")