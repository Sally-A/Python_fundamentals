from donations_pkg.homepage import *
# from donations_pkg.homepage imp
from donations_pkg.user import login
from donations_pkg.user import register
from donations_pkg.user import donate


database = {"admin": "password123"}
donations = []
authorized_user = ""


while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    choice = input("Choose an option: ")
    print()
    if choice == "1":
        username = input("Enter user name: ")
        password = input("Enter user password: ")
        print()
        authorized_user = login(database, username, password)

    elif choice == "2":
        username = input("Enter user name: ")
        password = input("Enter user password: ")
        print()
        authorized_user = register(database, username)

        if authorized_user:
            database[authorized_user] = password

    elif choice == "3":
        if not authorized_user:
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    elif choice == "4":
        show_donations(donations)

    elif choice == "5":
        print("Leaving DonateMe ...\n")
        break
