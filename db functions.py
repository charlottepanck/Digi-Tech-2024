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
    print(f"\nBook ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}")
    db.close()


def fetch_all_stand_alone_books():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # title column format
    sql1 = "SELECT Title FROM Books WHERE Series = 7 ORDER BY Length(title) desc LIMIT 1;"
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
    LEFT JOIN Series ON Books.series = Series.id
    WHERE Series = 7;"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Book ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
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
    LEFT JOIN Series ON Books.series = series.id
    WHERE availability = 'Avaliable';"""
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


def fetch_books_by_author_id(author_id):
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # title column format
    sql2 = f"SELECT Title FROM Books WHERE Author == {author_id} ORDER BY Length(title) desc LIMIT 1;"
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "

    # author column format
    sql3 = f"SELECT name FROM author WHERE id == {author_id} ORDER BY Length(name) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        alg = len(x)
        asp = (alg-6) * " "
    
    # series column format
    sql4 = f"""SELECT Series.series_title
FROM Books
LEFT JOIN Series on Books.series = series.id
WHERE author = {author_id}
ORDER BY Length(series_title) desc LIMIT 1;"""
    cursor.execute(sql4)
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
    WHERE author = {author_id};"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Book ID | Title {tsp}| Author {asp}| Series {ssp}| Avaiability")
    for i in results:
        print(f"{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}")
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
        print(f"{i[0]:>7} | {i[1]:{tlg}} | {i[2]:{alg}} | {i[3]:{slg}} | {i[4]}")
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
        fnsp = (fnlg-6) * " "

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
    borrowing.issue_date, Borrowing.due_date
    FROM Borrowing
    LEFT JOIN Members ON borrowing.member_id = Members.member_id
    LEFT JOIN Books ON borrowing.book_id = Books.book_id
    WHERE Borrowing.book_id = {book};"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member {fnsp}| Book Title {tsp}| Due Date | Issue Date")
    for i in results:
        print(f"{i[0]:{fnlg}} | {i[1]:{tlg}} | {i[2]:} | {i[3]} ")
    db.close()


def fetch_books_by_specific_author(book_id):
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # author id
    sqla = f"SELECT author FROM  Books WHERE book_id = {book_id};"
    cursor.execute(sqla)
    results = cursor.fetchone()
    for i in results:
        authorid = i

    # title column format
    sql1 = "SELECT title FROM books ORDER BY Length(title) desc LIMIT 1;"
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
    #sql = f"""SELECT Author.name, Books.title FROM Books LEFT JOIN Author ON Books.author = Author.id WHERE Books.book_id = {book_id};"""
    #cursor.execute(sql)
    #results = cursor.fetchall()
    #print(f"Author {asp}| Book Title {tsp}")
    #for i in results:
    #    print(f"{i[0]:{alg}} | {i[1]:{tlg}}")
    db.close()


# main code
print("\nWelcome to Libaray Database\n\nEnter 1 to view data\nEnter 2 to edit data")
userinput = input('>> ')
if userinput == '1':
    print("\nEnter 'a' to view book data\nEnter 'b' to view member data")
    userinput1 = input('>> ').lower()

    if userinput1 == 'a':
        fetch_all_books()
        print("\nEnter 'a' to filter results by author\nEnter 'b' to filter results by series\nEnter 'c' to view details of specific book")
        userinput2 = input('>> ').lower()
        if userinput2 == 'a':
            fetch_author_id()
            print("\nEnter Author ID to books by author (e.g. for J.K. Rowling input '27')")
            author = input("Author ID: ")
            fetch_books_by_author_id(author)
            


#        if userinput2 == 'b':
        if userinput2 == 'c':
            print("\nEnter Book ID to view details (e.g. for The Great Gatsby input '50')")
            book = input("Book ID: ")
            fetch_specific_book(book)





#            print("\nEnter 'a' to view avaiability details\nEnter 'b' to view more books by this author\nEnter 'c' to view books in this series\n")
#            userinput3 = input('>> ').lower()
#            if userinput3 == 'a':
#                fetch_specfic_borrowing_table(book)
#            if userinput3 == 'b':
#                fetch_books_by_specific_author(book)
#            if userinput3 == 'c':
#                print("[Table of bo`oks in this series]")
    if userinput1 == 'b':
        fetch_all_members()