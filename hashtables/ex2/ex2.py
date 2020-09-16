#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    destination_dict = {}
    for ticket in tickets:
        destination_dict[ticket.source] = ticket.destination
    
    route = [None] * length
    route[0] = destination_dict["NONE"]
    for i in range(1, length):
        route[i] = destination_dict[route[i - 1]]

    return route
