from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

passwordEntry = None

# Function to open admin window
def create_adminWindow():
    adminWindow = Toplevel()
    adminWindow.geometry("720x360")
    adminWindow.title("Admin Window")
    adminWindow.config(bg="#cbc1bf")
    
    # Admin label
    adminLabel = Label(adminWindow, text="Admin Page", font=('Times New Roman', 40), bg="#cbc1bf")
    adminLabel.pack(pady=40)
    
    # Line divider
    lineDivider = Frame(adminWindow, height=1, bd=1, relief='sunken', bg="black")
    lineDivider.pack(fill='x')
    
    # Admin buttons
    adminFrame = Frame(adminWindow, bg="#cbc1bf")
    adminFrame.pack(pady=20)
    
    addBooks = Button(adminFrame, text='Add Books', command=create_addBooksWindow, width=15, height=2, bg="#f0f0f0", fg="#000000", font=('Helvetica', 10), relief='raised', bd=5)
    addBooks.pack(side='left', padx=10)
    
    removeBooks = Button(adminFrame, text='Remove Books', command=create_removeBooksWindow, width=15, height=2, bg="#f0f0f0", fg="#000000", font=('Helvetica', 10), relief='raised', bd=5)
    removeBooks.pack(side='left', padx=10)
    
    viewBooks = Button(adminFrame, text='View Books', command=create_viewBooksWindow, width=15, height=2, bg="#f0f0f0", fg="#000000", font=('Helvetica', 10), relief='raised', bd=5)
    viewBooks.pack(side='left', padx=10)
    
    adminFrame2 = Frame(adminWindow, bg="#cbc1bf")
    adminFrame2.pack(pady=20)
    
    viewBorrowRecords = Button(adminFrame2, text="Borrow Records", command=create_viewBorrowerWindow, width=15, height=2, bg="#f0f0f0", fg="#000000", font=('Helvetica', 10), relief='raised', bd=5)
    viewBorrowRecords.pack(side='left', padx=10)
    
    viewBorrowedBooks = Button(adminFrame2, text="Borrowed Books", command=create_viewBorrowedBooksWindow, width=15, height=2, bg="#f0f0f0", fg="#000000", font=('Helvetica', 10), relief='raised', bd=5)
    viewBorrowedBooks.pack(side='left', padx=10)
    
    adminWindow.resizable(False, False)

# user window choices    
def create_userWindow():
    userWindow = Toplevel()
    userWindow.geometry("720x400")
    userWindow.title("User Window")
    userWindow.config(bg="#cbc1bf")
    
    # Adding the label
    userLabel = Label(userWindow, text="User Page", font=("Times New Roman", 40), bg="#cbc1bf")
    userLabel.pack(pady=20)
    
    # Line divider
    lineDivider = Frame(userWindow, height=2, bd=1, relief='solid', bg="black")
    lineDivider.pack(fill='x', padx=20, pady=10)
    
    userFrame = Frame(userWindow, bg="#cbc1bf")
    userFrame.pack(pady=20)
    
    # Buttons
    borrowBooks = Button(userFrame, text="Borrow Books", command=create_borrowBooksWindow, width=15, height=2, font=('Helvetica', 13), relief='raised', bd=5)
    borrowBooks.pack(side='left', padx=10)
    
    returnBooks = Button(userFrame, text="Return Book", command=create_returnBookWindow, width=15, height=2, font=('Helvetica', 13), relief='raised', bd=5)
    returnBooks.pack(side='left', padx=10)
    
    viewBooks = Button(userFrame, text="View Available Books", command=create_AvailableBooksWindow, width=20, height=2, font=('Helvetica', 13), relief='raised', bd=5)
    viewBooks.pack(side='left', padx=10)
    
    userWindow.resizable(False, False)

