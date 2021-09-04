class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, to_account, amount):
        print("\nYou are transfering $", amount, "to", to_account.name)
        print("Authentication required")
        pin_entered = int(input("Enter your pin: "))
        if pin_entered == self.pin:
            print("Transfer authorized")
            print("Transferring $", amount, "to", to_account.name)
            to_account.balance += amount
            self.balance -= amount
            return True
        else:
            print("Invalid PIN.  Transaction canceled.")
            return False

    def request_money(self, from_account, amount):
        print("\nYou are requesting $", amount, "from", from_account.name)
        print("User authentication required...")
        pin_entered = int(input("Enter " + from_account.name + "'s PIN: "))
        if pin_entered == from_account.pin:
            password_entered = input("Enter your password: ")
            if password_entered == self.password:
                print("Request authorized")
                print(from_account.name, "sent $", amount)
                #from_account.balance -= amount
                from_account.withdraw(amount)
                #self.balance += amount
                self.deposit(amount)
                return True
            else:
                print("Invalid password.  Transaction canceled.")
                return False
        else:
            print("Invalid PIN.  Transaction canceled.")
            return False


""" Driver Code for Task 1 """
""" user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password) """


""" Driver Code for Task 2 """
""" user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
user1.change_name("Bobby")
user1.change_pin(4321)
user1.change_password("newpassword")
print(user1.name, user1.pin, user1.password) """


""" Driver Code for Task 3"""
""" bankuser1 = BankUser("Bob", 1234, "password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance) """


""" Driver Code for Task 4"""
""" bankuser1 = BankUser("Bob", 1234, "password")
bankuser1.show_balance()
bankuser1.deposit(1000.00)
bankuser1.show_balance()
bankuser1.withdraw(500.00)
bankuser1.show_balance() """


""" Driver Code for Task 5"""
bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")
bankuser2.deposit(5000.0)
bankuser2.show_balance()
bankuser1.show_balance()
if bankuser2.transfer_money(bankuser1, 500.0):
    bankuser2.show_balance()
    bankuser1.show_balance()

    bankuser2.request_money(bankuser1, 250.0)

bankuser2.show_balance()
bankuser1.show_balance()
