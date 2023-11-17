import re


def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$"
    email = re.match(email_pattern, email)
    if email:
        print(f"This {email.group()} is a valid email")
    else:
        print(f"Not valid.")
        return None


def find_all_emails(text):
    pass


def main():
    validate_email("example@gmail.com")
    validate_email("not an email")


if __name__ == "__main__":
    main()