# window for borrowing books
def create_borrowBooksWindow():
    borrowBooksWindow = Toplevel()
    borrowBooksWindow.geometry("920x480")
    borrowBooksWindow.title("Borrow Books")
    borrowBooksWindow.config(bg="#cbc1bf")
    
    # Adding the label
    borrowBooksLabel = Label(borrowBooksWindow, text="Borrow a Book", font=("Times New Roman", 30), bg="#cbc1bf")
    borrowBooksLabel.pack(pady=20)
    
    # Line divider
    lineDivider = Frame(borrowBooksWindow, height=2, bd=1, relief='solid', bg="#333333")
    lineDivider.pack(fill='x', padx=20, pady=10)
    
    borrowFrame = Frame(borrowBooksWindow, bg="#cbc1bf")
    borrowFrame.pack(pady=20)
    
    # Borrower Information
    borrowerInfoLabel = Label(borrowFrame, text="Enter the details below", font=("Helvetica", 15, "bold"), bg="#cbc1bf")
    borrowerInfoLabel.pack(pady=10)
    
    firstRowFrame = Frame(borrowFrame, bg="#cbc1bf")
    firstRowFrame.pack(pady=10)
    
    borrowerNameLabel = Label(firstRowFrame, text="Borrower Name:", font=("Helvetica", 15), bg="#cbc1bf")
    borrowerNameLabel.pack(side='left', padx=(40,10))
    borrowerNameEntry = Entry(firstRowFrame, width=20, font=("Helvetica", 15))
    borrowerNameEntry.pack(side='left', padx=10)
    
    bookIdLabel = Label(firstRowFrame, text="Book ID:", font=("Helvetica", 15), bg="#cbc1bf")
    bookIdLabel.pack(side='left', padx=(10,40))
    bookIdEntry = Entry(firstRowFrame, width=20, font=("Helvetica", 15))
    bookIdEntry.pack(side='left', padx=10)
    
    secondRowFrame = Frame(borrowFrame, bg="#cbc1bf")
    secondRowFrame.pack(pady=10)
    
    borrowDateLabel = Label(secondRowFrame, text="Borrow Date:", font=("Helvetica", 15), bg="#cbc1bf")
    borrowDateLabel.pack(side='left', padx=40)
    borrowDateEntry = Entry(secondRowFrame, width=20, font=("Helvetica", 15))
    borrowDateEntry.pack(side='left', padx=10)
    
    returnDateLabel = Label(secondRowFrame, text="Return Date:", font=("Helvetica", 15), bg="#cbc1bf")
    returnDateLabel.pack(side='left', padx=10)
    returnDateEntry = Entry(secondRowFrame, width=20, font=("Helvetica", 15))
    returnDateEntry.pack(side='left', padx=10)
    
    noteLabel = Label(borrowFrame, text="Note: Use the format YYYY-MM-DD for dates.", font=("Helvetica", 15, "italic"), bg="#cbc1bf")
    noteLabel.pack(pady=10)
    
    def borrowBook():
        borrowerName = borrowerNameEntry.get()
        borrowDate = borrowDateEntry.get()
        returnDate = returnDateEntry.get()
        book_ID = bookIdEntry.get()
        if borrowerName and borrowDate and returnDate and book_ID:
            borrowBookDB(borrowerName, borrowDate, returnDate, book_ID)
            borrowBooksWindow.destroy()
    
    submitButton = Button(borrowBooksWindow, text="Borrow Book", command=borrowBook, width=20, height=2, font=("Helvetica", 10, "bold"), relief='raised', bd=5)
    submitButton.pack(pady=20)
    
    borrowBooksWindow.resizable(False, False)

# database function for borrowing books
def borrowBookDB(borrowerName, borrowDate, returnDate, book_ID):
    connection = connectDB()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        
        # Check if the book is already borrowed
        cursor.execute("SELECT * FROM borrowedBooks WHERE book_ID = %s", (book_ID,))
        if cursor.fetchone():
            messagebox.showerror("Error", "This book has already been borrowed!")
            return
        
        # Retrieve the book details from the books table
        cursor.execute("SELECT * FROM books WHERE book_ID = %s", (book_ID,))
        book = cursor.fetchone()
        if not book:
            messagebox.showerror("Error", "Book not found!")
            return
        
        title, author, publisher, publicationYear, ddc = book[1], book[2], book[3], book[4], book[5]
        
        # Insert into borrower table and get the borrowID
        query_borrower = """
            INSERT INTO borrower (borrowerName, borrowDate, returnDate, book_ID)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query_borrower, (borrowerName, borrowDate, returnDate, book_ID))
        borrowID = cursor.lastrowid
        
        # Insert into borrowed_books table with the specified columns
        query_borrowed_books = """
            INSERT INTO borrowedBooks (book_ID, title, author, publisher, publicationYear, ddc, borrowID, borrowDate, returnDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_borrowed_books, (book_ID,title, author, publisher, publicationYear, ddc, borrowID, borrowDate, returnDate))
        
        connection.commit()
        messagebox.showinfo("Success", "Borrower and borrowed book added successfully!")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error adding borrower: {error}")
    finally:
        cursor.close()
        connection.close()
