from Library import Library
from Book import Book

# The main function is used to create a Library object and display the library menu.
def main():
    # Create a Library object
    lib = Library()


# The main function is used to display the library menu.
    while True:
        print("\nLibrary Menu")
        print("1. Add book")
        print("2. Remove book")
        print("3. Find book")
        print("4. Display books")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")
        try:
            choice = input("Enter choice: ")
        except EOFError:  
                print("\nEOFError: No input received. Continuing...")
                continue


    # Use a match statement to match the choice
        match choice:
            case "1":
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                year = input("Enter year: ")
                lib.add_book(Book(title, author, isbn, year))
            case "2":
                isbn = input("Enter ISBN: ")
                print(lib.remove_book(isbn))
            case "3":
                isbn = input("Enter ISBN: ")
                print(lib.find_book(isbn))
            case "4":
                print(lib.display_books())
            case "5":
                filename = input("Enter filename: ")
                print(lib.save_to_file(filename))
            case "6":
                filename = input("Enter filename: ")
                print(lib.load_from_file(filename))
            case "7":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
