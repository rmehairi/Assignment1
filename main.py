class User:
    def __init__(self, name, username, password, email, phone):
        # initializing the attributes
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
    # getters and setters for the attributes
    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def set_name(self, name):
        self.name = name

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone
    # to verify the user login details
    def login(self, username_input, password_input):
        return username_input == self.username and password_input == self.password
    # will return the string format of the object
    def __str__(self):
        return f"User(name='{self.name}', username='{self.username}', email='{self.email}', phone='{self.phone}')"

class Passenger(User):

    def __init__(self, name, username, password, email, phone, referenceNumber, bookingType, bookingDate, specialNeed, age):
        # calling parent class constructor
        super().__init__(name, username, password, email, phone)
        self.referenceNumber = referenceNumber
        self.bookingType = bookingType
        self.bookingDate = bookingDate
        self.specialNeed = specialNeed
        self.age = age

    # Getters and setters for the attributes
    def get_referenceNumber(self):
        return self.referenceNumber

    def get_bookingType(self):
        return self.bookingType

    def get_bookingDate(self):
        return self.bookingDate

    def get_specialNeed(self):
        return self.specialNeed

    def get_age(self):
        return self.age

    def set_referenceNumber(self, referenceNumber):
        self.referenceNumber = referenceNumber

    def set_bookingType(self, bookingType):
        self.bookingType = bookingType

    def set_bookingDate(self, bookingDate):
        self.bookingDate = bookingDate

    def set_specialNeed(self, specialNeed):
        self.specialNeed = specialNeed

    def set_age(self, age):
        self.age = age

    def getBoardingPass(self,bookingPass):
        print("Booking Pass:\n",bookingPass)

    def verifyBookingDetails(self,ticket):
        print("Verifying Booking Details: ",ticket)
    # will return string format
    def __str__(self):
        return (f"Passenger(name='{self.name}', username='{self.username}', email='{self.email}', "
                f"phone='{self.phone}', referenceNumber='{self.referenceNumber}', bookingType='{self.bookingType}', "
                f"bookingDate='{self.bookingDate}', specialNeed='{self.specialNeed}', age='{self.age}')")

class Staff(User):
    def __init__(self, name, username, password, email, phone, responsibility, salary, designation, joiningDate, position):
        # calling parent class constructor
        super().__init__(name, username, password, email, phone)
        self.responsibility = responsibility
        self.salary = salary
        self.designation = designation
        self.joiningDate = joiningDate
        self.position = position

    # getters and setters for the attributes
    def get_responsibility(self):
        return self.responsibility

    def get_salary(self):
        return self.salary

    def get_designation(self):
        return self.designation

    def get_joiningDate(self):
        return self.joiningDate

    def get_position(self):
        return self.position

    def set_responsibility(self, responsibility):
        self.responsibility = responsibility

    def set_salary(self, salary):
        self.salary = salary

    def set_designation(self, designation):
        self.designation = designation

    def set_joiningDate(self, joiningDate):
        self.joiningDate = joiningDate

    def set_position(self, position):
        self.position = position
    # allows the user to view the booking details.
    def viewBookingDetails(self,ticket):
        print("Booking Details: \n",ticket)

    def generateBoardingPass(self):
        print("Boarding Pass Generated")
    def __str__(self):
        return (f"Staff(name='{self.name}', username='{self.username}', email='{self.email}', "
                f"phone='{self.phone}', responsibility='{self.responsibility}', salary='{self.salary}', "
                f"designation='{self.designation}', joiningDate='{self.joiningDate}', position='{self.position}')")

class Ticket:
    def __init__(self, ticketNumber, flightNumber, date, time, destination, departureAirport, passenger):
        # initializing the attributes
        self.ticketNumber = ticketNumber
        self.flightNumber = flightNumber
        self.date = date
        self.time = time
        self.destination = destination
        self.departureAirport = departureAirport
        self.passenger = passenger
        # default value for the status
        self.status = "Pending"
    # getters and setters of the attributes
    def get_ticketNumber(self):
        return self.ticketNumber

    def get_flightNumber(self):
        return self.flightNumber

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_destination(self):
        return self.destination

    def get_departureAirport(self):
        return self.departureAirport

    def get_passenger(self):
        return self.passenger

    def set_ticketNumber(self, ticketNumber):
        self.ticketNumber = ticketNumber

    def set_flightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def set_destination(self, destination):
        self.destination = destination

    def set_departureAirport(self, departureAirport):
        self.departureAirport = departureAirport

    def set_passenger(self, passenger):
        self.passenger = passenger

    def book(self):
        self.status = "Booked"
        print("Ticket Booked")

    def verify(self):
        print(self.__str__())
    # this function is to update the status of the ticket
    def changeStatus(self,status):
        self.status = status

    def __str__(self):
        return (f"Ticket(ticketNumber={self.ticketNumber}, flightNumber='{self.flightNumber}', "
                f"date='{self.date}', time='{self.time}', destination='{self.destination}', "
                f"departureAirport='{self.departureAirport}', passenger='{self.passenger}')")


class BoardingPass:
    def __init__(self, gate, boardingTill, seat, terminal, boardingStart):
        self.gate = gate
        self.boardingTill = boardingTill
        self.seat = seat
        self.terminal = terminal
        self.boardingStart = boardingStart
    # getters and setters of the attributes
    def get_gate(self):
        return self.gate

    def get_boardingTill(self):
        return self.boardingTill

    def get_seat(self):
        return self.seat

    def get_terminal(self):
        return self.terminal

    def get_boardingStart(self):
        return self.boardingStart

    def set_gate(self, gate):
        self.gate = gate

    def set_boardingTill(self, boardingTill):
        self.boardingTill = boardingTill

    def set_seat(self, seat):
        self.seat = seat

    def set_terminal(self, terminal):
        self.terminal = terminal

    def set_boardingStart(self, boardingStart):
        self.boardingStart = boardingStart

    def displayDetails(self):
        print(self.__str__())

    def checkDetails(self):
        print("Boarding Details: ")
        print(self.__str__())

    def __str__(self):
        return (f"BoardingPass(gate='{self.gate}', boardingTill='{self.boardingTill}', "
                f"seat='{self.seat}', terminal='{self.terminal}', boardingStart='{self.boardingStart}')")


# importing date and time to use Date and Time
from datetime import date, time
def main():
    # creating objects
    user1 = User("Hammad", "hammad123", "password123", "hammad@example.com", "050-123-4567")
    passenger1 = Passenger("Fatima Saeed", "fatimasaeed456", "password456", "fatimasaeed@example.com", "055-987-6543",
                           "REF789012", "Business", date(2024, 2, 22), "None", 35)
    staff1 = Staff("Mohammed Ahmed", "mohammedahmed789", "password789", "mohammedahmed@example.com", "056-789-0123",
                   "Security Officer", 6000.0, "Officer", date(2021, 12, 15), "Terminal 3")
    ticket1 = Ticket(987654, "EK202", date(2024, 2, 22), time(10, 30), "Dubai", "DXB", passenger1)
    boarding_pass1 = BoardingPass("Gate 5", time(10, 0), "B15", "Terminal 3", time(9, 30))
    # printing the details
    print("User details:")
    print(user1)
    print("Passenger details:")
    print(passenger1)
    print("Staff details:")
    print(staff1)
    print("Boarding pass details:")
    print(ticket1)
    print(boarding_pass1)
main()