# window to see the books available
def create_AvailableBooksWindow():
    availableBooksWindow = Toplevel()
    availableBooksWindow.geometry("1280x720")
    availableBooksWindow.title("Available Books")
    availableBooksWindow.config(bg="#cbc1bf")
    
    # Adding the label
    availableBooksLabel = Label(availableBooksWindow, text="Available Books in the Library", font=("Times New Roman", 30), bg="#cbc1bf")
    availableBooksLabel.pack(pady=20)
    
    # Creating the frame to ensure background color is visible
    treeFrame = Frame(availableBooksWindow, bg="#cbc1bf")
    treeFrame.pack(fill=BOTH, expand=True, padx=20, pady=20)
    
    tree = ttk.Treeview(treeFrame, columns=("book_ID", "title", "author", "publisher", "publicationYear", "ddc"), show='headings')
    tree.heading("book_ID", text="ID")
    tree.heading("title", text="Title")
    tree.heading("author", text="Author")
    tree.heading("publisher", text="Publisher")
    tree.heading("publicationYear", text="Publication Year")
    tree.heading("ddc", text="DDC")
    
    tree.column("book_ID", width=50)
    tree.column("title", width=200)
    tree.column("author", width=150)
    tree.column("publisher", width=150)
    tree.column("publicationYear", width=100)
    tree.column("ddc", width=100)
    
    tree.pack(fill=BOTH, expand=True)
    
    fetchAvailableBooks(tree)
def fetchAvailableBooks(tree):
    books = getAvailableBooks()
    for book in books:
        tree.insert('', END, values=book)
def getAvailableBooks():
    connection = connectDB()
    if connection is None:
        return []
    try:
        cursor = connection.cursor()
        query = """
            SELECT book_ID, title, author, publisher, publicationYear, ddc 
            FROM books 
            WHERE book_ID NOT IN (SELECT book_ID FROM borrowedBooks)
        """
        cursor.execute(query)
        available_books = cursor.fetchall()
        return available_books
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error fetching available books: {error}")
        return []
    finally:
        cursor.close()
        connection.close()
# window for returning book 
def create_returnBookWindow():
    returnBookWindow = Toplevel()
    returnBookWindow.geometry("720x360")
    returnBookWindow.title("Return Book")
    returnBookWindow.config(bg="#cbc1bf")
    
    # Adding the label
    returnBooksLabel = Label(returnBookWindow, text="Return the Book to the Library", font=("Times New Roman", 30), bg="#cbc1bf")
    returnBooksLabel.pack(pady=20)
    
    # Line divider
    lineDivider = Frame(returnBookWindow, height=2, bd=1, relief='solid', bg="black")
    lineDivider.pack(fill='x', padx=20, pady=10)
    
    returnBookFrame = Frame(returnBookWindow, bg="#cbc1bf")
    returnBookFrame.pack(pady=10)
    
    bookIdLabel = Label(returnBookFrame, text="Book ID:", font=("Helvetica", 15, "bold"), bg="#cbc1bf", fg="#000000")
    bookIdLabel.pack(side='left', padx=10)
    bookIdEntry = Entry(returnBookFrame, width=20, font=("Helvetica", 15))
    bookIdEntry.pack(side='left', padx=10)
    
    def returnBook():
        book_ID = bookIdEntry.get()
        if book_ID:
            returnBookDB(book_ID)
            returnBookWindow.destroy()
    
    submitButton = Button(returnBookWindow, text="Return Book", command=returnBook, width=15, height=2, font=("Helvetica", 10), relief='raised', bd=5)
    submitButton.pack(pady=20)
    
    returnBookWindow.resizable(False, False)

