# Validate user input excerise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Input your Username: ")

if len(username) > 12:
    print("Username is too long")
if " " in username:
    print("this has spaces")
if username.find(" ") != -1:
    print("this has spaces")
if username.isdigit():
    print("this is a digit")

if not username.isalpha():
    print("this is a digit")