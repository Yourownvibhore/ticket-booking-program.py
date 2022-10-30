
from msvcrt import getch


class Train:
    tejasSeats = 1000
    train18Seats = 1000
    rajdhaniSeats = 1000
    bulletSeats = 1000

    def __init__(self):
        # self.seats=seats
        pass

    def bookTickets(self, name):

        # 10 seats are kept reserved....
        print("------------------------------")
        if name == "tejas" and self.tejasSeats > 10:
            print(
                f"congo! your seat is book and your seat no. {self.tejasSeats} in train {name}")
            Train.tejasSeats -= 1
            print(f"total available seats in {name} are = {self.tejasSeats}")
            print("------------------------------")
            print(d)
            getch()
        elif name == "train18" and self.train18Seats > 10:
            print(
                f"congo! your seat is book and your seat no. {self.train18Seats} in train {name}")
            Train.train18Seats -= 1
            print(f"total available seats in {name} are = {self.train18Seats}")
            print("------------------------------")
            print(d)
            getch()
        elif name == "bullet" and self.bulletSeats > 10:
            print(
                f"congo! your seat is book and your seat no. {self.bulletSeats} in train {name}")
            Train.bulletSeats -= 1
            print(f"total available seats in {name} are = {self.bulletSeats}")
            print("------------------------------")
            print(d)
            getch()
        elif name == "rajdhani" and self.rajdhaniSeats > 10:
            print(
                f"congo! your seat is book and your seat no. {self.rajdhaniSeats} in train {name}")
            Train.rajdhaniSeats -= 1
            print(
                f"total available seats in {name} are = {self.rajdhaniSeats}")
            print("------------------------------")
            print(d)
            getch()
        else:
            print("------------------------------")
            print("seats not available")
            print("------------------------------")
            exit()

    def getStatus(self):

        print("------------------------------")
        print(f"total available seats in TEJAS are = {self.tejasSeats}")

        print(f"total available seats in TRAIN 18 are = {self.train18Seats}")

        print(f"total available seats in BULLET are = {self.bulletSeats}")

        print(f"total available seats in RAJDHANI are = {self.rajdhaniSeats}")
        print(d)
        print("------------------------------")
        getch()

    def getFare(self):
        print("------------------------------")
        print(''' 1) Tejas = ₹5000/person
 2) train 18 = ₹6000/person
 3) rajdhani = ₹2000/person
 4) bullet = ₹10000/person  ''')
        print("------------------------------")
        print(d)

        getch()

d="Press any key to Continue"
a = input("******Enter the operation you want to perform*****8\n      B for booking tickets\n      S to check status\n      F to check fare of trains\n------press ** for exit------\n")
while a != "**":
    b = Train()
    s = Train()
    f = Train()
    if a == 'b' or a == 'B':
        name = input("Enter the train name you want to book ticket\n")
        b.bookTickets(name)
    elif a == 's' or a == 'S':
        s.getStatus()
    elif a == 'f' or a == 'F':
        f.getFare()
    elif a == "**":
        exit()
    else:
        print("invalid input")
    a = input("******Enter the operation you want to perform*****8\n B for booking tickets\n S to check status\n F to check fare of trains\n----press ** for exit-----\n")
