import re


EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$"
PHONE_NUMBER_PATTERN = r"^(\+\d{1,})?[\-\s]?\(?[0-9]{3}\)?[\-\s]?[0-9]{3}[\-\s]?[0-9]{4}$"


def validate_email(email):
    valid_email = re.match(EMAIL_PATTERN, email)
    if valid_email:
        print(f"{email} is valid.")
        return valid_email.group()
    else:
        print(f"{email} is NOT valid.")
        return None


def validate_phone_number(num):
    valid_num = re.match(PHONE_NUMBER_PATTERN, num)
    if valid_num:
        print(f"{num} is a VALID phone number.")
        return valid_num.group()
    else:
        print(f"{num} is NOT a valid phone number.")
