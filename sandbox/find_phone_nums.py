import re


def validate_phone_number(num):
    valid_num = re.match(r"\+1-\d{3}-\d{3}-\d{4}", num)
    if valid_num:
        print(f"{num} is a VALID phone number")


def validate_phone_number_ii(num):
    valid_num = re.match(r"^(\+\d{1,})?[\-\s]?\(?[0-9]{3}\)?[\-\s]?[0-9]{3}[\-\s]?[0-9]{4}$", num)
    if valid_num:
        print(f"This {num} phone number is VALID.")


def main():
    validate_phone_number("+1-123-456-7890")
    validate_phone_number("1234567890")
    validate_phone_number("123-456-7890")
    validate_phone_number("(123) 456-7890")
    print("---")
    validate_phone_number_ii("+1-123-456-7890")
    validate_phone_number_ii("1234567890")
    validate_phone_number_ii("123-456-7890")
    validate_phone_number_ii("(123) 456-7890")


if __name__ == "__main__":
    main()