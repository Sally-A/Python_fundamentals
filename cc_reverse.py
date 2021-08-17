def reverse(str):
    # slice that steps backwards
    # [start:stop:step]
    return str[::-1]



name = input("What is your name? ")
print("Your name reversed is:", reverse(name))
