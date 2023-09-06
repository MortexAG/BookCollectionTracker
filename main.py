import tkinter as tk
from tkinter import Entry, Label, Button, Listbox, Toplevel, Frame, messagebox
import json
#import string
import os
import add_books

root = tk.Tk()
root.title("Library Manager")
root.geometry("960x540")

json_file = "./books.json"


# Check if the JSON file exists
if not os.path.exists(json_file):
    # If it doesn't exist, create it with the default structure
    default_data = {
        "Books": []
    }
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(default_data, file, indent=4, ensure_ascii=False)

def load_books():
    books_list = []
    books_details = []
    with open(json_file, 'r', encoding="utf-8") as file:
        books = json.load(file)
        for book in books["Books"]:
            books_list.append(book["Title"])
            books_details.append(book)
    return books_list, books_details, books["Books"]

books, books_details, all_books = load_books()

def all_books_show_details():
    # create window
    def create_details_window(book_name):
        # Create The Details Window
        details_window = Toplevel(root)
        details_window.geometry("320x480")
        details_window.title(f"{book_name} Details")

        # Details Frame
        details_frame = Frame(details_window)
        details_frame.grid(row=0, column=0, padx=10, pady=5)

        # Title Label And Content
        book_title_label = Label(details_frame, text="Title")
        book_title_label.grid(row=1, column=0, padx=5, pady=5)

        book_title_content = Listbox(details_frame, height=1, width=40)
        book_title_content.grid(row=2, column=0, padx=5, pady=5)

        # Author Label And Content
        book_author_label = Label(details_frame, text="Author")
        book_author_label.grid(row=3, column=0, padx=5, pady=5)

        book_author_content = Listbox(details_frame, height=1, width=40)
        book_author_content.grid(row=4, column=0, padx=5, pady=5)

        # Type Label And Content
        book_type_label = Label(details_frame, text="Type")
        book_type_label.grid(row=5, column=0, padx=10, pady=5)

        book_type_content = Listbox(details_frame, height=1, width=40)
        book_type_content.grid(row=6, column=0, padx=10, pady=5)

        # Publication Time Label And Content
        book_pubtime_label = Label(details_frame, text="Publication Time")
        book_pubtime_label.grid(row=7, column=0, padx=5, pady=5)

        book_pubdate_content = Listbox(details_frame, height=1, width=40)
        book_pubdate_content.grid(row=8, column=0, padx=5, pady=5)

        return book_title_content, book_author_content, book_type_content, book_pubdate_content


    def get_specific_book():
        #print(cleanitem)
        for book in books_details:
            if cleanitem.lower() in book["Title"].lower():
                book_title = book["Title"]
                book_author = book["Author"]
                book_type = book["Type"]
                book_publication_date = book["PublicationDate"]
        return book_title, book_author, book_type, book_publication_date
    
    # fill the window with the required details
    def fill_the_window():
        if len(cleanitem) >= 1:
            title_label, author_label, type_label, pubdate_label = create_details_window(cleanitem)
            title, author, the_type, publication_date = get_specific_book()
            title_label.insert(tk.END,title)
            author_label.insert(tk.END,author)
            type_label.insert(tk.END,the_type)
            pubdate_label.insert(tk.END,publication_date)

    # Step: Get The Selected Item From ListBoxx
    for i in books_listbox.curselection():
        item = str(books_listbox.get(i))
        #cleanitem = item.translate(str.maketrans('', '', string.punctuation))
        cleanitem = item
    if len(books_listbox.curselection()) >= 1:
        fill_the_window()
    else:
        messagebox.showinfo(title="No Item Selected", message="Please Select An Item From The List")


# Create a frame to hold the books list (Listbox)
books_frame = Frame(root)
books_frame.pack(side=tk.LEFT, padx=20, pady=13)

# Label for "Books" above the Listbox
books_label = Label(books_frame, text="All Books")
books_label.pack(padx=5, pady=5)

# Add Books Button
add_books_button = Button(books_frame,text="Add Books",command=add_books.main_app, activebackground="grey", activeforeground="grey", pady=5, padx=5)
add_books_button.pack(padx=5, pady=5)

# All Books Details Button
all_books_details_button = Button(books_frame,text="Details",command=all_books_show_details, activebackground="grey", activeforeground="grey", pady=5, padx=5)
all_books_details_button.pack(padx=5, pady=5)

# Listbox for textbooks (books_listbox)
books_listbox = Listbox(books_frame, height=40, width=35, bg="white", activestyle='dotbox', font="Helvetica", fg="Black")
books_listbox.pack(fill=tk.BOTH, expand=True)

for book in books:
    books_listbox.insert(tk.END, book)

# Create a frame to hold the search components
search_frame = Frame(root)
search_frame.pack(side=tk.RIGHT, padx=20, pady=11)

# Search Area
search_title = Label(search_frame, text="Search")
search_title.grid(row=0, column=0, padx=5, pady=5)

search_box = Entry(search_frame, width="40")
search_box.grid(row=1, column=0, padx=5, pady=5)

