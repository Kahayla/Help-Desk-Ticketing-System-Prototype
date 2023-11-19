# Help-Desk-Ticketing-System-Prototype

This Python script implements a Help Desk Ticketing System prototype. Below are the key functionalities and instructions for running the code in the terminal.

## Features

- **Submit a Ticket:**
  - Users can submit a helpdesk ticket by providing their staff ID, name, email, and describing the issue.
  - If the issue involves a password change, the system automatically generates a new password.
- **Show All Tickets Created by User:**
  - Displays all tickets created by the currently logged-in user.
- **Update Ticket:**
  - Allows IT team members to update ticket details, add responses, and change the ticket status.
- **Respond to Ticket:**
  - Enables users to respond to a ticket, adding their comments.
- **Check Open Tickets:**
  - IT team members can view all open tickets.
- **Show All Tickets:**
  - Displays details of all tickets in the system.
- **Show Ticket Dashboard:**
  - Provides statistics on the total number of tickets, unresolved tickets resolved tickets, and tickets with no response.

## How to run:

1. **Install:**
   - Install the [python extension](https://code.visualstudio.com/docs/languages/python) in [VS Code](https://code.visualstudio.com/) and a python interpreter.
2. **Copy repository code:**
   - Copy [git hub repository](https://github.com/Kahayla/Help-Desk-Ticketing-System-Prototype) code into VS Code
3. **Open the terminal:**
   - Navigate to the directory where the script (`main.py`) is located.
4. **Run the script:**
   - Type the following command and press enter.
   - `python3 main.py`
   - This initiates the Help Desk Ticketing system.

## How to use:

1. **Login:**
   - When prompted, select your role (_type 1 for User, 2 for IT team member_).
   - Eneter your staffID, name, and email.
2. **User Options:**
   - Users (Role 1) can do the following:
     - Type `0` to log out of system
     - Type `1` to submit new helpdesk ticket
       - This prompt asks you to then provide a description of the issue.
       - If your issue involves a password change, a new password will be automatically generated for you.
     - Type `2` to respond to tickets
