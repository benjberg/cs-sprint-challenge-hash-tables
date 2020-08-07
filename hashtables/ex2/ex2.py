#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    #define route lenght and location
    route = [None] * length
    location = {}
    #loop through our tickets setting ticket source to dest and next location to none
    for ticket in tickets:
        location[ticket.source] = ticket.destination
    next = location["NONE"]
    #loop over length setting the route index to the next location and the next to the next location in the list 
    for i in range(0, length):
        route[i] = next
        next = location[next]

    return route

