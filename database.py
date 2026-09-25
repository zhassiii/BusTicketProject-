import csv
import os

FILENAME = "tickets.csv"
#Function that saves a ticket
def save_ticket(name, ticket, price, quantity):
    #Checks if the file exists
    isTrue = os.path.isfile("tickets.csv")
    #Mode 'a' - append. Stores new data without deleting everything else
    with open(FILENAME, mode='a', newline='') as file:
        fieldnames = ["name", "ticket", "price", "tickets_purchased"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        #If the file does not exist it prints out column names
        if not isTrue:
            writer.writeheader()
            #Saves the data as the new rows
        writer.writerow({"name": name, "ticket": ticket, "price": price, "tickets_purchased": quantity})
#Function that allows admin to view the ticket
def view_tickets():
    if not os.path.isfile(FILENAME):
        return "No tickets available"
    #Formats the headers appropriately in the console
    print(f'\n{"Name":<15} {"Ticket":<45} {"Price":<10} {"Tickets Purchased":<5}')
    print("-"*90)
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        #Prints out the data from the file
        for row in reader:
            print(f'{row["name"]:<14}  {row["ticket"]:<44}  {row["price"]:<10}  {row["tickets_purchased"]:<15}')
#Function to update the prices
def newPrice(changedTitle, priceChange):
    filename = "mobile_products.csv"
    newRows = []
    with open(filename, mode='r', newline='') as csvfile:
        csvReader = csv.DictReader(csvfile)
        fieldnames = csvReader.fieldnames

        for line in csvReader:
            #Checks if the wanted title exists
            if line["topup_title"] == changedTitle:
                adminResp = input(f"Are you sure you wish to change {changedTitle} to {priceChange} ")
                if adminResp.lower() == "yes":
                    print("Success! The price is changed!")
                else:
                    print("Try again!")
                line["topup_price_in_pence"] = priceChange
                #Stores the new price with its title into the list
            newRows.append(line)
#Overwrites the data, not just creates a new line
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(newRows)
#Function to store admins
names = {}
def adminLogin(fullName, password):
    if fullName not in names:
        names[fullName] = password
    return


