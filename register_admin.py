# register_admin.py
from auth import register_member

if __name__ == "__main__":
    data_dir = './data'
    register_member(data_dir, "Admin", "admin@library.com", "admin123")
