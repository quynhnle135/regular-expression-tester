import re


EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}"
PHONE_NUMBER_PATTERN = r"\+\d{1}[\-\s]?\(?[0-9]{3}\)?[\-\s]?[0-9]{3}[\-\s]?[0-9]{4}"


def validate_regex(regex):
    try:
        re.compile(regex)
        print(f"This {regex} regular expression is VALID")
        return re.compile(regex)
    except re.error:
        print("NOT VALID")
        return None


def validate_string_against_regex(text, args):
    # Check for patterns
    if args.email:
        print("Check for valid email")
        regex_pattern = EMAIL_PATTERN
    elif args.phone:
        print("Check for valid phone number")
        regex_pattern = PHONE_NUMBER_PATTERN
    else:
        regex_pattern = args.regex

    # Check for flags
    flag = None
    if args.ignorecase:
        flag = re.IGNORECASE
    elif args.multiline:
        flag = re.MULTILINE
    else:
        if args.flag:
            flag = args.flag

    try:
        if flag:
            pattern = re.compile(regex_pattern, flag)
        else:
            pattern = re.compile(regex_pattern)

        if pattern:
            matches = list(pattern.finditer(text))
            for match in matches:
                start, end = match.span()
                match_text = match.group()

                if start == 0 and end == len(text):
                    print("The entire text is fully matched.")
                else:
                    print("Only a part of the text is matched.")

                print(f"Match found: {match_text} positions from {start} to {end}")
    except re.error:
        print("Invalid Regular Expression")


def validate_email(text):
    valid_email = re.search(EMAIL_PATTERN, text)
    if valid_email:
        print(f"{text} is valid.")
        return valid_email.group()
    else:
        print(f"{text} is NOT valid.")
        return None


def validate_phone_number(text):
    valid_num = re.search(PHONE_NUMBER_PATTERN, text)
    if valid_num:
        print(f"{text} is a VALID phone number.")
        return valid_num.group()
    else:
        print(f"{text} is NOT a valid phone number.")
