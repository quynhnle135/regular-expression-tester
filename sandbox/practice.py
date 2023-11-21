import re


# pat = re.compile(r"[a-zA-Z0-9]+")
# test = input("Enter the string")
#
# if re.fullmatch(pat, test):
#     print(f"{test} is an alphanumeric string")
# else:
#     print(f"{test} is NOT an alphanumeric string")

# word_5 = re.compile(r"\b\w{5}\b")
# text1 = "hello seven learn python software update"
# words = word_5.findall(text1)
# print(words)

matches = list(re.finditer(r"\b\w{5}\b", "hello kitty quinn notquinn starbucks python script field"))
for match in matches:
    # print(match)
    start, end = match.span()
    print(start, end)
    match_text = match.group()
    print(match_text)