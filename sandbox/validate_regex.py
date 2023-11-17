import re


def validate_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


def main():
    correct_pattern_1 = r"cat"
    correct_pattern_2 = r"\d{2}"
    correct_pattern_3 = r".123"
    incorrect_pattern_1 = r".*"
    incorrect_pattern_2 = r"(\d{2}"
    print(validate_regex(correct_pattern_1))
    print(validate_regex(correct_pattern_2))
    print(validate_regex(correct_pattern_3))
    print(validate_regex(incorrect_pattern_1))
    print(validate_regex(incorrect_pattern_2))
    print("---")
    regex_patterns = ["\d+", "(", "[a-z]", correct_pattern_1, correct_pattern_2, correct_pattern_3, incorrect_pattern_1, incorrect_pattern_2]
    for pattern in regex_patterns:
        is_valid = validate_regex(pattern)
        if is_valid:
            print(f"Regex {pattern} is valid")
        else:
            print(f"Regex {pattern} is not valid")


if __name__ == "__main__":
    main()