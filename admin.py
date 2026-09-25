import database
print("""       Welcome to the admin's portal where you can view the tickets purchased
                    and change the prices! Please sign in.""")
fullName = input("\nWhat is your full name? ")
password = input("\nEnter your password (8 characters long): ")
while len(password) < 8:
    password = input("\nYour password must be 8 characters long.")
print("Access granted!")
database.adminLogin(fullName, password)

choice = input("Would you like to see purchased tickets (1) or change the prices (2)? ")

if choice == "1":
    print("Here is the list of the tickets purchased:")
    database.view_tickets()
elif choice == "2":
    changedTitle = input("Which top up's price would you like to choose? ")
    priceChange = int(input("What is the new price? "))
    database.newPrice(changedTitle, priceChange)