def returnBookDB(book_ID):
    connection = connectDB()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM borrowedBooks WHERE book_ID = %s", (book_ID,))
        book = cursor.fetchone()
        if not book:
            messagebox.showerror("Error", "Book not found in borrowed_books!")
            return
    
        query_delete_borrowed = "DELETE FROM borrowedBooks WHERE book_ID = %s"
        cursor.execute(query_delete_borrowed, (book_ID,))
        
        connection.commit()
        messagebox.showinfo("Success", "Book returned successfully!")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error returning book: {error}")
    finally:
        cursor.close()
        connection.close()
          
# view all books as admin
def create_viewBooksWindow():
    viewBooksWindow = Toplevel()
    viewBooksWindow.geometry("1280x720")
    viewBooksWindow.title("View Books")
    viewBooksWindow.config(bg="#cbc1bf")
    
    # Adding the label
    viewBooksLabel = Label(viewBooksWindow, text="Books in the Library", font=("Times New Roman", 30), bg="#cbc1bf")
    viewBooksLabel.pack(pady=20)
    
    # Creating the frame to ensure background color is visible
    treeFrame = Frame(viewBooksWindow, bg="#cbc1bf")
    treeFrame.pack(fill=BOTH, expand=True, padx=20, pady=20)
    
    tree = ttk.Treeview(treeFrame, columns=("book_ID", "title", "author", "publisher", "publicationYear", "ddc"), show='headings')
    tree.heading("book_ID", text="ID")
    tree.heading("title", text="Title")
    tree.heading("author", text="Author")
    tree.heading("publisher", text="Publisher")
    tree.heading("publicationYear", text="Publication Year")
    tree.heading("ddc", text="DDC")
    
    tree.column("book_ID", width=50)
    tree.column("title", width=200)
    tree.column("author", width=150)
    tree.column("publisher", width=150)
    tree.column("publicationYear", width=100)
    tree.column("ddc", width=100)
    
    tree.pack(fill=BOTH, expand=True)
    fetchDisplayBooks(tree)
def fetchDisplayBooks(tree):
    connection =connectDB()
    if connection is None:
        return
    try:
        cursor = connection.cursor()
        query = "SELECT book_ID, title, author, publisher, publicationYear, ddc FROM books"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", "end",values =row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error fetching book data: {error}")
    finally:
        cursor.close()
        connection.close()
 
