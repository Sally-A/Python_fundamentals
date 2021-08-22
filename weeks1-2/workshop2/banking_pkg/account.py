def show_balance(balance):
    print("Current Balance: ${:.2f}".format(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: $")
    return balance + float(amount)


def withdraw(balance):
    amount = input("Enter amount to withdraw: $")
    if float(amount) > balance:
        print("Not enough funds in account")
        return balance
    else:
        return balance - float(amount)


def logout(name):
    print("Goodby " + name + "!")
