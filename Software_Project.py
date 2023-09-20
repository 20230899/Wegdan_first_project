# Define a Ticket class to represent support tickets
class Ticket:
    counter = 2000
    
    def __init__(self, creator, staff_id, email, description):
        # Initialize ticket attributes
        self.ticket_number = Ticket.counter  # Assign a unique ticket number
        Ticket.counter += 1  # Increment the counter for the next ticket
        self.creator = creator
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"  # Default response
        self.status = "Open"  # Default status is "Open"
        
    def resolve_ticket(self):
        # Resolve the ticket based on its description
        if "Password Change" in self.description:
            self.response = self.generate_new_password()
        else:
            self.response = "Issue Resolved"
        self.status = "Closed"  # Update the ticket status to "Closed"
        
    def generate_new_password(self):
        # Generate a new password for password change requests
        return self.staff_id[:2] + self.creator[:3]

# Define a TicketManager class to manage support tickets
class TicketManager:
    def __init__(self):
        self.tickets = []  # Initialize an empty list to store tickets
        
    def add_ticket(self, ticket):
        # Add a new ticket to the list
        self.tickets.append(ticket)
        
    def print_ticket_stats(self):
        # Print statistics about the tickets
        open_tickets = sum(1 for ticket in self.tickets if ticket.status == "Open")
        closed_tickets = len(self.tickets) - open_tickets
        print(f"Tickets Created: {len(self.tickets)}")
        print(f"Tickets Resolved: {closed_tickets}")
        print(f"Tickets To Solve: {open_tickets}")
        
    def print_tickets(self):
        # Print details of all tickets
        for ticket in self.tickets:
            print(f"Ticket Number: {ticket.ticket_number}")
            print(f"Ticket Creator: {ticket.creator}")
            print(f"Ticket Status: {ticket.status}")

# Main program
if __name__ == "__main__":
    manager = TicketManager()
    
    # Create and add three sample tickets
    manager.add_ticket(Ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working"))
    manager.add_ticket(Ticket("Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera"))
    manager.add_ticket(Ticket("John", "JOHNS", "john@whitecliffe.co.nz", "Password Change"))
    
    # Print ticket statistics and details
    manager.print_ticket_stats()
    manager.print_tickets()
    
    # Resolve two tickets
    manager.tickets[0].resolve_ticket()
    manager.tickets[2].resolve_ticket()
    
    # Print updated ticket statistics and details
    manager.print_ticket_stats()
    manager.print_tickets()

