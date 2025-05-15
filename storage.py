import csv
import os
from models import Book, Member, Loan

def load_books(data_dir):
    books = []
    with open(os.path.join(data_dir, 'books.csv'), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['CopiesTotal'] = int(row['CopiesTotal'])
            row['CopiesAvailable'] = int(row['CopiesAvailable'])
            books.append(Book(**row))
    return books

def save_books(data_dir, books):
    with open(os.path.join(data_dir, 'books.csv'), 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Book.__annotations__.keys())
        writer.writeheader()
        for book in books:
            writer.writerow(book.__dict__)

def load_members(data_dir):
    members = []
    with open(os.path.join(data_dir, 'members.csv'), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            members.append(Member(**row))
    return members

def save_members(data_dir, members):
    with open(os.path.join(data_dir, 'members.csv'), 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Member.__annotations__.keys())
        writer.writeheader()
        for member in members:
            writer.writerow(member.__dict__)

def load_loans(data_dir):
    loans = []
    with open(os.path.join(data_dir, 'loans.csv'), newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            loans.append(Loan(**row))
    return loans

def save_loans(data_dir, loans):
    with open(os.path.join(data_dir, 'loans.csv'), 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Loan.__annotations__.keys())
        writer.writeheader()
        for loan in loans:
            writer.writerow(loan.__dict__)

