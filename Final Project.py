def main():
    library_books = {}  
    returned_books = []  
    delivery_books = []
    while True:
        print("\nLibrary Book Management System")
        print("1. Add a Book")
        print("2. View Total Expense")
        print("3. View Total Books and Names")
        print("4. Delete a Book")
        print("5. Add Returned Book")
        print("6. Add Delivery Book")
        print("7. View Returned Books")
        print("8. View Delivery Books")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_book(library_books)
        elif choice == '2':
            view_total_expense(library_books)
        elif choice == '3':
            view_total_books_and_names(library_books)
        elif choice == '4':
            delete_book(library_books)
        elif choice == '5':
            add_returned_book(returned_books)
        elif choice == '6':
            add_delivery_book(delivery_books)
        elif choice == '7':
            view_books(returned_books, "Returned Books")
        elif choice == '8':
            view_books(delivery_books, "Delivery Books")
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_book(library_books):
    book_name = input("Enter the name of the book: ")
    try:
        expense = float(input("Enter the expense of the book: "))
        library_books[book_name] = expense
        print(f"Book '{book_name}' added successfully with an expense of {expense}.")
    except ValueError:
        print("Invalid input for expense. Please enter a valid number.")

def view_total_expense(library_books):
    total_expense = sum(library_books.values())
    print(f"\nTotal expense of all books: {total_expense}")

def view_total_books_and_names(library_books):
    total_books = len(library_books)
    print(f"\nTotal number of books: {total_books}")
    if total_books > 0:
        print("Book Names:")
        for book_name in library_books.keys():
            print(f"- {book_name}")
    else:
        print("No books available in the library.")

def delete_book(library_books):
    book_name = input("Enter the name of the book to delete: ")
    if book_name in library_books:
        del library_books[book_name]
        print(f"Book '{book_name}' deleted successfully.")
    else:
        print(f"Book '{book_name}' not found in the library.")

def add_returned_book(returned_books):
    book_name = input("Enter the name of the returned book: ")
    returned_books.append(book_name)
    print(f"Book '{book_name}' added to the returned books list.")

def add_delivery_book(delivery_books):
    book_name = input("Enter the name of the delivery book: ")
    delivery_books.append(book_name)
    print(f"Book '{book_name}' added to the delivery books list.")

def view_books(book_list, category_name):
    print(f"\n{category_name}:")
    if book_list:
        for book_name in book_list:
            print(f"- {book_name}")
    else:
        print(f"No books in the {category_name.lower()} list.")

if __name__ == "__main__":
    main()
