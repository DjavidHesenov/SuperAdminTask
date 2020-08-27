positions = ["superadmin", "admin", "editor", "user"]
superadmin = ["Cavid", "1234"]
logins = ["Celal"]
passwords = ["1212"]
userpositions = ["user"]

choice = input("""
Insert '1' to log in.
Insert '2' to register.
Insert '3' to delete a user.
Insert 'stop' to stop the program.
""")

def adminpage():
    ChangedLogin = input("Insert username of person to change . ")
    index = logins.index(ChangedLogin)
    if ChangedLogin in logins:
        ChangedOption = input("Insert '0' to make person 'SuperAdmin', '1' to 'Admin', '2' to 'Editor', '3' to 'User' . ")
        if ChangedOption == '0':
            print(f"{superadmin[0]}, now you are Admin, and {ChangedLogin} is SuperAdmin")
            superadmin[0], ChangedLogin = ChangedLogin, superadmin[0]
            superadmin[1], passwords[index] = passwords[index], superadmin[1]
            print(superadmin)
        elif ChangedOption == '1':
            print(f"Now {ChangedLogin} is admin")
            userpositions[index] = positions[1]
        elif ChangedOption == '2':
            print(f"Now {ChangedLogin} is editor")
            userpositions[index] = positions[2]
        elif ChangedOption == '3':
            print(f"Now {ChangedLogin} is user")
            userpositions[index] = positions[3]
        else:
            print("Incorrect input. Use numbers from 0 to 3")
            adminpage()
    else:
        print("There's no such person. ")

def choice1():
    login = input("Login: ")
    password = input("Password: ")
    position = input("Position: ").lower()
    if position == "superadmin" and login == superadmin[0] and password == superadmin[1]:
        adminpage()
    elif login in logins:
        userIndex = logins.index(login)
        passwordIndex = passwords.index(password)
        positionIndex = userpositions.index(position)
        if userIndex == passwordIndex == positionIndex:
            if position == "user":
                print(f"Hi, {login}")
            if position == "editor":
                print(f"Hi, {login} / editor.")
            if position == "admin":
                print(f"Hi, {login} / admin")

    else:
        print("Incorrect username or password. ")
        print("------------------------------------------")
        choice1()


def choice2():
    NewName = input("Insert username: ")
    NewPassw = input("Insert password: ")
    NewPassCheck = input("Insert password again: ")
    print("------------------------------------------")
    if NewName in logins:
        print("Such name is already used")
        print("------------------------------------------")
        choice2()
    elif NewPassw != NewPassCheck:
        print("Passwords don't match")
        print("------------------------------------------")
        choice2()
    elif NewName not in logins and NewPassw == NewPassCheck:
        logins.append(NewName)
        passwords.append(NewPassw)
        userpositions.append("user")
        print(logins)
        print(passwords)
        print(userpositions)


def program():
    if choice == "1":
        choice1()
    elif choice == "2":
        choice2()
    elif choice == "stop":
        return
    else:
        print("Incorrect input. ")
        program()

program()