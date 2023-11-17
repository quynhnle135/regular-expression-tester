import re

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}"


def validate_email(email):
    email = re.match(EMAIL_PATTERN, email)
    if email:
        print(f"This {email.group()} is a valid email")
    else:
        print(f"Not valid.")
        return None


def validate_email_using_search(text):
    found = re.search(EMAIL_PATTERN, text)
    print(found)
    if found:
        print(f"Found valid email in {text}")
    else:
        print(f"No valid email is found.")


def find_all_emails(text):
    pass


def main():
    text1 = "example@gmail.com"
    text2 = "another_example@gmail.com"
    text3 = "learning@educative.edu"
    text4 = "not an email"
    text5 = "my email is example@gmail.com"
    text6 = "my name is hailey"

    # validate_email(text1)
    # validate_email(text2)
    # validate_email(text3)
    # validate_email(text4)
    # validate_email(text5)
    # validate_email(text6)

    print()

    validate_email_using_search(text1)
    validate_email_using_search(text2)
    validate_email_using_search(text3)
    validate_email_using_search(text4)
    validate_email_using_search(text5)
    validate_email_using_search(text6)


if __name__ == "__main__":
    main()