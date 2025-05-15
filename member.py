from storage import load_books, load_loans
from datetime import datetime

def member_menu(data_dir, user):
    while True:
        print("\n=== Member Dashboard ===")
        print("1. Search Catalogue\n2. My Loans\n3. Logout")
        choice = input("> ")
        if choice == '1':
            keyword = input("Enter title or author keyword: ").lower()
            books = load_books(data_dir)
            results = [b for b in books if keyword in b.Title.lower() or keyword in b.Author.lower()]
            for b in results:
                print(f"{b.Title} by {b.Author} - {b.CopiesAvailable}/{b.CopiesTotal} available")
        elif choice == '2':
            loans = load_loans(data_dir)
            for l in loans:
                if l.MemberID == user.MemberID:
                    status = "Returned" if l.ReturnDate else "Due: " + l.DueDate
                    print(f"LoanID: {l.LoanID}, ISBN: {l.ISBN}, IssueDate: {l.IssueDate}, {status}")
        elif choice == '3':
            break