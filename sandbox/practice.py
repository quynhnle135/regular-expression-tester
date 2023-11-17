import re


# pat = re.compile(r"[a-zA-Z0-9]+")
# test = input("Enter the string")
#
# if re.fullmatch(pat, test):
#     print(f"{test} is an alphanumeric string")
# else:
#     print(f"{test} is NOT an alphanumeric string")

word_5 = re.compile(r"\b\w{5}\b")
text1 = "hello seven learn python software update"
words = word_5.findall(text1)
print(words)