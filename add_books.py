import tkinter as tk
from tkinter import messagebox, Frame, Label, Button, Entry, Toplevel
import json

def main_app():
    root = tk.Tk()
    root.geometry("320x480")
    root.title("Add Books")

    # Load the JSON file
    json_file = "example.json"
    def load_json():
        with open(json_file, 'r', encoding="utf-8") as file:
            old_data = json.load(file)
        return old_data

    old_data = load_json()

    # The Addition Functions

    def save_json(data):
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_one():
        def create_window():

            # Create Window
            add_one_window = Toplevel(root)
            add_one_window.geometry("320x480")
            add_one_window.title("Add One Book")

            # Details Frame
            details_frame = Frame(add_one_window)
            details_frame.grid(row=0, column=0, padx=90, pady=5)

            # Title Label And Content
            book_title_label = Label(details_frame, text="Title")
            book_title_label.grid(row=1, column=0, padx=5, pady=5)
            book_title_content = Entry(details_frame)
            book_title_content.grid(row=2, column=0, padx=5, pady=5)

            # Author Label And Content
            book_author_label = Label(details_frame, text="Author")
            book_author_label.grid(row=3, column=0, padx=5, pady=5)
            book_author_content = Entry(details_frame)
            book_author_content.grid(row=4, column=0, padx=5, pady=5)

            # Type Label And Content
            book_type_label = Label(details_frame, text="Type")
            book_type_label.grid(row=5, column=0, padx=10, pady=5)
            book_type_content = Entry(details_frame)
            book_type_content.grid(row=6, column=0, padx=10, pady=5)

            # Publication Time Label And Content
            book_pubtime_label = Label(details_frame, text="Publication Time")
            book_pubtime_label.grid(row=7, column=0, padx=5, pady=5)
            book_pubdate_content = Entry(details_frame)
            book_pubdate_content.grid(row=8, column=0, padx=5, pady=5)

            # Confirm function
            def confirm_add_one():
                title = book_title_content.get()
                author = book_author_content.get()
                book_type = book_type_content.get()
                pub_date = book_pubdate_content.get()

                if title and author and book_type and pub_date:
                    new_book = {
                        "Title": title,
                        "Author": author,
                        "Type": book_type,
                        "PublicationDate": pub_date
                    }
                    old_data["Books"].append(new_book)
                    save_json(old_data)
                    add_one_window.destroy()
                else:
                    messagebox.showinfo("Error", "Please fill in all fields.")

            # Confirm Button
            confirm_button = Button(details_frame, text="Confirm", command=confirm_add_one, activebackground="grey", activeforeground="grey", pady=5, padx=5)
            confirm_button.grid(row=9, column=0, padx=5, pady=5)

        create_window()

    def add_multiple():
        def create_window():

            # Create Window
            add_multiple_window = Toplevel(root)
            add_multiple_window.geometry("320x480")
            add_multiple_window.title("Add Multiple Books")

            # Details Frame
            details_frame = Frame(add_multiple_window)
            details_frame.grid(row=0, column=0, padx=90, pady=5)

            # Title Label And Content
            book_title_label = Label(details_frame, text="Title")
            book_title_label.grid(row=1, column=0, padx=5, pady=5)
            book_title_content = Entry(details_frame)
            book_title_content.grid(row=2, column=0, padx=5, pady=5)

            # Author Label And Content
            book_author_label = Label(details_frame, text="Author")
            book_author_label.grid(row=3, column=0, padx=5, pady=5)
            book_author_content = Entry(details_frame)
            book_author_content.grid(row=4, column=0, padx=5, pady=5)

            # Type Label And Content
            book_type_label = Label(details_frame, text="Type")
            book_type_label.grid(row=5, column=0, padx=10, pady=5)
            book_type_content = Entry(details_frame)
            book_type_content.grid(row=6, column=0, padx=10, pady=5)

            # Publication Time Label And Content
            book_pubtime_label = Label(details_frame, text="Publication Time")
            book_pubtime_label.grid(row=7, column=0, padx=5, pady=5)
            book_pubdate_content = Entry(details_frame)
            book_pubdate_content.grid(row=8, column=0, padx=5, pady=5)

            # Confirm function
            def confirm_add_multiple():
                title = book_title_content.get()
                author = book_author_content.get()
                book_type = book_type_content.get()
                pub_date = book_pubdate_content.get()

                if title and author and book_type and pub_date:
                    new_book = {
                        "Title": title,
                        "Author": author,
                        "Type": book_type,
                        "PublicationDate": pub_date
                    }
                    old_data["Books"].append(new_book)
                    save_json(old_data)
                    book_title_content.delete(0, tk.END)
                    book_author_content.delete(0, tk.END)
                    book_type_content.delete(0, tk.END)
                    book_pubdate_content.delete(0, tk.END)
                else:
                    messagebox.showinfo("Error", "Please fill in all fields.")

            # Confirm Button
            confirm_button = Button(details_frame, text="Confirm", command=confirm_add_multiple, activebackground="grey", activeforeground="grey", pady=5, padx=5)
            confirm_button.grid(row=9, column=0, padx=5, pady=5)

        create_window()

    # Make a frame to hold the buttons
    buttons_frame = Frame(root)
    buttons_frame.grid(row=0, column=4, padx=100, pady=100)

    # The buttons
    add_one_button = Button(buttons_frame, text="Add One Book", command=add_one, activebackground="grey", activeforeground="grey", pady=5, padx=5)
    add_one_button.grid(row=3, column=4, padx=5, pady=5)

    add_multiple_button = Button(buttons_frame, text="Add Multiple Books", command=add_multiple, activebackground="grey", activeforeground="grey", pady=5, padx=5)
    add_multiple_button.grid(row=4, column=4, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_app()
