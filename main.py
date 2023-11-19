# creating a ticket class with a property of all_tickets to store every ticket that is created and ticket_counter to generate a unique id for each ticket
class Tickets:
    all_tickets = []
    ticket_counter = 2000

# creating attributes/schema for each ticket in the all_tickets array 
    def __init__(self, name, email, staffID, description):
        self.name = name
        self.email = email
        self.staffID = staffID
        self.description = description
        self.status = "Open"
        self.ticketID = Tickets.ticket_counter
        self.user_responses = []
        self.internal_responses = []
        Tickets.ticket_counter += 1
        Tickets.all_tickets.append(self)

# some fancy stringify function to make tickets readable in the console
    def __str__(self):
        return f"Ticket ID: {self.ticketID}\nName: {self.name}\nEmail: {self.email}\nStaff ID: {self.staffID}\nDescription: {self.description}\nStatus: {self.status}\nUser Responses: {self.user_responses}\nInternal Responses: {self.internal_responses}"

    def __repr__(self):
        return self.__str__()
    
# defining the submit_ticket function with a parameter of staffID to prevent repition at the user's end
def submit_ticket(staffID, name, email):
    print("\nSubmit a ticket")
    # setting the description parameter to be a user input
    description = input("Please describe your issue: ")
    new_ticket = Tickets(name, email, staffID, description)
    print("\nTicket Summary - \nName: {}\nEmail: {}\nStaff ID: {}\nDescription: {}".format(
        new_ticket.name, new_ticket.email, new_ticket.staffID, new_ticket.description
    ))
    print("Ticket submitted successfully.\n")
    # check if ticket contains the string "passsword change"
    if "password change" in description.lower():
        new_password = staffID[:2] + name[:3]
        response = "Here is your new password: " + new_password
        new_ticket.user_responses.append(response)
        new_ticket.status = "Resolved"
        
# displays all tickets that were created by the currently logged in user - if the staffID on a ticket matches staff_id of current user then print else skip
def show_all_tickets_created_by_user(staff_id):
    print("\nShowing all tickets...\n")
    
    # loop through all tickets and check if staffID matches
    for ticket in Tickets.all_tickets:
        if ticket.staffID == staff_id:
            print(f"Ticket ID: {ticket.ticketID}")
            print(f"Description: {ticket.description}")
            
            if not ticket.user_responses:
                print("Responses: No response yet")
            else:
                print(f"Responses: {ticket.user_responses}")
            
            print(f"Status: {ticket.status}\n")

# update ticket properties based on a provided ticket ID
def update_ticket():
    ticket_id = int(input("What is the ID of the ticket you would like to update? "))
    
    #loop through all tickets and check if the ticket ID matches
    for ticket in Tickets.all_tickets:
        if ticket.ticketID == ticket_id:
            response_type = int(input("Type 1 for an internal response or 2 for a response back to the ticket creator: "))
            new_response = input("What is your response? ")

            if response_type == 1:
                ticket.internal_responses.append(new_response)
            elif response_type == 2:
                ticket.user_responses.append(new_response)

            print("\nResponse added successfully.\n")

            update_status = input("\nDo you wish to update the ticket status? (Y or N): ").lower()
            
            #asks if the ticket requires a status update
            if update_status == "y":
                print("\nTicket statuses\n1: Open\n2: In progress\n3: Awaiting customer response\n4: Resolved\n")
                change_status_to = int(input("Select the number to update the ticket status: "))
                
                # update ticket status based on user response
                if change_status_to == 1:
                    ticket.status = "Open"
                elif change_status_to == 2:
                    ticket.status = "In progress"
                elif change_status_to == 3:
                    ticket.status = "Awaiting customer response"
                elif change_status_to == 4: 
                    ticket.status = "Resolved"
                else:
                    print("\nInvalid status selection.")

                print("\nTicket status updated successfully.")

            print(f"\n{ticket}")
            break
    else:
        print(f"\nTicket with ID {ticket_id} not found.")

# show all tickets in Ticket.all_tickets array       
def show_all_tickets():
    for ticket in Tickets.all_tickets:
        print(f"\n{ticket}")

