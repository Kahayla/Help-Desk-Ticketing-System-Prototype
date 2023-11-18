class Tickets:
    all_tickets = []
    ticket_counter = 2000
    
    def __init__(self, name, email, staffID, description):
        self.name = name
        self.email = email
        self.staffID = staffID
        self.description = description
        self.status = "Open"
        self.ticketID = Tickets.ticket_counter
        Tickets.ticket_counter += 1
        Tickets.all_tickets.append(self)
        

def submit_ticket():
    print("Submit a ticket")
    name = input("What is your name? ")
    email = input("What is your email? ")
    staffID = input("What is your staff ID? ")
    description = input("Please describe your issue: ")
    
    new_ticket = Tickets(name, email, staffID, description)
    print("Ticket Summary - \nName: {}\nEmail: {}\nStaff ID: {}\nDescription: {}".format(
        new_ticket.name, new_ticket.email, new_ticket.staffID, new_ticket.description
    ))
    print("Ticket submitted successfully.")
    
def show_all_tickets():
    print("Showing all tickets...")
    for ticket in Tickets.all_tickets:
        print("Ticket ID: {}\nName: {}\nEmail: {}\nStaff ID: {}\nDescription: {}\nStatus: {}\n".format(
            ticket.ticketID, ticket.name, ticket.email, ticket.staffID, ticket.description, ticket.status
        ))
print("Please select one of the following options: \n0: Exit \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket \n4: Re-open resolved ticket \n5: Show ticket statistics")

user_input = input("What would you like to do? ")



if user_input == "0":
    print("Exiting...")
    quit()

if user_input == "1":
    print("Submitting helpdesk ticket...")

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