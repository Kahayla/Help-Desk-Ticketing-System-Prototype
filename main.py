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
        return f"Ticket ID: {self.ticketID}\nName: {self.name}\nEmail: {self.email}\nStaff ID: {self.staffID}\nDescription: {self.description}\nStatus: {self.status}\n"
    
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

# def password_change(staffID,name,description):
#     if "password change" in description.lower():
#         new_password = staffID[:2]+name[:3]

def password_change(ticketID,staffID,name):
    for ticket in Tickets:
        if ticket.ticketID == ticketID and "password change" in ticket.description.lower() :
            new_password = staffID[:2]+name[:3]
            response = "Here is your new password: " + new_password
            ticket.user_responses.append(response)
            ticket.status = "Resolved"
    
    
def show_all_tickets(staffID):
    print("Showing all tickets...")
    for ticket in Tickets.all_tickets:
        if ticket.staffID == staffID:
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
        print("Ticket" + ticket_id + "does not exist.")



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
                    show_all_tickets(staff_id)

                if user_input == "3":
                    user_respond_to_ticket()

                if user_input == "help":
                    print("Please select one of the following options: \n0: Log out \n1: Submit helpdesk ticket \n2: Show all tickets \n3: Respond to ticket \n4: Re-open resolved ticket \n5: Show ticket statistics")

                else:
                    print("Please select a number from one of the options above. If you would like a reminder, please type 'help'")

        elif role == "2":
            print("IT member")

main()