# add book details window
def create_addBooksWindow():
    addBooksWindow = Toplevel()
    addBooksWindow.geometry("1000x500")
    addBooksWindow.title("Add Books")
    addBooksWindow.config(bg="#cbc1bf")
    
    addBooksLabel = Label(addBooksWindow, text="Register Newly Added Books Here", font=("Times New Roman", 30), bg="#cbc1bf", fg="#333333")
    addBooksLabel.pack(pady=20)
    
    # Line divider
    lineDivider = Frame(addBooksWindow, height=2, bd=1, relief='solid', bg="#333333")
    lineDivider.pack(fill='x', padx=20, pady=10)
    
    # Frames for entries
    titleFrame = Frame(addBooksWindow, bg="#cbc1bf")
    titleFrame.pack(pady=10)
    authorFrame = Frame(addBooksWindow, bg="#cbc1bf")
    authorFrame.pack(pady=10)
    publisherFrame = Frame(addBooksWindow, bg="#cbc1bf")
    publisherFrame.pack(pady=10)
    yearFrame = Frame(addBooksWindow, bg="#cbc1bf")
    yearFrame.pack(pady=10)
    ddcFrame = Frame(addBooksWindow, bg="#cbc1bf")
    ddcFrame.pack(pady=10)
    
    # Labels and entries
    titleLabel = Label(titleFrame, text="Book Title:", font=("Helvetica", 15, "bold"), bg="#cbc1bf", fg="#000000")
    titleLabel.pack(side='left', padx=10)
    titleEntry = Entry(titleFrame, width=50, font=("Helvetica", 15))
    titleEntry.pack(side='left')

    authorLabel = Label(authorFrame, text="Author:", font=("Helvetica", 15, "bold"), bg="#cbc1bf", fg="#000000")
    authorLabel.pack(side='left', padx=10)
    authorEntry = Entry(authorFrame, width=50, font=("Helvetica", 15))
    authorEntry.pack(side='left')

    publisherLabel = Label(publisherFrame, text="Publisher:", font=("Helvetica", 15, "bold"), bg="#cbc1bf", fg="#000000")
    publisherLabel.pack(side='left', padx=10)
    publisherEntry = Entry(publisherFrame, width=50, font=("Helvetica", 15))
    publisherEntry.pack(side='left')

    yearLabel = Label(yearFrame, text="Year Published:", font=("Helvetica", 15, "bold"), bg="#cbc1bf", fg="#000000")
    yearLabel.pack(side='left', padx=10)
    yearEntry = Entry(yearFrame, width=50, font=("Helvetica", 15))
    yearEntry.pack(side='left')

    ddcLabel = Label(ddcFrame, text="DDC:", font=("Helvetica", 15, "bold"), bg="#cbc1bf", fg="#000000")
    ddcLabel.pack(side='left', padx=10)
    ddcEntry = Entry(ddcFrame, width=50, font=("Helvetica", 15))
    ddcEntry.pack(side='left')
    
    def submitBook():
        title = titleEntry.get()
        author = authorEntry.get()
        publisher = publisherEntry.get()
        publicationYear = yearEntry.get()
        ddc = ddcEntry.get()
        addBooksDB(title, author, publisher, publicationYear, ddc)
        addBooksWindow.destroy()
    
    # Submit button
    submitButton = Button(addBooksWindow, text="Submit Book", command=submitBook, width=15, height=2, font=("Helvetica", 15, "bold"), relief='raised', bd=5)
    submitButton.pack(pady=20)
    
    addBooksWindow.resizable(False, False)

       
    
    submitButton = Button(addBooksWindow, text="Register book", command=submitBook)
    submitButton.pack(pady=20)
   
# connecting to server
def connectDB():
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="librarydatabase")
        return connection
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error connecting to MySQL: {error}")
        return None

# add book database
def addBooksDB(title, author, publisher, publicationYear, ddc):
    connection = connectDB()
    if connection is None:
        return
    try:
        cursor =connection.cursor()
        query = "INSERT INTO books (title, author, publisher, publicationYear, ddc) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (title, author, publisher, publicationYear,ddc))
        connection.commit()
        messagebox.showinfo("Success!","Book was added successfully!")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error adding book: {error}")
    finally:
        cursor.close()
        connection.close()  
# remove books
def create_removeBooksWindow():
    removeBooksWindow = Toplevel()
    removeBooksWindow.geometry("720x360")
    removeBooksWindow.title("Remove Books")
    removeBooksWindow.config(bg="#cbc1bf")
    
    removeBooksLabel = Label(removeBooksWindow, text="Remove Books from the Library", font=("Times New Roman", 30), bg="#cbc1bf")
    removeBooksLabel.pack(pady=20)
    
    # Line divider
    lineDivider = Frame(removeBooksWindow, height=2, bd=1, relief='solid', bg="black")
    lineDivider.pack(fill='x', padx=20, pady=10)
    
    removeBookFrame = Frame(removeBooksWindow, bg="#cbc1bf")
    removeBookFrame.pack(pady=10)
    
    bookIdLabel = Label(removeBookFrame, text="Book ID:", font=("Helvetica", 15, "bold"), bg="#cbc1bf", fg="#000000")
    bookIdLabel.pack(side='left', padx=10)
    bookIdEntry = Entry(removeBookFrame, width=20, font=("Helvetica", 15))
    bookIdEntry.pack(side='left')
    
    def submitRemoveBook():
        book_id = bookIdEntry.get()
        if book_id:
            removeBookDB(book_id)
            removeBooksWindow.destroy()
    
    submitButton = Button(removeBooksWindow, text="Remove Book", command=submitRemoveBook, width=15, height=2, font=("Helvetica", 10, "bold"), relief='raised', bd=5)
    submitButton.pack(pady=20)
    
    removeBooksWindow.resizable(False, False)

