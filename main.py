import argparse
from regex_tester import validate_regex, validate_string_against_regex


def main():
    # Main functions
    parser = argparse.ArgumentParser(description="CLI Regular Expression Tester")
    parser.add_argument("-r", "--regex", type=str, help="Regular expression to test against the text")
    parser.add_argument("-t", "--text", type=str, help="Text to be tested by the regular expression")
    parser.add_argument("-f", "--flag", type=str, help="Flag you want to include if they are not IGNORE-CASE or MULTILINE")

    # Regex flags
    flag = parser.add_mutually_exclusive_group()
    flag.add_argument("-i", "--ignorecase", action="store_true", help="Perform case-sensitive matching")
    flag.add_argument("-m", "--multiline", action="store_true", help="Allows the '^' and '$' metacharacters to match each line.")

    # Pre-defined patterns
    pattern = parser.add_mutually_exclusive_group()
    pattern.add_argument("-e", "--email", action="store_true", help="Use a predefined pattern for email validation.")
    pattern.add_argument("-p", "--phone", action="store_true", help="Use a predefined pattern for phone number validation")

    args = parser.parse_args()

    if args.regex:
        print("---Validate Regex---")
        validate_regex(args.regex)

    if args.text:
        print("---Validate Text---")
        validate_string_against_regex(args.text, args)


if __name__ == "__main__":
    main()
