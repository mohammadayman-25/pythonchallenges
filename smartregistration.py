sid = input("Enter Student ID: ")
email = input("Enter Email ID: ")
password = input("Enter Password: ")
ref = input("Enter Referral Code: ")

valid = True

if len(sid) != 7 or sid[0:3] != "CSE" or sid[3] != "-" or not (sid[4].isdigit() and sid[5].isdigit() and sid[6].isdigit()):
    valid = False

if "@" not in email or "." not in email or email[0] == "@" or email[-1] == "@" or not email.endswith(".edu"):
    valid = False

if len(password) < 8 or not password[0].isupper() or not (
    password[0].isdigit() or password[1].isdigit() or password[2].isdigit() or
    password[3].isdigit() or password[4].isdigit() or password[5].isdigit() or
    password[6].isdigit() or password[7].isdigit()):
    valid = False

if len(ref) != 6 or ref[0:3] != "REF" or not (ref[3].isdigit() and ref[4].isdigit()) or ref[5] != "@":
    valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")
