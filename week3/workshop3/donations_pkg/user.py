def login(database, username, password):
    for user in database:
        if user == username:
            if database[user] == password:
                print("Welcome back", username, "\n")
                return username
            else:
                print("Incorrect password for", username, "\n")
                return ""

    print("User not found.  Please register. \n")
    return ""


def register(database, username):
    # could also do if database.has_key(username):
    if username in database:
        print("Username already registered. \n")
        return ""
    else:
        print("Username has been registered. \n")
        return username


def donate(username):
    donation = ""
    donation_amt = float(input("Enter the amoount to donate: "))
    #donation = (username + " donated $" + str(donation_amt))
    donation = (username + " donated ${:.2f}".format(donation_amt))
    print("Thank you for your donation!")
    return donation