def removeBookDB(book_id):
    connection = connectDB()
    if connection is None:
        return
    
    try:
        cursor = connection.cursor()
        query = "DELETE FROM books WHERE book_ID = %s"
        cursor.execute(query,(book_id,))
        connection.commit()
        messagebox.showinfo("Removal successful!", "Book was removed successfully")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error removing book: {error}")
    finally:
        cursor.close()
        connection.close()
# view borrowers log table
def create_viewBorrowerWindow():
    viewBorrowerWindow = Toplevel()
    viewBorrowerWindow.geometry("1280x720")
    viewBorrowerWindow.title("View Borrowers")
    viewBorrowerWindow.config(bg="#cbc1bf")
    
    # Adding the label
    viewBorrowerLabel = Label(viewBorrowerWindow, text="Borrower's Log", font=("Times New Roman", 30), bg="#cbc1bf")
    viewBorrowerLabel.pack(pady=20)
    
    # Creating the frame to ensure background color is visible
    treeFrame = Frame(viewBorrowerWindow, bg="#cbc1bf")
    treeFrame.pack(fill=BOTH, expand=True, padx=20, pady=20)
    
    tree = ttk.Treeview(treeFrame, columns=("borrowID", "borrowerName", "borrowDate", "returnDate", "book_ID"), show='headings')
    tree.heading("borrowID", text="ID")
    tree.heading("borrowerName", text="Borrower Name")
    tree.heading("borrowDate", text="Borrow Date")
    tree.heading("returnDate", text="Return Date")
    tree.heading("book_ID", text="Book ID")
    
    tree.column("borrowID", width=50)
    tree.column("borrowerName", width=200)
    tree.column("borrowDate", width=100)
    tree.column("returnDate", width=100)
    tree.column("book_ID", width=50)
    
    tree.pack(fill=BOTH, expand=True)
    
    fetchBorrowers(tree)

def fetchBorrowers(tree):
    borrowers = getBorrowers()
    for borrower in borrowers:
        tree.insert('', END, values=borrower)

def getBorrowers():
    connection = connectDB()
    if connection is None:
        return []
    try:
        cursor = connection.cursor()
        query = """
            SELECT borrowID, borrowerName, borrowDate, returnDate, book_ID 
            FROM borrower
        """
        cursor.execute(query)
        borrowers = cursor.fetchall()
        return borrowers
    except mysql.connector.Error as error:
        print(f"Error fetching borrowers: {error}")
        return []
    finally:
        cursor.close()
        connection.close()

def create_viewBorrowedBooksWindow():
    viewBorrowedBooksWindow = Toplevel()
    viewBorrowedBooksWindow.geometry("1280x720")
    viewBorrowedBooksWindow.title("View Borrowed Books")
    viewBorrowedBooksWindow.config(bg="#cbc1bf")
    
    # Adding the label
    viewBorrowedBooksLabel = Label(viewBorrowedBooksWindow, text="Borrowed Books", font=("Times New Roman", 30), bg="#cbc1bf")
    viewBorrowedBooksLabel.pack(pady=20)
    
    # Creating the frame to ensure background color is visible
    treeFrame = Frame(viewBorrowedBooksWindow, bg="#cbc1bf")
    treeFrame.pack(fill=BOTH, expand=True, padx=20, pady=20)
    
    tree = ttk.Treeview(treeFrame, columns=("book_ID","borrowID", "title", "author", "publisher", "publicationYear", "ddc",  "borrowDate", "returnDate"), show='headings')
    tree.heading("book_ID", text="Book ID")
    tree.heading("borrowID", text="Borrow ID")
    tree.heading("title", text="Title")
    tree.heading("author", text="Author")
    tree.heading("publisher", text="Publisher")
    tree.heading("publicationYear", text="Publication Year")
    tree.heading("ddc", text="DDC")
    tree.heading("borrowDate", text="Borrow Date")
    tree.heading("returnDate", text="Return Date")
    
    tree.column("book_ID", width=50)
    tree.column("borrowID", width=100)
    tree.column("title", width=150)
    tree.column("author", width=150)
    tree.column("publisher", width=150)
    tree.column("publicationYear", width=100)
    tree.column("ddc", width=100)
    tree.column("borrowDate", width=100)
    tree.column("returnDate", width=100)
    
    tree.pack(fill=BOTH, expand=True)
    
    fetchBorrowedBooks(tree)

