name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")
age = int(input("Enter Age: "))

if (
    not name.startswith(" ") and
    not name.endswith(" ") and
    name.count(" ") >= 1 and

    len(mobile) == 10 and
    mobile.isdigit() and

    age >= 18 and age <= 60 and

    email.find("@") != -1 and
    email.index("@") > 0
):
    print("User Profile is VALID")
else:
    print("User Profile is NOT VALID")
