import bcrypt
from storage import load_members, save_members
from models import Member
from datetime import date
import uuid

def register_member(data_dir, name, email, password):
    members = load_members(data_dir)
    for m in members:
        if m.Email == email:
            print("Email already registered.")
            return
    member_id = str(uuid.uuid4().int)[:4]
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_member = Member(MemberID=member_id, Name=name, PasswordHash=pw_hash, Email=email, JoinDate=str(date.today()))
    members.append(new_member)
    save_members(data_dir, members)
    print("✔ Member registered.")

def login(data_dir, role):
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    members = load_members(data_dir)
    for member in members:
        if member.Email == email and bcrypt.checkpw(password.encode(), member.PasswordHash.encode()):
            if role == 'member' or (role == 'librarian' and member.Email == 'admin@library.com'):
                print("✔ Login successful")
                return member
    print("❌ Login failed")
    return None