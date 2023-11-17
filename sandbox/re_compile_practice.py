import re


regex_pattern = re.compile(r"^\w{5}$")
email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$")
# print(re.compile(regex_pattern))
# print(re.compile(email_pattern))
print(regex_pattern)
print(email_pattern)

valid_email = email_pattern.search("example@gmail.com")

if valid_email:
    print("Valid")
else:
    print("Not valid")


contain_foo = re.compile(r"\bfoo\b", flags=re.I)
print(contain_foo.findall("foo FOO foO FOo are my fav words ever I love fOo"))
print("---")

try:
    p = re.compile(r"\d{2")
    print(p)
    if p:
        print("True")
except re.error:
    print("False")