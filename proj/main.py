import tkinter as tk
import tkinter.font as tkf
import mysql.connector as sqc
from tkinter import ttk

class Books:
  def __init__(self):
    # Create the main window
    self.window = tk.Tk()
    self.window.title("Books Manager")
    self.window.geometry("400x200")
    
    # Create a Title
    self.title_label = tk.Label(self.window, text="Books Management System", font=tkf.Font(family="Times", size="20"))

    # Create the buttons
    self.add_button = tk.Button(self.window, text="Add Book", command=self.add_book)
    self.delete_button = tk.Button(self.window, text="Delete Book", command=self.delete_book)
    self.view_button = tk.Button(self.window, text="View Books", command=self.view_books)
    
    # Pack
    self.title_label.pack()
    self.add_button.pack()
    self.delete_button.pack()
    self.view_button.pack()
    
  def add_book(self):
    # Create a new window for adding a book
    add_window = tk.Tk()
    add_window.title("Add Book")
    add_window.geometry("400x200")

    # Create labels and entry fields for the book's title, author, and year
    title_label = tk.Label(add_window, text="Title:")
    self.title_entry = tk.Entry(add_window)
    author_label = tk.Label(add_window, text="Author:")
    self.author_entry = tk.Entry(add_window)
    year_label = tk.Label(add_window, text="Year:")
    self.year_entry = tk.Entry(add_window)

    # Create a submit button
    submit_button = tk.Button(add_window, text="Submit", command=self.submit_add)

    # Pack
    title_label.pack()
    self.title_entry.pack()
    author_label.pack()
    self.author_entry.pack()
    year_label.pack()
    self.year_entry.pack()
    submit_button.pack()

    # Run the window loop
    add_window.mainloop()

  def submit_add(self):
    # Get the values from the entry fields
    title = self.title_entry.get()
    author = self.author_entry.get()
    year = self.year_entry.get()

    # Connect to the database
    conn = sqc.connect(
      host="localhost",
      user="root",
      password="toor",
      database="library"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute an INSERT query
    cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))

    # Commit the changes
    conn.commit()
  #add_book function ENDS HERE
    
  def delete_book(self):
    # Create a new window for deleting a book
    delete_window = tk.Tk()
    delete_window.title("Delete Book")
    delete_window.geometry("400x200")
  
    # Create a label and entry field for the book's ID
    id_label = tk.Label(delete_window, text="ID:")
    self.id_entry = tk.Entry(delete_window)

    # Create a submit button
    self.submit_button = tk.Button(delete_window, text="Submit", command=self.submit_delete)

    # Pack 
    id_label.pack()
    self.id_entry.pack()
    self.submit_button.pack()

    # Run the window loop
    delete_window.mainloop()

  def submit_delete(self):
    # Get the value from the entry field
    book_id = self.id_entry.get()

    # Connect to the database
    conn = sqc.connect(
      host="localhost",
      user="root",
      password="toor",
      database="library"
    )
    # Create a cursor
    cursor = conn.cursor()

    # Execute a DELETE query
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))

    # Commit the changes
    conn.commit()
  #delete_book function ENDS HERE
    
  def view_books(self):
    # Connect to the database
    conn = sqc.connect(
      host="localhost",
      user="root",
      password="toor",
      db = "library"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Execute a SELECT query
    cursor.execute("SELECT * FROM books")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Create a new window for displaying the books
    book_window = tk.Tk()
    book_window.title("Books")
    book_window.geometry("400x200")

    # Create a listbox for displaying the books
    listbox = tk.Listbox(book_window)
    #Create a horizontal scrollbar
    scrollbar = ttk.Scrollbar(book_window, orient= "vertical")
    scrollbar.pack(side= tk.RIGHT, fill= tk.BOTH)

    listbox.config(font=tkf.Font(size="14"), yscrollcommand= scrollbar.set)
    listbox.pack(fill=tk.BOTH, expand=True)

    #Configure the scrollbar
    scrollbar.config(command = listbox.yview)

    # Add the books to the listbox
    listbox.insert(tk.END, f"ID. <Book name> by <Author> (<Year>)")
    for row in rows:
      listbox.insert(tk.END, f"{row[0]}. {row[1]} by {row[2]} ({row[3]})")

    # Run the window loop
    book_window.mainloop()
  #view_books function ENDS HERE
  
  def run(self):
    # Connect to the database
    conn = sqc.connect(
      host="localhost",
      user="root",
      password="toor",
      db = "library"
    )

    # Check connection
    if conn.is_connected():
      status = "Connection: Successful"
    else:
      status = "Connection: Failed"

    # Set footer
    self.footer = tk.Frame(self.window)
    self.label = tk.Label(self.footer, text=status)
    self.footer.pack(side="bottom", fill="x")
    self.label.pack(side="right")
    
    # Main Loop
    self.window.mainloop()
    
if __name__ == "__main__":
  app = Books()
  app.run()
