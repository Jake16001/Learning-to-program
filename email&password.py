email = input("Enter your email: ")
password = input("Enter your password: ")
bold = '\033[1m'

while True:
    print(bold + "You entered:")
    print("Email: " + email)
    print("Password: " + password)
    print("Is this correct?")
    answer = input("Y/N: ")

    if answer.upper() == "Y":
        print("Thank you for entering your email and password.")
        break
    elif answer.upper() == "N":
        print("Please re-enter your email.")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
