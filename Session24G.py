import threading

lock = threading.Lock()

class MovieTicket:

    def __init__(self, name, seatNum):
        self.name = name
        self.seatNum = seatNum
        self.isBooked = False

    def showMovieTicket(self):
        print("Ticket Details: {} | {} | {}".format(self.name, self.seatNum, self.isBooked))


m1 = MovieTicket("Love Aaj Kal", 1)
m2 = MovieTicket("Love Aaj Kal", 2)
m3 = MovieTicket("Love Aaj Kal", 3)
m4 = MovieTicket("Love Aaj Kal", 4)
m5 = MovieTicket("Love Aaj Kal", 5)
rowA = [m1, m2, m3, m4, m5]



class BookMovieTicket(threading.Thread):

    def selectMovieTicket(self, ticket, email):
        self.ticket = ticket
        self.email = email

    def run(self):
        lock.acquire()
        if self.ticket.isBooked == False:
            print("----Booking for {}----".format(self.email))
            print(">> Movie Ticket Booked for {}".format(self.email))
            for i in range(0, 10):
                print(">> Processing Payments for {}".format(self.email))
            self.ticket.isBooked = True
            print(">> Email Sent to {}".format(self.email))
            self.ticket.showMovieTicket()
            print("-------------------")
        else:
            print(">> Sorry !! Ticket not Available !!")
        lock.release()


def main():
    print(">> App Started")
    user1 = BookMovieTicket()
    user2 = BookMovieTicket()

    user1.selectMovieTicket(rowA[2], "john@example.com")
    user2.selectMovieTicket(rowA[2], "mike@example.com")

    user1.start()
    user2.start()

    print(">> App Finished")


if __name__ == "__main__":
    main()


# PS: Concurrent Programming or Synchronization
# is needed for multiple threads working on same object

