import sqlite3

""" SQLite3 Connection function methods 
    .connect() - connect to a database
    .cursor() - returns a cursor connected to the database
    .execute() - performs the SQL expression
    .commit() - commits current transaction
    .close() - terminates connection
    
"""
def connect():
    conn=sqlite3.connect('bookstore.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)") #creates a table (i.e. book) within bookstore database if it doesn't exist
    
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn=sqlite3.connect('bookstore.db')
    cur=conn.cursor()    
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect('bookstore.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(title='',author='',year='',isbn=''): 
    conn=sqlite3.connect('bookstore.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect('bookstore.db')
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect('bookstore.db')
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()


connect()

















































