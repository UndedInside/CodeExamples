count = 0

while count < 3:
    userPass = input("Please enter the password: ")
    if userPass == "UndedIs1337":
        print("Welcome Unded")
        break
    else:
        print("Incorrect password")
        count += 1
