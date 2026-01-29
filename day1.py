import sys

fullname = input("Enter your full name: ")
email = input("Enter your email: ")
mobile = input("Enter your mobile number: ")
age = input("Enter your age: ")

# ---------- Full Name Validation ----------
if fullname[0] == " " or fullname[-1] == " ":
    print("User Profile is INVALID")
    sys.exit()

name_parts = fullname.split(" ")
if len(name_parts) < 2:
    print("User Profile is INVALID")
    sys.exit()

# ---------- Email Validation ----------
if email.count("@") != 1 or email.count(".") == 0:
    print("User Profile is INVALID")
    sys.exit()

if email[0] == "@":
    print("User Profile is INVALID")
    sys.exit()

# ---------- Mobile Number Validation ----------
if len(mobile) != 10:
    print("User Profile is INVALID")
    sys.exit()

if not mobile.isdigit():
    print("User Profile is INVALID")
    sys.exit()

if mobile[0] == "0":
    print("User Profile is INVALID")
    sys.exit()

# ---------- Age Validation ----------
if not age.isdigit():
    print("User Profile is INVALID")
    sys.exit()

age = int(age)
if age < 18 or age > 60:
    print("User Profile is INVALID")
    sys.exit()

print("User Profile is VALID")