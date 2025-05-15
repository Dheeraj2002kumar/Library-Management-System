import argparse
from auth import register_member, login
from librarian import librarian_menu
from member import member_menu

parser = argparse.ArgumentParser()
parser.add_argument('--data-dir', default='./data')
args = parser.parse_args()

data_dir = args.data_dir

try:
    while True:
        role = input("Login as (librarian/member): ").strip().lower()
        user = login(data_dir, role)
        if user:
            if role == 'librarian':
                librarian_menu(data_dir, user)
            elif role == 'member':
                member_menu(data_dir, user)
except KeyboardInterrupt:
    print("\nExiting program. Goodbye!")
