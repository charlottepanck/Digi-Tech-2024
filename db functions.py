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
    sql2 = f"""SELECT Title FROM Books 
WHERE Author == {author_id} 
ORDER BY Length(title) desc LIMIT 1;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "

    # author column format
    sql3 = f"""SELECT name FROM author 
WHERE id == {author_id} 
ORDER BY Length(name) desc LIMIT 1;"""
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
    sql1 = f"""SELECT Title FROM Books
WHERE book_id = {book_id}
ORDER BY Length(title) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "

    # author column format
    sql2 = f"""SELECT Author.name FROM books
LEFT JOIN Author ON Author.id = books.author
WHERE book_id = {book_id}
ORDER BY Length(name) desc;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        alg = len(x)
        asp = (alg-6) * " "

    # series column format
    sql3 = f"""SELECT Series.series_title
FROM Books
LEFT JOIN Series on Books.series = series.id
WHERE book_id = {book_id}
ORDER BY Length(series_title) desc LIMIT 1;"""
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
    sql1 = """SELECT forename FROM Members 
ORDER BY Length(forename) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        fnlg = len(x)
        fnsp = (fnlg-4) * " "

    # title column format
    sql2 = """SELECT title FROM books 
ORDER BY Length(title) desc LIMIT 1;"""
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

def fetch_young_adults():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-4) * " "

    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    sql = "SELECT * FROM Members WHERE Age > 13 and Age < 18;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {forenamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{emaillength}} | {i[3]}")
    db.close()    

def fetch_all_minors():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-4) * " "

    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    sql = "SELECT * FROM Members WHERE Age < 12;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {forenamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{emaillength}} | {i[3]}")
    db.close()


def fetch_all_adults():
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-4) * " "


    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    sql = "SELECT * FROM Members WHERE Age > 17;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {forenamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{emaillength}} | {i[3]}")
    db.close()



def fetch_specific_series(id):
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # series id
    sqla = f"""SELECT series FROM Books 
WHERE series = {id};"""
    cursor.execute(sqla)
    results = cursor.fetchone()
    for i in results:
        seriesid = i   

    # title column format
    sql1 = f"""SELECT title FROM books
WHERE series == {id} 
ORDER BY Length(title) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        tlg = len(x)
        tsp = (tlg-5) * " "
    
    # author column format
    sql2 = f"""SELECT author.name
FROM books
LEFT JOIN author on author.id = books.author
WHERE series == {id} ORDER BY Length(name) desc LIMIT 1;"""
    cursor.execute(sql2)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        alg = len(x)
        asp = (alg-6) * " "

    # series column format
    sql3 = f"SELECT series_title FROM series WHERE id == {seriesid} ORDER BY Length(series_title) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        slg = len(x)
        ssp = (slg-6) * " "

    sql = f"""SELECT Books.title, Author.name, series.series_title, books.availability 
FROM Books
LEFT JOIN Author ON Books.author = Author.id
LEFT JOIN Series ON Books.series = Series.id
WHERE series = {id};"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Title {tsp}| Author {asp}| Series {ssp}| Availability")
    for i in results:
        print(f"{i[0]:{tlg}} | {i[1]:{alg}} | {i[2]:{slg}} | {i[3]}")
    db.close


def fetch_specific_member(member_id):
    db = sqlite3.connect('PraticeHome.db')
    cursor = db.cursor()

    # forename column format
    sql1 = f"""SELECT Forename
    FROM Members WHERE member_id = {member_id} ORDER BY Length(forename) desc LIMIT 1;"""
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        fnlg = len(x)
        fnsp = (fnlg-4) * " "

    # email column format
    sql3 = f"SELECT email FROM Members WHERE member_id = {member_id} ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        elg = len(x)
        esp = (elg-5) * " "

    # print table
    sql = f"SELECT * FROM Members WHERE member_id = {member_id};"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {fnsp}| Email {esp}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{fnlg}} | {i[2]:{elg}} | {i[3]}")
    db.close()

# main code
print("\nWelcome to Libaray Database\n")
while True:
    userinput = input("\nEnter 1 to view data\nEnter 2 to edit data\n>> ")
    if userinput == '1':
        userinput1 = input("\nEnter 'a' to view book data\nEnter 'b' to view member data\n>> ").lower()

        if userinput1 == 'a':
            fetch_all_books()
            userinput2 = input("\nEnter 'a' to filter results by author\nEnter 'b' to filter results by series\nEnter 'c' to view details of specific book\nEnter 'd' to filter results by avaliability\n>> ").lower()
            if userinput2 == 'a':
                fetch_author_id()
                print("\nEnter Author ID to view books by author (e.g. for J.K. Rowling input '27')")
                author = input("Author ID: ")
                fetch_books_by_author_id(author)
            if userinput2 == 'b':
                fetch_all_series()
                print("\nEnter Series ID to books in series (e.g. for Harry Potter input '9')")
                series = input("Series ID: ")
                fetch_specific_series(series)
            if userinput2 == 'c':
                print("\nEnter Book ID to view details (e.g. for Harry Potter and the Sorcerer's Stone input '56')")
                book = input("Book ID: ")
                fetch_specific_book(book)
            if userinput2 == 'd':
                userinput3 = input("\nEnter 'a' to view avaliable books\nEnter 'b' to view unavaliable books\n>> ")
                if userinput3 == 'a':
                    fetch_all_avaliable_books()
                if userinput3 == 'b':
                    fetch_all_unavaliable_books()
        if userinput1 == 'b':
            fetch_all_members()
            userinput4 = input("\nEnter 'a' to view members with a book checked out \nEnter 'b' to view details of specific member \nEnter 'c' to filter data by age\n>> ")
            if userinput4 == 'a':
                fetch_borrowing_table()
            if userinput4 == 'b':
                print("\nEnter member id to view details (e.g. for Belle Rungrojthanacorn input '9')")
                member = input("Member ID: ")
                fetch_specific_member(member)
            if userinput4 == 'c':
                userinput7 = input("\nEnter 'a' to filter by children (under 12)\nEnter 'b' to filter by young adults (ages 12 to 17)\nEnter 'c' to filter by Adults (18+)\n>> ")
                if userinput7 == 'a':
                    fetch_all_minors()
                if userinput7 == 'b':
                    fetch_young_adults()
                if userinput7 == 'c':
                    fetch_all_adults()



    if userinput == '2':
        userinput5 = input("\nEnter 'a' to add data\nEnter 'b' to remove data\nEnter 'c' to edit data\n>> ")
        if userinput5 == 'a':
            userinput6 = input("\nEnter 'a' to add a book\nEnter 'b' to add a member")
            if userinput6 == 'a':
                print('a')