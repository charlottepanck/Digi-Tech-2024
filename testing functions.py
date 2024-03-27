import sqlite3


def fetch_books_by_specific_author(book_id):
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # author id
    sqla = f"""SELECT author FROM Books 
WHERE book_id = {book_id};"""
    cursor.execute(sqla)
    results = cursor.fetchone()
    for i in results:
        authorid = i

    # title column format
    sql1 = f"""SELECT title FROM books WHERE author == {book_id}
ORDER BY Length(title) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "

    # series column format
    sql3 = """SELECT series_title
    FROM series ORDER BY Length(series_title) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        slg = len(x)
        ssp = (slg-6) * " "

    # author column format
    sql2 = f"SELECT name FROM author WHERE id == {authorid} ORDER BY Length(name) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        alg = len(x)
        asp = (alg-6) * " "

    # books by author
    sqlb = f"""SELECT Books.title, Author.name, series.series_title, books.availability 
FROM Books
LEFT JOIN Author ON Books.author = Author.id
LEFT JOIN Series ON Books.series = Series.id
WHERE author = {authorid};"""
    cursor.execute(sqlb)
    results = cursor.fetchall()
    print(f"Title {tsp}| Author {asp}| Series {ssp}| Availability")
    for i in results:
        print(f"{i[0]:{tlg}} | {i[1]:{alg}} | {i[2]:{slg}} | {i[3]}")

    # print table
    # sql = f"""SELECT Author.name, Books.title FROM Books LEFT JOIN Author ON Books.author = Author.id WHERE Books.book_id = {book_id};"""
    # cursor.execute(sql)
    # results = cursor.fetchall()
    # print(f"Author {asp}| Book Title {tsp}")
    # for i in results:
    #     print(f"{i[0]:{alg}} | {i[1]:{tlg}}")
    db.close()
while True:
    book = input("> ")
    fetch_books_by_specific_author(book)