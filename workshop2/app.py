from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


balance = 0.0
print("          === Automated Teller Machine ===          ")
while True:
    user = input("Enter name to register: ")
    if len(user) < 1 or len(user) > 10:
        print("Name must be between 1 and 10, please try again")
        continue
    else:
        break
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print("PIN must be 4 digits, please try again")
        continue
    else:
        break

print()
print(user, "has been registered with a starting balance of $" + str(balance))
print()


while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == user and pin_to_validate == pin:
        print("Login successful! ")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(user)
    option = input("Choose an option: ")
    print()
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:
        account.logout(user)
        break
