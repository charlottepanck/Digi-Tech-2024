import sqlite3

# view functions

DB = 'PraticeHome.db'

# prints author and author id in a table
def fetch_author_id():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM Author;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Author ID | Author's Name")
    for i in results:
        print(f"{i[0]:9} | {i[1]}")
    db.close

# prints seires and series id in a table
def fetch_all_series():
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = "SELECT * FROM Series;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Series ID | Series Name")
    for i in results:
        print(f"{i[0]:9} | {i[1]}")

# prints all books in a table
def fetch_all_books():
    db = sqlite3.connect(DB)
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

# prints unavaliable books in a table
def fetch_all_unavaliable_books():
    db = sqlite3.connect(DB)
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

# prints avaliable books in a table
def fetch_all_avaliable_books():
    db = sqlite3.connect(DB)
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

# prints all members in a table
def fetch_all_members():
    db = sqlite3.connect(DB)
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

# prints all books by a specific author
def fetch_books_by_author_id(author_id):
    db = sqlite3.connect(DB)
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

# prints a specifc book in a table 
def fetch_specific_book(book_id):
    db = sqlite3.connect(DB)
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

# prints all books that are currently being borrowed and nae of borrower 
def fetch_borrowing_table():
    db = sqlite3.connect(DB)
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

# prints all members between ages 12 - 18 in a table
def fetch_young_adults():
    db = sqlite3.connect(DB)
    cursor = db.cursor()

    # name column formatting
    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-4) * " "

    # email column formatting
    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    # print table
    sql = "SELECT * FROM Members WHERE Age >= 12 and Age < 18;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {forenamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{emaillength}} | {i[3]}")
    db.close()

# prints all members under 12 in a table
def fetch_all_minors():
    db = sqlite3.connect(DB)
    cursor = db.cursor()

    # name format
    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-4) * " "

    # email format
    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    # print table
    sql = "SELECT * FROM Members WHERE Age < 12;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {forenamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{emaillength}} | {i[3]}")
    db.close()

# prints all members over 18 in a table
def fetch_all_adults():
    db = sqlite3.connect(DB)
    cursor = db.cursor()

    # name formet
    sql1 = "SELECT Forename FROM Members ORDER BY Length(forename) desc LIMIT 1;"
    cursor.execute(sql1)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        forenamelength = len(x)
        forenamespaces = (forenamelength-4) * " "

    # email format
    sql3 = "SELECT email FROM Members ORDER BY Length(email) desc LIMIT 1;"
    cursor.execute(sql3)
    results = cursor.fetchone()
    for i in results:
        x = (f"{i}")
        emaillength = len(x)
        emailspaces = (emaillength-5) * " "

    # print table
    sql = "SELECT * FROM Members WHERE Age > 17;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"Member ID | Name {forenamespaces}| Email {emailspaces}| Age")
    for i in results:
        print(f"{i[0]:>9} | {i[1]:<{forenamelength}} | {i[2]:{emaillength}} | {i[3]}")
    db.close()

# prints books from a specific series in a table
def fetch_specific_series(id):
    db = sqlite3.connect(DB)
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

# prints details of a specific member in a table
def fetch_specific_member(member_id):
    db = sqlite3.connect(DB)
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

