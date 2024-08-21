import os
import mysql.connector
from mysql.connector import Error
from Book import Book


class Library:
    def __init__(
        self,
        host="mysql-service",
        user="root",
        password="R00t1234!@#$",
        db_name="library",
    ):
        self.books = []
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.conn = self.connect_to_db()
        if self.conn:
            self.create_table()
            self.load_books_from_db()

    def connect_to_db(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )
            print("Connection to database established successfully.")
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS books (
                    book_id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    author VARCHAR(255) NOT NULL,
                    year INT,
                    isbn VARCHAR(20) UNIQUE NOT NULL
                )
            """
            )
            self.conn.commit()
            print("Table 'books' created or verified successfully.")
        except Error as e:
            print(f"Error creating table: {e}")

    def load_books_from_db(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            for row in rows:
                self.books.append(Book(row[1], row[2], row[4], row[3]))
        except Error as e:
            print(f"Error loading books: {e}")

    def add_book(self, book):
        try:
            for b in self.books:
                if b.isbn == book.isbn:
                    return "Book already exists"
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO books (title, author, year, isbn)
                VALUES (%s, %s, %s, %s)
            """,
                (book.title, book.author, book.year, book.isbn),
            )
            self.conn.commit()

            # Update the in-memory books list
            self.books.append(book)
            return "Book added"
        except mysql.connector.IntegrityError:
            return "Book already exists"
        except Error as e:
            return f"Error adding book: {e}"

    def display_books(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            return "\n".join(f"{row[1]}, {row[2]}, {row[3]}, {row[4]}" for row in rows)
        except Error as e:
            return f"Error displaying books: {e}"

    def find_book(self, isbn):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
            row = cursor.fetchone()
            if row:
                return f"{row[1]}, {row[2]}, {row[3]}, {row[4]}"
            return "Book not found"
        except Error as e:
            return f"Error finding book: {e}"

    def remove_book(self, isbn):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM books WHERE isbn = %s", (isbn,))
            self.conn.commit()
            if cursor.rowcount > 0:
                # Update the in-memory books list
                self.books = [book for book in self.books if book.isbn != isbn]
                return "Book removed"
            return "Book not found"
        except Error as e:
            return f"Error removing book: {e}"

    def save_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.year},{book.isbn}\n")
            return "Books saved to file."
        except Exception as e:
            return str(e)

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            return "File not found"
        try:
            with open(filename, "r") as file:
                for line in file:
                    title, author, year, isbn = line.strip().split(",")
                    book = Book(title, author, isbn, year)
                    self.add_book(book)
            return "Books loaded from file."
        except Exception as e:
            return str(e)

    def __del__(self):
        if self.conn:
            self.conn.close()
            print("Connection to database closed successfully.")