def fetchBorrowedBooks(tree):
    borrowed_books = getBorrowedBooks()
    for book in borrowed_books:
        tree.insert('', END, values=book)

def getBorrowedBooks():
    connection = connectDB()
    if connection is None:
        return []
    try:
        cursor = connection.cursor()
        query = """
            SELECT book_ID, borrowID, title, author, publisher, publicationYear, ddc,borrowDate, returnDate 
            FROM borrowedBooks
        """
        cursor.execute(query)
        borrowed_books = cursor.fetchall()
        return borrowed_books
    except mysql.connector.Error as error:
        print(f"Error fetching borrowed books: {error}")
        return []
    finally:
        cursor.close()
        connection.close()
# Function to handle password input

def getPassword(passwordWindow):
    global passwordEntry
    try:
        password = passwordEntry.get()
        if password == "123":
            passwordWindow.destroy()
            create_adminWindow()
        else:
            raise ValueError("Invalid password")
    except ValueError as ve:
        messagebox.showerror("Error!!!", str(ve) + "\nRefer to the Librarian for the admin password, Thank You!")
    finally:
        passwordWindow.destroy()

# Function to prompt for admin password
def adminPassword():
    global passwordEntry
    passwordWindow = Toplevel()
    passwordWindow.geometry("300x150")
    passwordWindow.title("Enter Admin Password")
    
    passwordLabel = Label(passwordWindow, text="Enter admin password:")
    passwordLabel.pack(pady=10)
    passwordEntry = Entry(passwordWindow, width=40, show="X")
    passwordEntry.pack(pady=10)
    
    submitButton = Button(passwordWindow, text="Submit", command=lambda: getPassword(passwordWindow))
    submitButton.pack(pady=10)

# Function to ask for confirmation to proceed as admin
def ask_yes_no():
    answer = messagebox.askquestion('?', 'Do you want to proceed as an admin?')
    if answer == 'yes':
        adminPassword()

# Main window
window = Tk()
# Window initialization settings
window.geometry("1280x720")
window.title("Library Manager")
window.config(background="#cbc1bf")
icon = PhotoImage(file='Logo.png')
window.iconphoto(True, icon)
window.resizable(False, False)

# Main label
mainLabel = Label(window, text="Welcome to BooKeep:\nThe Library Manager",font=('Times New Roman', 30),bg="#cbc1bf")
mainLabel.pack(anchor='w', padx=30, pady=(110, 10))

# Line divider
window_width = 1920
lineDivider_width = window_width // 5.3
lineDivider = Frame(window, height=2, bd=1, bg="black", width=lineDivider_width)
lineDivider.pack(anchor='w', padx=25)

# Image insert
logoImage = Image.open("C:\\Users\\Jiro\\Documents\\Carag, JiroNinoAngelo 2102\\logBigger.png")
resizeLogo = logoImage.resize((840, 840), Image.LANCZOS)
logoNew = ImageTk.PhotoImage(resizeLogo)

image_label = Label(window, image=logoNew)
image_label.place(relx=1.0, rely=0.5, anchor='e')

# Choice between admin or user
adminButton = Button(window, text='Admin', command=ask_yes_no)
adminButton.config(font=('Helvetica', 20))
adminButton.pack(anchor='w', padx=160, pady=(50, 10))

userButton = Button(window, text='User', command=create_userWindow)
userButton.config(font=('Helvetica', 20))
userButton.pack(anchor='w', padx=170, pady=30)

window.mainloop()
