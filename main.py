import argparse
from regex_tester import validate_email, validate_phone_number


def main():
    parser = argparse.ArgumentParser(description="Welcome to Regular Expression Tester")
    parser.add_argument("-ve", "--email", type=str, help="Validate email.")
    parser.add_argument("-vp", "--phone", type=str, help="Validate US Phone Number.")

    args = parser.parse_args()

    if args.email:
        print("---Validate email---")
        validate_email(args.email)
    elif args.phone:
        print("---Validate phone number---")
        validate_phone_number(args.phone)


if __name__ == "__main__":
    main()