# replaces author id with author name
def replace_authorid_with_name(author_id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()

    sql = f"SELECT Author.name FROM Author Where id == {author_id} LIMIT 1;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        return i[0]
    db.close()

# replaces series id with series name
def replace_seriesid_with_name(series_id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()

    sql = f"SELECT Series.series_title FROM Series Where id == {series_id} LIMIT 1;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for i in results:
        return i[0]
    db.close()

# check id
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
    

# edit functions

# adds book
def add_book(title, author_id, series_id):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"""INSERT INTO Books (title, author, series, availability)
VALUES ("{title}", "{author_id}", "{series_id}", "Avaliable");"""
    cursor.execute(sql)
    db.commit()

# adds a member
def add_member(forename, email, age):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"""INSERT INTO members (forename, email, age)
VALUES ('{forename}', '{email}', '{age}');"""
    cursor.execute(sql)
    db.commit()

# adds an author
def add_author(name):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"""INSERT INTO Author (name)
VALUES ("{name}");"""
    cursor.execute(sql)
    db.commit()

# adds a series
def add_series(series):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f'INSERT INTO Series (series_title) VALUES ("{series}");'
    cursor.execute(sql)
    db.commit()

# remove a book
def remove_book(bookid):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Books WHERE book_id = {bookid};"
    cursor.execute(sql)
    db.commit()

# remove an author
def remove_author(authorid):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Author WHERE id = {authorid};"
    cursor.execute(sql)
    db.commit()

# remove a series
def remove_series(seriesid):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Series WHERE id = {seriesid};"
    cursor.execute(sql)
    db.commit()

# remove a member
def remove_member(memberid):
    db = sqlite3.connect(DB)
    cursor = db.cursor()
    sql = f"DELETE FROM Members WHERE member_id = {memberid};"
    cursor.execute(sql)
    db.commit()


# main code
print("\nWelcome to Libaray Database")
while True:
    userinput = input("\nEnter 1 to view data\nEnter 2 to edit data\n>> ")
    if userinput == '1':
        # view data
        while True:
            userinput1 = input("\nEnter 'a' to view book data\nEnter 'b' to view member data\nEnter 'x' to go back\n>> ").lower()
            if userinput1 == 'a':
                # view book data
                fetch_all_books()
                while True:
                    userinput2 = input("\nEnter 'a' to filter results by author\nEnter 'b' to filter results by series\nEnter 'c' to view details of specific book\nEnter 'd' to filter results by avaliability\nEnter 'x' to go back\n>> ").lower()
                    if userinput2 == 'a':
                        # results filtered by author
                        fetch_author_id()
                        print("\nEnter Author ID to view books by author (e.g. for J.K. Rowling input '27')")
                        while True:
                            try:
                                author = input("Author ID: ")
                                check = author.isnumeric()
                                if check == True:
                                    fetch_books_by_author_id(author)
                                    break
                                if check == False:
                                    print("Oops! That is not a valid Author ID\n")
                            except TypeError:
                                print("Oops! That is either not a valid Author ID or this Author has no books in our Library.\n")
                    if userinput2 == 'b':
                        # results filtered by series
                        fetch_all_series()
                        print("\nEnter Series ID to books in series (e.g. for Harry Potter input '9')")
                        while True:
                            try:
                                series = input("Series ID: ")
                                check = series.isnumeric()
                                if check == True:
                                    fetch_specific_series(series)
                                    break
                                if check == False:
                                    print("Oops! That is not a valid Series ID.\n")
                            except TypeError:
                                print("Oops! That is either not a valid Series ID or there are no books in our library that are apart of this Series.\n")
                    if userinput2 == 'c':
                        # results of specific book
                        print("\nEnter Book ID to view details (e.g. for Harry Potter and the Sorcerer's Stone input '56')")
                        while True:
                            try:
                                book = input("Book ID: ")
                                check = book.isnumeric()
                                if check == True:
                                    fetch_specific_book(book)
                                    break
                                if check == False:
                                    print("Oops! That is not a valid Book ID.")
                            except TypeError:
                                print("Oops! That is not a valid Book ID.")
                    if userinput2 == 'd':
                        # avaliability
                        while True:
                            userinput3 = input("\nEnter 'a' to view avaliable books\nEnter 'b' to view unavaliable books\nEnter 'x' to go back\n>> ").lower()
                            if userinput3 == 'a':
                                # avaliable
                                fetch_all_avaliable_books()
                            if userinput3 == 'b':
                                # unavaliable
                                fetch_all_unavaliable_books()
                            elif userinput3 == 'x':
                                # go back
                                break
                    if userinput2 == 'x':
                        # go back
                        break
            if userinput1 == 'b':
                # view member data
                fetch_all_members()
                while True:
                    userinput4 = input("\nEnter 'a' to view members with a book checked out \nEnter 'b' to view details of specific member \nEnter 'c' to filter data by age\nEnter 'x' to go back\n>> ").lower()
                    if userinput4 == 'a':
                        # books checked out
                        fetch_borrowing_table()
                    if userinput4 == 'b':
                        # results of specific member
                        print("\nEnter member id to view details (e.g. for Belle Rungrojthanacorn input '9')")
                        while True:
                            try:
                                member = input("Member ID: ")
                                check = member.isnumeric()
                                if check == True:
                                    fetch_specific_member(member)
                                    break
                                if check == False:
                                    print("Oops! That is not a valid Member ID.")
                            except TypeError:
                                print("Oops! That is not a valid Member ID.")
                    if userinput4 == 'c':
                        # results by age
                        while True:
                            userinput7 = input("\nEnter 'a' to view children (under 12)\nEnter 'b' to view young adults (ages 12 to 17)\nEnter 'c' to view Adults (18+)\nEnter 'x' to go back\n>> ").lower()
                            if userinput7 == 'a':
                                # under 12
                                fetch_all_minors()
                            if userinput7 == 'b':
                                # aged 12 - 17
                                fetch_young_adults()
                            if userinput7 == 'c':
                                # aduls
                                fetch_all_adults()
                            if userinput7 == 'x':
                                # go back
                                break
                    if userinput4 == 'x':
                        # go back
                        break
            if userinput1 == 'x':
                # go back
                break

    if userinput == '2':
        # edit data
        while True:
            userinput8 = input("\nEnter pin to continue\nEnter 'x' to go back\n>> ")
            # password = 40981
            if userinput8 == '40981':
                while True:
                    userinput5 = input("\nEnter 'a' to add data\nEnter 'b' to remove data\nEnter 'x' to go back\n>> ").lower()
                    if userinput5 == 'a':
                        # add data
                        while True:
                            userinput6 = input("\nEnter 'a' to add a book\nEnter 'b' to add an author\nEnter 'c' to add a series\nEnter 'd' to add a member\nEnter 'x' to go back\n>> ").lower()
                            if userinput6 == 'a':
                                # add a title
                                title = input("\nTitle: ")
                                fetch_author_id()
                                flag = False
                                while True:
                                    # author
                                    author_id = input("Author ID: ")
                                    if author_id.isnumeric() == True:
                                        check = check_id("author", author_id)
                                        if check == True:
                                            # series
                                            fetch_all_series()
                                            while True:
                                                series_id = input("Series ID: ")
                                                if series_id.isnumeric() == True:
                                                    check1 = check_id("series", series_id)
                                                    if check1 == True:
                                                        while True:
                                                            # confirmation
                                                            confirmation = input(f"\nYou wish to add: Title: {title}, Author: {replace_authorid_with_name(author_id)}, Series: {replace_seriesid_with_name(series_id)}?\nEnter 'yes' to commit change\nEnter 'no' to cancel\n>> ").lower()
                                                            if confirmation == 'yes':
                                                                add_book(title, author_id, series_id)
                                                                flag = True
                                                                break
                                                            if confirmation == 'no':
                                                                flag = True
                                                                break
                                                            if confirmation != 'yes' or confirmation != 'no':
                                                                print('Oops! Invalid Input. Please input "yes" or "no".')
                                                    if check1 == False:
                                                        print("Oops! Invalid Series ID.\n")
                                                if series_id.isnumeric() == False:
                                                    print("Oops! Invalid Series ID.\n")
                                                if flag == True:
                                                    break
                                        if check == False:
                                                print("Oops! Invalid Author ID.\n")
                                    if author_id.isnumeric() == False:
                                        print("Oops! Invalid Author ID.\n")
                                    if flag == True:
                                        break
                            if userinput6 == 'b':
                                # add author name
                                name = input("\nAuthor's Full name: ")
                                # confirm
                                confirmation = input(f"\nYou wish to add: Author's Fullname: {name}?\nEnter 'yes' to commit change\nEnter 'no' to cancel\n>> ").lower()
                                if confirmation == 'yes':
                                    add_author(name)
                                if confirmation == 'no':
                                    break
                            if userinput6 == 'c':
                                # add series
                                series = input("\nSeries title: ")
                                # confirm
                                confirmation = input(f"\nYou wish to add: Series title: {series}?\nEnter 'yes' to commit change\nEnter 'no' to cancel\n>> ").lower()
                                if confirmation == 'yes':
                                    add_series(series)
                                if confirmation == 'no':
                                    break
                            if userinput6 == 'd':
                                # add member
                                flag = False
                                while True:
                                    if flag == True:
                                        break
                                    # name
                                    forename = input("\nFullname: ")
                                    check = ' ' in forename
                                    if check == False:
                                        print("Please enter First and Last name! (First and last name must be seperated by a space).")
                                    if check == True:
                                        #check for... a space ' ' as it must be a full name
                                        while True:
                                            if flag == True:
                                                break
                                            # email
                                            email = input("Email: ")
                                            check1 = '@' in email
                                            if check1 == False:
                                                print("Invalid email address.")
                                            if check1 == True:
                                            #check for contains '@'
                                                while True:
                                                    if flag == True:
                                                        break
                                                    # add age
                                                    age = input("Age: ")
                                                    if age.isnumeric() == False:
                                                        print("Invalid age.")
                                                    if age.isnumeric() == True:
                                                        #check for... is a number
                                                        while True:
                                                            confirmation = input(f"\nYou wish to add: Fullname: {forename}, Email adress: {email}, Age: {age}?\nEnter 'yes' to commit change\nEnter 'no' to cancel\n>> ").lower()
                                                            if confirmation == 'yes':
                                                                add_member(forename, email, age)
                                                                flag = True
                                                                break
                                                            if confirmation == 'no':
                                                                flag = True
                                                                break
                                                            if confirmation != 'yes' or confirmation != 'no':
                                                                print("Oops! Invalid input. Please enter 'yes' or 'no'.")
                                                                # use flags to get out of while loop
                            if userinput6 == 'x':
                                # go back
                                break

                    if userinput5 == 'b':
                        # remove data
                        while True:
                            userinput9 = input("\nEnter 'a' to remove a book\nEnter 'b' to remove an author\nEnter 'c' to remove a series\nEnter 'd' to remove a member\nEnter 'x' to go back\n>> ").lower()
                            if userinput9 == 'a':
                                # remove book
                                fetch_all_books()
                                # check numeric
                                bookid = input("Enter Book ID: ")
                                if bookid.isnumeric() == False:
                                    print("Invalid input. Try again!")
                                    break
                                if bookid.isnumeric() == True:
                                    # confrim
                                    confirmation = input(f"\nYou want to remove {bookid} from libray system?\nEnter 'yes' to remove book\nEnter 'no' to cancel\n>> ").lower()
                                    if confirmation == 'no':
                                        break
                                    if confirmation == 'yes':
                                        remove_book(bookid)
                            if userinput9 == 'b':
                                # remove author
                                fetch_author_id()
                                authorid = input("Enter Author ID: ")
                                if authorid.isnumeric() == False:
                                    print("Invalid input. Try again!")
                                    break
                                if authorid.isnumeric() == True:
                                    # confrim
                                    confirmation = input(f"\nYou want to remove {authorid} from library system?\nEnter 'yes' to remove author\nEnter 'no' to cancel\n>> ").lower()
                                    if confirmation == 'no':
                                        break
                                    if confirmation == 'yes':
                                        remove_author(authorid)
                            if userinput9 == 'x':
                                # go back
                                break
                            if userinput9 == 'c':
                                # remove a series
                                fetch_all_series()
                                seriesid = input("Enter Series ID: ")
                                if seriesid.isnumeric() == False:
                                    print("Invalid input. Try again!")
                                    break
                                if seriesid.isnumeric() == True:
                                    # confirm
                                    confirmation = input(f"\nYou wish to remove {seriesid} from library system?\nEnter 'yes' to remove series\nEnter 'no' to cancel\n>> ").lower()
                                    if confirmation == 'no':
                                        break
                                    if confirmation == 'yes':
                                        remove_series(seriesid)
                            if userinput9 == 'd':
                                # remove member
                                fetch_all_members()
                                memberid = input("Enter Member ID: ")
                                if memberid.isnumeric() == False:
                                    print("Invalid input. Try again!")
                                    break
                                if memberid.isnumeric() == True:
                                    while True:
                                        # confirm
                                        confirmation = input(f"\nYou wish to remove {memberid} from library system?\nEnter 'yes' to remove member\nEnter 'no' to cancel\n>> ").lower()
                                        if confirmation == 'no':
                                            break
                                        if confirmation == 'yes':
                                            remove_member(memberid)
                                            break
                                        if confirmation != 'yes' or confirmation != 'no':
                                            print("Oops! Invalid input. Please enter 'yes' or 'no'.")
                    if userinput5 == 'x':
                        # go back
                        break
            if userinput8 == 'x':
                # go back
                break
            else:
                print("Incorrect pin!")