# prompts the user to respond to a ticket
def user_respond_to_ticket():
    print("\nResponding to ticket...")
    ticket_id = int(input("\nWhat is the ticket ID? "))
    
    #loops through each ticket and if ticket id matches supplied ticket id then prompt the user to provide their update otherwise skip
    for ticket in Tickets.all_tickets:
        if ticket.ticketID == ticket_id:
            response = input("What is your response? ")
            ticket.user_responses.append(response)
            print("\nResponse added successfully.\n")
            print("Ticket Summary - \nName: {}\nEmail: {}\nStaff ID: {}\nDescription: {}\nResponses: {}".format(
                ticket.name, ticket.email, ticket.staffID, ticket.description, ticket.user_responses
            ))
            break
    else:
        print(f"\nTicket {ticket_id} does not exist.\n")

# returns all tickets at status of "Open"
def check_open_tickets():
    print("\nGrabbing open tickets")
    
    # loop through and check if ticket status equals "Open" if yes then print ticket
    for ticket in Tickets.all_tickets:
        if ticket.status == "Open":
            print(ticket)

# show ticket statistics            
def show_ticket_dashboard():
    
    # len function counts how many items in Ticket.all_tickets array and returns the number of items in the array
    total_tickets = len(Tickets.all_tickets)
    # set totals to 0
    total_tickets_to_resolve = 0
    total_tickets_resolved = 0
    total_tickets_with_no_response = 0
    
    # loop through each ticket
    for ticket in Tickets.all_tickets:
        
        # if ticket isn't "Resolved" add 1 to total_tickets_to_resolve
        if ticket.status in ["Open", "In progress", "Awaiting customer response"]:
            total_tickets_to_resolve += 1
            
        # if ticket is "Resolved" add 1 to total_tickets_resolved
        elif ticket.status == "Resolved":
            total_tickets_resolved += 1
            
        # if ticket isn't "Resolved" add 1 to total_tickets_with_no_response
        if not ticket.user_responses:
            total_tickets_with_no_response += 1
    # print ticket statistics
    print(f"\nTicket Statistics \nTickets created: {total_tickets} \nTickets not resolved: {total_tickets_to_resolve} \nTickets resolved: {total_tickets_resolved}\nTotal tickets with no response {total_tickets_with_no_response}\n")
    print("Do you want to see the list of tickets?")
    see_all_tickets = input("Y or N ").lower()
    
    # ask if user wishes to see all the tickets and their properties/details
    if see_all_tickets == "y":
        
        #loop through and print each ticket
        for ticket in Tickets.all_tickets:
            print(f"\n{ticket}\n")
        
    
# start of app
def main():
    while True:
        
        # reset user details
        role = None
        staff_id = None
        name = None
        email = None
        
        # Log in
        print("LOG IN\n")
        
        # Asks for user's details at a global level to prevent repition
        role = input("Please type select role you are: \n1: User  \n2: IT team member \nWhat role are you? ")
        staff_id = input("What is your staff_id? ")
        name = input("What is your name? ")
        email = input("What is your email? ")

        # if user has a role of "User"
        if role == "1":
            while True:
                print("\n----------------------\nPlease select one of the following options: \n0: Log out \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket\n")

                user_input = input("What would you like to do? ")

                #calling functions based on user response
                if user_input == "0":
                    print("Logging out...")
                    break

                if user_input == "1":
                    submit_ticket(staff_id, name, email)

                if user_input == "2":
                    show_all_tickets_created_by_user(staff_id)

                if user_input == "3":
                    user_respond_to_ticket()

                if user_input == "help":
                    print("Please select one of the following options: \n0: Log out \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket \n4: Re-open resolved ticket \n5: Show ticket statistics")

                else:
                    print("Please select a number from one of the options above. If you would like a reminder, please type 'help'")
        
        # if user has a role of "IT team member"
        elif role == "2":
            while True:
                print("\n----------------------\nPlease select one of the following options: \n0: Log out \n1: Check all Open tickets \n2: Check all tickets\n3: Update ticket \n4: Go to ticket dashboard\n")

                user_input = input("What would you like to do? ")

                #calling functions based on IT team member's response
                if user_input == "0":
                    print("Logging out...")
                    break

                if user_input == "1":
                    check_open_tickets()

                if user_input == "2":
                    show_all_tickets()
                    
                if user_input == "3":
                    update_ticket()

                if user_input == "4":
                    show_ticket_dashboard()


                else:
                    print("Please select a number from one of the options above")

# return to beginning of app
main()