# Label for "Search Results" below the search box
search_results_label = Label(search_frame, text="Search Results")
search_results_label.grid(row=2, column=0, padx=5, pady=5)

# Listbox for search results
search_results_listbox = Listbox(search_frame, height=30, width=35, bg="white", activestyle='dotbox', font="Helvetica", fg="Black")
search_results_listbox.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

# Search Button
def search():
        # Step 1: Read The Json File
        data = all_books
        # def read_json_file(filename):
        #     with open(filename, 'r', encoding="utf-8") as file:
        #         data = json.load(file)
        #     return data['Books']
        
        #  Step 2: Get The User Input
        search_title = search_box.get()
        # Step 3: Search The Json File
        def search_json(data, query):
            results = []
            for book in data:
                if query.lower() in book['Title'].lower() or query.lower() in book['Author'].lower() or query.lower() in book['Type'].lower() or query.lower() in book['PublicationDate'].lower():
                    results.append(book)
            return results
        # Step 4: Return results
        if len(search_title) >= 1:
            #data = read_json_file(json_file)  # Replace 'your_library.json' with your JSON file's name
            found_books = search_json(data, search_title)
        else:
            # clean listbox
            search_results_listbox.delete(0, tk.END)
            search_results_listbox.insert(tk.END, "Search Field Empty")

        # Step 5: Return In App
        if found_books:
                # clean the listbox
            search_results_listbox.delete(0, tk.END)
                # add to listbox
            #print("Found matching books:")
            for book in found_books:
                #print(f"Title: {book['Title']}, Author: {book['Author']}, Type: {book['Type']}, Publication Date: {book['PublicationDate']}")
                search_results_listbox.insert(tk.END, book["Title"])
        else:
            # clean listbox
            search_results_listbox.delete(0, tk.END)
            # add to listbox
            search_results_listbox.insert(tk.END, "No Books Found")  

def show_details():
    # create window
    def create_details_window(book_name):
        # Create The Details Window
        details_window = Toplevel(root)
        details_window.geometry("320x480")
        details_window.title(f"{book_name} Details")

        # Details Frame
        details_frame = Frame(details_window)
        details_frame.grid(row=0, column=0, padx=10, pady=5)

        # Title Label And Content
        book_title_label = Label(details_frame, text="Title")
        book_title_label.grid(row=1, column=0, padx=5, pady=5)

        book_title_content = Listbox(details_frame, height=1, width=40)
        book_title_content.grid(row=2, column=0, padx=5, pady=5)

        # Author Label And Content
        book_author_label = Label(details_frame, text="Author")
        book_author_label.grid(row=3, column=0, padx=5, pady=5)

        book_author_content = Listbox(details_frame, height=1, width=40)
        book_author_content.grid(row=4, column=0, padx=5, pady=5)

        # Type Label And Content
        book_type_label = Label(details_frame, text="Type")
        book_type_label.grid(row=5, column=0, padx=10, pady=5)

        book_type_content = Listbox(details_frame, height=1, width=40)
        book_type_content.grid(row=6, column=0, padx=10, pady=5)

        # Publication Time Label And Content
        book_pubtime_label = Label(details_frame, text="Publication Time")
        book_pubtime_label.grid(row=7, column=0, padx=5, pady=5)

        book_pubdate_content = Listbox(details_frame, height=1, width=40)
        book_pubdate_content.grid(row=8, column=0, padx=5, pady=5)

        return book_title_content, book_author_content, book_type_content, book_pubdate_content


    def get_specific_book():
        for book in books_details:
            if cleanitem.lower() in book["Title"].lower():
                book_title = book["Title"]
                book_author = book["Author"]
                book_type = book["Type"]
                book_publication_date = book["PublicationDate"]
        return book_title, book_author, book_type, book_publication_date
    
    # fill the window with the required details
    def fill_the_window():
        if len(cleanitem) >= 1:
            title_label, author_label, type_label, pubdate_label = create_details_window(cleanitem)
            title, author, the_type, publication_date = get_specific_book()
            title_label.insert(tk.END,title)
            author_label.insert(tk.END,author)
            type_label.insert(tk.END,the_type)
            pubdate_label.insert(tk.END,publication_date)

    # Step: Get The Selected Item From ListBoxx
    for i in search_results_listbox.curselection():
        item = str(search_results_listbox.get(i))
        #cleanitem = item.translate(str.maketrans('', '', string.punctuation))
        cleanitem = item
    if len(search_results_listbox.curselection()) >= 1:
        fill_the_window()
    else:
        messagebox.showinfo(title="No Item Selected", message="Please Select An Item From The List")
    

# Search Button
search_button = Button(search_frame, text="Search", command=search, activebackground="grey", activeforeground="grey", pady=5, padx=5)
search_button.grid(row=1, column=1, padx=5, pady=5)
# Details Button
details_button = Button(search_frame,text="Details", command=show_details, activebackground="grey", activeforeground="grey", pady=5, padx=5)
details_button.grid(row=1,column=2, padx=5, pady=5)

root.mainloop()
