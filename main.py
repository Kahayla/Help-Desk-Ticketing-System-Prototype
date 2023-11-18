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
        self.user_responses = []
        self.internal_responses = []
        Tickets.ticket_counter += 1
        Tickets.all_tickets.append(self)

    def __str__(self):
        return f"Ticket ID: {self.ticketID}\nName: {self.name}\nEmail: {self.email}\nStaff ID: {self.staffID}\nDescription: {self.description}\nStatus: {self.status}\nUser Responses: {self.user_responses}\nInternal Responses: {self.internal_responses}"

    def __repr__(self):
        return self.__str__()

def submit_ticket(staffID):
    print("Submit a ticket")
    name = input("What is your name? ")
    email = input("What is your email? ")
    description = input("Please describe your issue: ")

    new_ticket = Tickets(name, email, staffID, description)
    print("Ticket Summary - \nName: {}\nEmail: {}\nStaff ID: {}\nDescription: {}".format(
        new_ticket.name, new_ticket.email, new_ticket.staffID, new_ticket.description
    ))
    print("Ticket submitted successfully.")

    # Check if the description contains "password change" and apply the logic
    if "password change" in description.lower():
        new_password = staffID[:2] + name[:3]
        response = "Here is your new password: " + new_password
        new_ticket.user_responses.append(response)
        new_ticket.status = "Resolved"

def show_all_tickets_created_by_user(staffID):
    print("Showing all tickets...")
    for ticket in Tickets.all_tickets:
        if ticket.staffID == staffID:
            print("Ticket ID:", ticket.ticketID)
            print("Description:", ticket.description)
            print("Status:", ticket.status)
            print("Responses:", ticket.user_responses)
           

def update_ticket():
    ticket_id = int(input("What is the ID of the ticket you would like to update? "))
    
    for ticket in Tickets.all_tickets:
        if ticket.ticketID == ticket_id:
            response_type = int(input("Type 1 for an internal response or 2 for a response back to the ticket creator: "))
            new_response = input("What is your response? ")

            if response_type == 1:
                ticket.internal_responses.append(new_response)
            elif response_type == 2:
                ticket.user_responses.append(new_response)

            print("Response added successfully.")

            update_status = input("Do you wish to update the ticket status? (Y or N): ").lower()
            
            if update_status == "y":
                print("Ticket statuses\n1: Open\n2: In progress\n3: Awaiting customer response\n4: Resolved")
                change_status_to = int(input("Select the number to update the ticket status: "))
                
                if change_status_to == "1":
                    ticket.status = "Open"
                elif change_status_to == "2":
                    ticket.status = "In progress"
                elif change_status_to == "3":
                    ticket.status = "Awaiting customer response"
                elif change_status_to == "4": 
                    ticket.status = "Resolved"
                else:
                    print("Invalid status selection.")

                print("Ticket status updated successfully.")

            print(ticket)
            break
    else:
        print(f"Ticket with ID {ticket_id} not found.")
def show_all_tickets():
    for ticket in Tickets.all_tickets:
        print(ticket)
    
    

def user_respond_to_ticket():
    print("Responding to ticket...")
    ticket_id = int(input("What is the ticket ID? "))
    response = input("What is your response? ")
    for ticket in Tickets.all_tickets:
        if ticket.ticketID == ticket_id:
            ticket.user_responses.append(response)
            print("Response added successfully.")
            print("Ticket Summary - \nName: {}\nEmail: {}\nStaff ID: {}\nDescription: {}\nResponses: {}".format(
                ticket.name, ticket.email, ticket.staffID, ticket.description, ticket.user_responses
            ))
            break
    else:
        print(f"Ticket {ticket_id} does not exist.")

def check_open_tickets():
    print("Grabbing open tickets")
    for ticket in Tickets.all_tickets:
        if ticket.status == "Open":
            print(ticket)

def main():
    while True:
        role = None
        staff_id = None
        print(f"Role: {role}, Staff ID: {staff_id}")
        print("LOG IN")
        role = input("Please type select role you are: \n1: User  \n2: IT team member \nWhat role are you?")
        staff_id = input("What is your staff_id?")

        if role == "1":
            while True:
                print("Please select one of the following options: \n0: Log out \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket")

                user_input = input("What would you like to do? ")

                if user_input == "0":
                    print("Logging out...")
                    break

                if user_input == "1":
                    submit_ticket(staff_id)

                if user_input == "2":
                    show_all_tickets_created_by_user(staff_id)

                if user_input == "3":
                    user_respond_to_ticket()

                if user_input == "help":
                    print("Please select one of the following options: \n0: Log out \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket \n4: Re-open resolved ticket \n5: Show ticket statistics")

                else:
                    print("Please select a number from one of the options above. If you would like a reminder, please type 'help'")

        elif role == "2":
            while True:
                print("Please select one of the following options: \n0: Log out \n1: Check all Open tickets \n2: Check all tickets\n3: Update ticket \n4: Go to ticket dashboard")

                user_input = input("What would you like to do? ")

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
                    user_respond_to_ticket()

                if user_input == "help":
                    print("Please select one of the following options: \n0: Log out \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket \n4: Re-open resolved ticket \n5: Show ticket statistics")

                else:
                    print("Please select a number from one of the options above. If you would like a reminder, please type 'help'")


main()
