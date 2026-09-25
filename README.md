# BusTicketProject
A program where the user will be able to see the bus tickets they can get (an analogy of NCTX bus ticket app) and the admin can change the prices

## Use Case 1: Buying A Ticket
### Actors
- User

### Preconditions
- User is logged in (or identified as a guest)

### Trigger
- Customer selects the option as "Buy Ticket"

### Main flow
- User gets options of which category title they are looking for
- After the category is chosen, they need to pick which top up they need
- When the choices are done, the program asks the user to confirm if the top up title, price are correct
- If user has chosen grouprider tickets, the program asks for specificationse


### Postconditions
- Ticket is created and associated with customer
- Confirmation message is shown


## Use Case 2
### Actors
- Admin

### Preconditions
- Admin logs in
- Admin selects if wishes to change prices or view bought tickets

### Trigger
- Admin selects to change price
- Or admin selects to view the tickets

### Main flow
- If selected view the tickets, creating a csv file with the purchased tickets in another module
- Linking the main code with the csv file so that when the customer says YES the ticket and its price is saved
- In another module, interface for the admin to view the tickets
- If selected change the price, another module with the functions is created
- Opening a file and changing the price for the chosen topup

### Postconditions
- The file is made and can be read
- The prices are changed


## Planing
### What has been done
- I am done with creating classes and opening the file
- I have listed the options for the user of category titles
- After they have to choose which top-up they are looking for

### What needs to be completed
- Ask the user if they wish to register/login, or proceed as a guest (Done)
  - If the wish to register/login, make a program for them to add their username and password (Done)
- Create modules for options of category classes, in order to minimize the overall code (Done)
- Save the ticket and associate with a customer (Done)
- Create admin interface (Done)
- Write a code to change the price (Done)
- Align the names, titles and prices with the names (formatting) (Done)
- Used links for this project:
- https://www.w3schools.com/python/ref_func_open.asp (open() functions) learned how to use these
- https://www.w3schools.com/python/python_file_handling.asp (file handling)
- https://realpython.com/python-string-formatting/ (string formatting so that the console looks nice)
- https://www.geeksforgeeks.org/python/python-os-path-isfile-method/ (checking if file exists)


- Final conclusion regarding the project:
  After I added a login info for admin, added a code to chabfe prices and view the tickets. A lot has been unknown for thi project, however a lot has been learned as well. When the code did not work I reached out to my tutor, and researched so I can make it work (the references' links are above). The most difficult part was file handling however once learned, it became clear how it works. Having many modes with files helps to do exactly what wanted. 
