import argparse
from regex_tester import validate_email, validate_phone_number, validate_regex, validate_string_against_regex


def main():
    parser = argparse.ArgumentParser(description="CLI Regular Expression Tester")
    parser.add_argument("-r", "--regex", type=str, help="Regular expression to test against the text")
    parser.add_argument("-t", "--text", type=str, help="Text to be tested by the regular expression")
    parser.add_argument("-ve", "--email", type=str, help="Validate email.")
    parser.add_argument("-vp", "--phone", type=str, help="Validate US Phone Number.")

    args = parser.parse_args()

    if args.regex:
        print("---Validate Regex---")
        validate_regex(args.regex)

    if args.regex and args.text:
        print("---Validate Text---")
        validate_string_against_regex(args.text, args.regex)

    if args.email:
        print("---Validate Email---")
        validate_email(args.email)

    if args.phone:
        print("---Validate Phone Number")
        validate_phone_number(args.phone)


if __name__ == "__main__":
    main()
