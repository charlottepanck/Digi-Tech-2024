import sqlite3

# functions


def fetch_author_id():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Author;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Author ID | Author's Name")
    for i in results:
        print(f"{i[0]:9} | {i[1]}")
    db.close


def fetch_all_series():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Series;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Series ID | Series Name")
    for i in results:
        print(f"{i[0]:9} | {i[1]}")


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
    print(f"Book ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}")
    db.close()


def fetch_all_members():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # forename column format
    sql1 = """SELECT Forename
    FROM Members ORDER BY Length(forename) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        fnlg = len(x)
        fnsp = (fnlg-4) * " "

    # email column format
    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        elg = len(x)
        esp = (elg-5) * " "

    # print table
    sql = "SELECT * FROM Members;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {fnsp}| Email {esp}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{fnlg}} | {i[2]:{elg}} | {i[3]}")
    db.close()


def fetch_specific_book(book_id):
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
    sql3 = """SELECT series_title
    FROM series ORDER BY Length(series_title) desc LIMIT 1;"""
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        slg = len(x)
        ssp = (slg-6) * " "

    # print table
    sql = f"""SELECT Books.book_id, Books.Title,
    Author.name, Series.series_title, Books.availability
    FROM Books
    LEFT JOIN Author ON Books.Author = Author.id
    LEFT JOIN Series ON Books.series = series.id
    WHERE book_id = {book_id};"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Book ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
    for i in results:
        print(f"""{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}""")
    db.close()


def fetch_borrowing_table():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # forename column format
    sql1 = """SELECT forename
    FROM Members ORDER BY Length(forename) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        fnlg = len(x)
        fnsp = (fnlg-4) * " "

    # title column format
    sql2 = "SELECT title FROM books ORDER BY Length(title) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-10) * " "

    # print table
    sql = """SELECT Members.forename, Books.title,
    Borrowing.issue_date, Borrowing.due_date
    FROM Borrowing
    LEFT JOIN Members ON borrowing.member_id = Members.member_id
    LEFT JOIN Books ON borrowing.book_id = Books.book_id;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Name {fnsp}| Book Title {tsp}| Due Date | Issue Date")
    for i in results:
        print(f"{i[0]:{fnlg}} | {i[1]:{tlg}} | {i[2]} | {i[3]}")
    db.close()


def fetch_specfic_borrowing_table(book_id):
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # forename column format
    sql1 = """SELECT forename FROM Members
    ORDER BY Length(forename) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        fnlg = len(x)
        fnsp = (fnlg-8) * " "

    # title column format
    sql2 = "SELECT title FROM books ORDER BY Length(title) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-10) * " "

    # print table
    sql = f"""SELECT Members.forename, Books.title,
    Borrowing.issue_date, Borrowing.due_date
    FROM Borrowing
    LEFT JOIN Members ON borrowing.member_id = Members.member_id
    LEFT JOIN Books ON borrowing.book_id = Books.book_id
    WHERE book_id = {book_id};"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Forename {fnsp}| Book Title {tsp}| Due Date | Issue Date")
    for i in results:
        print(f"{i[0]:{fnlg}} | {i[1]:{tlg}} | {i[2]:} | {i[3]} ")
    db.close()


# main code
print("""
Welcome to Libaray Database

Enter 1 to view a list of all books
Enter 2 to view a list of books borrowed by a specific member
Enter 3 to view a list of members who borrowed a specific book
Enter ... [Add and remove data, Edit/change data, Delete items,
Renew book, mark a book overdue (can i make this automatic?)]
""")
userinput = input('>> ').lower()
if userinput == '1':
    fetch_all_books()
    print("""
    Enter Book ID to view details (e.g. for The Great Gatsby input '50')
    """)
    book = input(">> ")
    fetch_specific_book(book)
    print("""
Enter 'a' to view avaiability details
Enter 'b' to view more books by author
Enter 'c' to view books in series
""")
    userinput = input('>> ').lower()
    if userinput == 'a':
        fetch_specfic_borrowing_table(book)
    if userinput == 'b':
        print('a')
