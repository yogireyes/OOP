class ParkingGarage:
    def __init__(self, total_tickets, total_parking_spaces):
        self.tickets = list(range(1, total_tickets + 1))
        self.parkingSpaces = list(range(1, total_parking_spaces + 1))
        self.currentTicket = {}
    
    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            parking_space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {"paid": False, "parking_space": parking_space}
            print(f"Ticket #{ticket} has been issued. You can now park in space #{parking_space}.")
        else:
            print("Sorry, the parking garage is full. No more tickets available.")
    
    def payForParking(self, ticket_number):
        if ticket_number in self.currentTicket:
            if not self.currentTicket[ticket_number]["paid"]:
                amount = float(input(f"Please enter the payment amount for Ticket #{ticket_number}: $"))
                self.currentTicket[ticket_number]["paid"] = True
                print(f"Ticket #{ticket_number} has been paid ${amount}. You have 15 minutes to leave.")
            else:
                print(f"Ticket #{ticket_number} has already been paid.")
        else:
            print("Invalid ticket number or does not exist.")
    
    def leaveGarage(self, ticket_number):
        if ticket_number in self.currentTicket:
            if self.currentTicket[ticket_number]["paid"]:
                parking_space = self.currentTicket[ticket_number]["parking_space"]
                self.parkingSpaces.append(parking_space)
                self.tickets.append(ticket_number)
                del self.currentTicket[ticket_number]
                print("Thank you, have a nice day!")
            else:
                amount = float(input(f"Payment is required to leave. Please enter the payment amount for Ticket #{ticket_number}: $"))
                self.currentTicket[ticket_number]["paid"] = True
                print("Ticket has been paid. You have 15 minutes to leave.")
        else:
            print("Invalid ticket number or does not exist.")

# Example usage:
garage = ParkingGarage(10, 10)  # Creating a parking garage with 10 tickets and 10 parking spaces

while True:
    user_choice = input("Enter '1' to take a ticket, '2' to pay for parking, '3' to leave the garage, or 'q' to quit: ")

    if user_choice == '1':
        garage.takeTicket()
    elif user_choice == '2':
        ticket_number = int(input("Enter your ticket number: "))
        garage.payForParking(ticket_number)
    elif user_choice == '3':
        ticket_number = int(input("Enter your ticket number: "))
        garage.leaveGarage(ticket_number)
    elif user_choice == 'q':
        break
    else:
        print("Invalid choice. Please enter '1', '2', '3', or 'q'.")
