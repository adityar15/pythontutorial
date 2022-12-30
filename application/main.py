from classes import Reader, Author, Book
from email_validator import validate_email, EmailNotValidError

def main():
    choice = 0
    # big while loop
    while choice != -1:

        print("Please select an option")
        choice = input("\n1. Manage Reader \n2. Manage Author \n0. Press for exit \n")
        validChoices = ["0", "1", "2"]
        if choice not in validChoices:
            print("\nPlease input a correct choice")
            continue
        
        elif choice == "0":
            choice =-1
        
        elif choice == "1":
            reader()
        
        elif choice == "2":
            author()


def reader():
    print("Please select an option")
    readerChoice = input("\n1. Add Reader \n2. Add book to collection \n0. To go back \n")
    validReaderChoices = ["0", "1", "2"]
    # reader while loop
    while readerChoice != -1:
        if readerChoice not in validReaderChoices:
            print("\nPlease input a correct choice")
            continue
        elif readerChoice == "0":
            readerChoice = -1

        elif readerChoice == "1":
            name = input("\n Please enter the name of the reader: ")
            email = input("\n Please enter the email of the reader: ")
            if name == "" or email == "":
                print("\nEnter correct details.")
                continue

            if emailValidator(email) == False:
                continue
            
            reader = Reader.Reader(name=name, email=email)
            reader.createReader()
            print("\nReader added successfully")
            
           
        elif readerChoice == "2":
            # code for display books code for adding the book
            pass

def author():
    print("Please select an option")
    authorChoice = input("\n1. Add Author \n2. Add book to database \n3. Update book \n0. To go back \n")
    validAuthorChoice = ["0", "1", "2", "3"]

    while authorChoice != -1:

        if authorChoice not in validAuthorChoice:
            print("\nPlease input a correct choice")
            continue
        elif authorChoice == "0":
            authorChoice = -1

        elif authorChoice == "1":
        #    your exercise code of creating an author
            pass
        elif authorChoice == "2":
            book = Book.Book()
            books = book.getAllBooks()
            print("\n Name \t\t Price \t\t")
            for book in books:
                title = book["title"]
                price = book["price"]
                print(f"\n {title} \t\t {price}")
            
            print("\n Add a book if it is not shown here ")

            insideChoice = input("\nAny key to Conitnue \n2. Go back")

            if insideChoice == "2":
                break

            title = input("\n Please enter the title of the book: ")
            price = input("\n Please enter the price of the book: ")
            email = input("\n Please enter the email of the author: ")

            if title == "" or price == "" or email == "":
                print("\nEnter correct details.")
                continue
            
            if emailValidator(email) == False:
                continue

            author = Author.Author()
            authorDetailsList = author.getAuthor(email=email)
            authorDetails = authorDetailsList[0] if authorDetailsList else None 

            if not authorDetails:
                print("\n Author does not exist")
                continue

            book = Book.Book(title=title, price=price)
            book.addBook(authorDetails["id"])
            print("\n Book added successfully")
            continue

def emailValidator(email):
        try:
            valid = validate_email(email) 
            return valid.email
           
        except EmailNotValidError as e:
            print(str(e))
            return False

if __name__ == "__main__":
    main()