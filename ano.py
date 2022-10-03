from decouple import config
from getpass import getpass

pwd = config("PWD")

user_name = input("Enter your name: ")
user_pwd = getpass("Enter a password: ")

if user_pwd == pwd:
    print(f"Welcome!....{user_name}")
else:
    print(f"Get out..{user_pwd}")