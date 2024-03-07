# main.py

from login import login

def main():
    email = "xxxxxxxx@gmail.com"
    password = "xxxxx123"
    session = login(email, password)

if __name__ == "__main__":
    main()
