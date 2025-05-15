from storage import load_books, save_books, load_loans, save_loans, load_members
from models import Loan
from datetime import datetime, timedelta
import uuid
from models import Book


def librarian_menu(data_dir, user):
    while True:
        print("\n=== Librarian Dashboard ===")
        print("1. Add Book\n2. Register Member\n3. Issue Book\n4. Return Book\n5. Overdue List\n6. Logout")
        choice = input("> ")
        if choice == '1':
            add_book(data_dir)
        elif choice == '2':
            from auth import register_member
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            register_member(data_dir, name, email, password)
        elif choice == '3':
            issue_book(data_dir)
        elif choice == '4':
            return_book(data_dir)
        elif choice == '5':
            view_overdue(data_dir)
        elif choice == '6':
            break


def add_book(data_dir):
    isbn = input("ISBN: ")
    title = input("Title: ")
    author = input("Author: ")
    total = int(input("Total Copies: "))
    books = load_books(data_dir)
    for book in books:
        if book.ISBN == isbn:
            print("Book already exists.")
            return
    books.append(Book(isbn, title, author, total, total))
    save_books(data_dir, books)
    print("✔ Book added")

def issue_book(data_dir):
    isbn = input("ISBN to issue: ")
    member_id = input("Member ID: ")
    books = load_books(data_dir)
    book = next((b for b in books if b.ISBN == isbn), None)
    if not book or book.CopiesAvailable < 1:
        print("❌ Book not available")
        return
    loans = load_loans(data_dir)
    loan_id = str(uuid.uuid4().int)[:4]
    today = datetime.today().date()
    due_date = today + timedelta(days=14)
    new_loan = Loan(loan_id, member_id, isbn, str(today), str(due_date), '')
    loans.append(new_loan)
    book.CopiesAvailable -= 1
    save_books(data_dir, books)
    save_loans(data_dir, loans)
    print(f"✔ Book issued. Due on {due_date.strftime('%d-%b-%Y')}")

def return_book(data_dir):
    loan_id = input("Loan ID: ")
    loans = load_loans(data_dir)
    for loan in loans:
        if loan.LoanID == loan_id and loan.ReturnDate == '':
            loan.ReturnDate = str(datetime.today().date())
            books = load_books(data_dir)
            for book in books:
                if book.ISBN == loan.ISBN:
                    book.CopiesAvailable += 1
                    break
            save_books(data_dir, books)
            save_loans(data_dir, loans)
            print("✔ Book returned")
            return
    print("❌ Invalid Loan ID or already returned")

def view_overdue(data_dir):
    loans = load_loans(data_dir)
    today = datetime.today().date()
    print("\nOverdue Loans:")
    for loan in loans:
        if not loan.ReturnDate and datetime.strptime(loan.DueDate, '%Y-%m-%d').date() < today:
            print(f"LoanID: {loan.LoanID}, MemberID: {loan.MemberID}, ISBN: {loan.ISBN}, DueDate: {loan.DueDate}")