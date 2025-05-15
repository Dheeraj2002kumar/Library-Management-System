import os
import csv
from models import Book, Member, Loan

def ensure_file_exists(file_path, headers):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)


def load_books(data_dir):
    file_path = os.path.join(data_dir, 'books.csv')
    ensure_file_exists(file_path, ['ISBN', 'Title', 'Author', 'TotalCopies', 'AvailableCopies'])
    books = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(row)
    return books


def save_books(data_dir, books):
    with open(os.path.join(data_dir, 'books.csv'), 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Book.__annotations__.keys())
        writer.writeheader()
        for book in books:
            writer.writerow(book.__dict__)

def load_members(data_dir):
    file_path = os.path.join(data_dir, 'members.csv')
    ensure_file_exists(file_path, ['MemberID', 'Name', 'Email'])
    members = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            members.append(row)
    return members


def load_users(data_dir):
    file_path = os.path.join(data_dir, 'users.csv')
    ensure_file_exists(file_path, ['Email', 'PasswordHash', 'Role', 'ReferenceID'])
    users = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row)
    return users


def save_members(data_dir, members):
    with open(os.path.join(data_dir, 'members.csv'), 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=Member.__annotations__.keys())
        writer.writeheader()
        for member in members:
            writer.writerow(member.__dict__)

def load_loans(data_dir):
    file_path = os.path.join(data_dir, 'loans.csv')
    ensure_file_exists(file_path, ['LoanID', 'MemberID', 'ISBN', 'IssueDate', 'DueDate', 'ReturnDate'])
    loans = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            loans.append(row)
    return loans


def save_loans(data_dir, loans):
    file_path = os.path.join(data_dir, 'loans.csv')
    ensure_file_exists(file_path, ['LoanID', 'MemberID', 'ISBN', 'IssueDate', 'DueDate', 'ReturnDate'])
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['LoanID', 'MemberID', 'ISBN', 'IssueDate', 'DueDate', 'ReturnDate'])
        writer.writeheader()
        writer.writerows(loans)

