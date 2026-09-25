import classes_module
from database import save_ticket

categoryObjectList = []
topUpObjectList = []
#Opening file from a module
#Calling two lists from a functions
categoryObjectList, topUpObjectList = classes_module.csvRead()
#Print the list of options of the categories to the user
user_resp = int(input("""                                       Welcome!
                    Would you like to sign in (1) or continue as a guest (2)?
                                    Pick a number: """))

if user_resp == 1:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
elif user_resp == 2:
    print("Welcome guest!" +
          "\n\nPlease pick a category number from the list below: ")
    username = "Guest"
#Printing out the category titles for user to choose from
titleNum = 0
#Iterates through a list where categories represents an instance from the list
for categories in categoryObjectList:
    print("\n", titleNum, "-", categories.getTitle(), " (" + categories.getDescription() + ")")
    titleNum += 1
response = int(input("\nYour choice: "))
#Listing top up titles for user's choice depending on the chosen category
while response > 6:
    response = int(input("\nPlease enter a number from the list above: "))
#Based off user's response, the loop lists all the top-up types for the certain category
for topup in categoryObjectList[response].topupTypes:
    print("\n-------\n"
          "Top-up title:", topup.title,
          "\nDescription:", topup.description,
          "\nPrice:",topup.getPriceinPoundAndPence(),
          "\nEligible for:", topup.passengerClassName,
          "\nTickets permitted for this top up:", topup.quantity,
          "\nEntitlement type:", topup.entitlementtype,
          "\nEntitlement value and unit:", topup.entitlementvalue, topup.entitlementunit,
          "\n-------")
topUpResp = input("\nWhich top-up name would you like to choose? ")
#A method that searches through every top-up title available for a specific category
selected_topup = categoryObjectList[response].findTopupTypesByName(topUpResp)
#Since network grouprider and grouprider have identical names but different passenger class name
#the program specifies which exactly user wants
if topUpResp in ["Network Grouprider", "Grouprider"]:
    eligibility = input("\nWould you like to get for Under 19s or Adults?: ")
    #Creates a specific instance
    selectedTicket = classes_module.specTicket(topUpResp, eligibility)
    if selectedTicket:
        print("Success!")
    else:
        print("Ticket not found.")
userResp = input("\nYour choice is: " + selected_topup.chosenTopup() +
                 "\nAre you satisfied with your choice? Yes/No ")
# Evaluating if the user is happy with their choice or not
if userResp.lower() == "yes":
    ticket_name = selected_topup.title
    ticket_price = topup.getPriceinPoundAndPence()
    tickets_purchased = topup.getTicketsPurchased()
    #Saves the ticket into a csv file
    save_ticket(username, ticket_name, ticket_price, tickets_purchased)
    print("\nThank you for choosing NCTX. Goodbye!")
elif userResp.lower() == "no":
    print("Please start over!")
