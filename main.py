class Tickets:
    all_tickets = []

print("Please select one of the following options: \n0: Exit \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket \n4: Re-open resolved ticket \n5: Show ticket statistics")

user_input = input("What would you like to do? ")

if user_input == "0":
    print("Exiting...")
    quit()

if user_input == "1":
    print("Submitting helpdesk ticket...")
    name = input("What is your name? ")
    email = input("What is your email? ")
    staffID = input("What is your staff ID? ")
    description = input("What is your issue? ")
    print("Ticket Summary - \nName: " + name + "\nEmail: " + email + "\nStaff ID: " + staffID + "\nDescription: " + description)
    class Ticket:
        def __init__(self, name, email, staffID, description):
            self.name = name
            self.email = email
            self.staffID = staffID
            self.description = description
            self.status = "Open"
            self.ticketID = len(Tickets.all_tickets) + 1
            
            
            Tickets.all_tickets.append(self)
    
    print("Ticket submitted successfully.")
    user_input = input("What would you like to do? ")

if user_input == "2":
    print("Getting all tickets...")
    print(Tickets.all_tickets)

if user_input == "3":
    print("Responding to ticket...")
    
if user_input == "4":
    print("Re-opening resolved ticket...")
    
if user_input == "5":
    print("Showing ticket statistics...")

if user_input == "help":
    print("Please select one of the following options: \n0: Exit \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket \n4: Re-open resolved ticket \n5: Show ticket statistics")
    
else :
    print("Please select a number from one of options above if you would like reminder please type 'help'")