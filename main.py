import datetime

class Library:
    def __init__(self):
        # Dictionary to store borrowed book information
        self.borrowed_books = {}
        
    def borrow_book(self, barcode, patron_name):
        """Borrow a book and record the borrower's details and due date."""
        if barcode in self.borrowed_books:
            print(f"Book with barcode {barcode} is already borrowed.")
        else:
            due_date = datetime.datetime.now() + datetime.timedelta(days=14)  # 2-week loan period
            self.borrowed_books[barcode] = {
                'patron': patron_name,
                'borrow_date': datetime.datetime.now(),
                'due_date': due_date
            }
            print(f"Book with barcode {barcode} borrowed by {patron_name}. Due date: {due_date}")

    def return_book(self, barcode):
        """Return a borrowed book and remove it from the borrowed books record."""
        if barcode in self.borrowed_books:
            del self.borrowed_books[barcode]
            print(f"Book with barcode {barcode} has been returned.")
        else:
            print(f"No record found for book with barcode {barcode}.")
    
    def check_due_date(self, barcode):
        """Check the due date of a borrowed book."""
        if barcode in self.borrowed_books:
            due_date = self.borrowed_books[barcode]['due_date']
            print(f"Book with barcode {barcode} is due on {due_date}")
        else:
            print(f"No record found for book with barcode {barcode}.")

    def list_borrowed_books(self):
        """List all borrowed books with details."""
        if not self.borrowed_books:
            print("No books are currently borrowed.")
        else:
            for barcode, details in self.borrowed_books.items():
                patron = details['patron']
                borrow_date = details['borrow_date']
                due_date = details['due_date']
                print(f"Barcode: {barcode}, Patron: {patron}, Borrowed on: {borrow_date}, Due date: {due_date}")

# Example usage:
library = Library()
library.borrow_book("123456789", "Alice")
library.borrow_book("987654321", "Bob")
library.check_due_date("123456789")
library.list_borrowed_books()
library.return_book("123456789")
library.list_borrowed_books()
